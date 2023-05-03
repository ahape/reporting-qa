#!/usr/local/bin/python3.11
import sys, os, argparse, datetime, logging, yaml, random, markdown
from datetime import datetime as dt

OUTPUT_FILE_NAME = "README"
logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("main")
environment = None

def create_link(link):
  if environment in { "beta", "testing" }:
    link = link.replace("webapp", environment)
  elif environment == "localhost":
    link = link.replace("https://webapp.brightmetrics.com/", "http://localhost:8080/")
  bust = "?" if "?" not in link else "&"
  bust += "_qa=" + timestamp() + str(random.randint(0,999_999))
  splice = link.rindex("#") if "#" in link else len(link)
  return link[:splice] + bust + link[splice:]

def load_yaml(path):
  with open(path, "r", encoding="utf8") as stream:
    try:
      return yaml.safe_load(stream)
    except yaml.YAMLError as ex:
      logger.error("%s", ex)
  return None

def load_tests():
  groups = []

  for group_name in os.listdir("tests"):
    group = TestGroup(group_name)
    groups.append(group)
    fullpath = "tests/" + group_name
    for test_name in os.listdir(fullpath):
      json = load_yaml(fullpath + "/" + test_name)
      group.tests.append(Test(test_name, **json))

  return groups

def md_hr(title, bar):
  return "".zfill(len(title)).replace("0", bar)

class TestGroup:
  def __init__(self, name):
    self.name = (name.replace("_", " ") + " tests").upper()
    self.tests = []

class Test:
  def __init__(self, name, **kwargs):
    self.name = name.replace(".yaml", "").replace("_", " ").title()
    self.link = create_link(kwargs["link"])
    self.steps = ["  * " + bullet for bullet in kwargs["desc"]]

test_template = r"""
{name}
{hr}
  * [(link to test)]({link})
{steps}
"""

test_group_template = r"""
{name}
{hr}
{tests}
"""

def timestamp():
  return dt.strftime(dt.now(), "%Y%m%d%H%M%S")

def render():
  def render_tests(tests):
    rendered = []
    for t in tests:
      rendered.append(
        test_template.format(
          name=t.name,
          link=t.link,
          hr=md_hr(t.name, "-"),
          steps="\n".join(t.steps)))
    return "".join(rendered)

  def render_test_group(test_group):
    return test_group_template.format(
      name=test_group.name,
      hr=md_hr(test_group.name, "="),
      tests=render_tests(test_group.tests))

  def _render(test_groups):
    return "".join([render_test_group(tg) for tg in test_groups])

  return _render(load_tests())

def get_args():
  args = argparse.ArgumentParser()
  args.add_argument("-k", "--keep", action="store_true")
  args.add_argument("-v", "--verbose", action="store_true")
  args.add_argument("-e", "--environment")
  args.add_argument("--html", action="store_true")
  return args.parse_args()

def archive_existing_checklist():
  filename = OUTPUT_FILE_NAME + ".md"
  if os.path.exists(filename):
    contents = ""
    with open(filename, "r", encoding="utf8") as existing_file:
      contents = existing_file.read()

    if not os.path.exists("archives"):
      os.mkdir("archives")

    with open(f"archives/n{timestamp()}_{filename}", "w", encoding="utf8") as archived_file:
      archived_file.write(contents)

def create_checklist_file(args):
  filename = OUTPUT_FILE_NAME + ".md"

  if args.keep:
    archive_existing_checklist()

  md = ""

  with open(filename, "w", encoding="utf8") as file:
    md = render()
    file.write(md)

  if args.html:
    with open(OUTPUT_FILE_NAME + ".html", "w", encoding="utf8") as file:
      html = markdown.markdown(md)
      file.write(html)

  logger.debug("DONE")

def main(args):
  if args.verbose:
    logger.setLevel(logging.DEBUG)

  create_checklist_file(args)

if __name__ == "__main__":
  _args = get_args()
  environment = _args.environment
  main(_args)
