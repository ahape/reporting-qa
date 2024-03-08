#!/usr/local/bin/python3.11
import os, argparse, logging, yaml, random, markdown
from datetime import datetime as dt

OUTPUT_FILE_NAME = "README"
TEST_DIR = "tests"
ARCHIVE_DIR = "archives"
TEST_TEMPLATE = r"""
{name}
{underline}
* [(link to test)]({link})
{steps}
"""
TEST_GROUP_TEMPLATE = r"""
{name}
{underline}
{tests}
"""
environment = logger = None

class TestGroup:
  def __init__(self, name):
    self.name = (name.replace("_", " ") + " tests").upper()
    self.tests = []

class Test:
  def __init__(self, name, **kwargs):
    self.name = name.replace(".yaml", "").replace("_", " ").title()
    self.link = create_link(kwargs["link"])
    self.steps = ["* " + bullet for bullet in kwargs["desc"]]

def create_link(link):
  def set_env(_link):
    if environment in { "beta", "testing" }:
      return _link.replace("webapp", environment)
    if environment == "localhost":
      return _link.replace("https://webapp.brightmetrics.com/", "http://localhost:8080/")
    return _link

  def set_cache_bust(_link):
    """
    Makes it so that <a> link appears in the non-`:visited` CSS styling, as
    well as adds context to web session via address bar
    """
    key = ("?" if "?" not in _link else "&") + "_qa"
    val = f"{timestamp()}_{random.randint(0,999_999)}"
    splice_at = _link.rindex("#") if "#" in _link else len(_link)
    return _link[:splice_at] + f"{key}={val}" + _link[splice_at:]

  return set_cache_bust(set_env(link))

def load_yaml(path):
  with open(path, "r", encoding="utf8") as stream:
    try:
      return yaml.safe_load(stream)
    except yaml.YAMLError as ex:
      logger.error("%s", ex)
  return None

def load_tests():
  groups = []
  for group_name in os.listdir(TEST_DIR):
    if group_name:
      group = TestGroup(group_name)
      fullpath = f"{TEST_DIR}/{group_name}"
      for test_name in filter(lambda x: x.endswith(".yaml"), os.listdir(fullpath)):
        abspath = f"{fullpath}/{test_name}"
        logger.debug("Loading test file %s", abspath)
        if (json := load_yaml(abspath)):
          group.tests.append(Test(test_name, **json))
      if group.tests:
        group.tests.sort(key=lambda t: t.name)
        groups.append(group)
  return groups

def timestamp():
  return dt.strftime(dt.now(), "%Y%m%d%H%M%S")

def render():
  def underline(title, bar):
    return "".zfill(len(title)).replace("0", bar)

  def render_tests(tests):
    rendered = []
    for t in tests:
      rendered.append(
        TEST_TEMPLATE.format(
          name=t.name,
          link=t.link,
          underline=underline(t.name, "-"),
          steps="\n".join(t.steps)))
    return "".join(rendered)

  def render_test_group(test_group):
    return TEST_GROUP_TEMPLATE.format(
      name=test_group.name,
      underline=underline(test_group.name, "="),
      tests=render_tests(test_group.tests))

  def _render(test_groups):
    return "".join([render_test_group(tg) for tg in test_groups])

  return _render(load_tests())

def get_args():
  args = argparse.ArgumentParser()
  args.add_argument("-k", "--keep", action="store_true", help="Archive the last checklist")
  args.add_argument("-v", "--verbose", action="store_true")
  args.add_argument("-e", "--environment", help="localhost | beta | testing | webapp (default)")
  args.add_argument("--html", action="store_true")
  return args.parse_args()

def create_logger(args):
  logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s")
  _logger = logging.getLogger("main")
  if args.verbose:
    _logger.setLevel(logging.DEBUG)
  return _logger

def archive_existing_checklist():
  filename = OUTPUT_FILE_NAME + ".md"
  if os.path.exists(filename):
    contents = ""
    with open(filename, "r", encoding="utf8") as existing_file:
      contents = existing_file.read()
    if not os.path.exists(ARCHIVE_DIR):
      os.mkdir(ARCHIVE_DIR)
    with open(f"{ARCHIVE_DIR}/t{timestamp()}_{filename}", "w", encoding="utf8") as archived_file:
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
      html = "<style>body { margin: 3em 2em 5em; font-family: system-ui; }</style>"
      html += markdown.markdown(md)
      file.write(html)
  logger.debug("DONE")

def main(args):
  create_checklist_file(args)

if __name__ == "__main__":
  _args = get_args()
  environment = _args.environment
  logger = create_logger(_args)
  main(_args)
