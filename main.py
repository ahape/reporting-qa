#!/usr/local/bin/python3.11
import sys, os, argparse, datetime, logging, yaml, uuid
from datetime import datetime as dt

OUTPUT_FILE_NAME = "checklist.html"
logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("main")

def create_link(link):
  bust = "?" if "?" not in link else "&"
  bust += "_qa=" + timestamp()
  splice = link.rindex("#") if "#" in link else len(link)
  return link[:splice] + bust + link[splice:]

def load_yaml():
  tests = []

  with open("tests.yaml", "r", encoding="utf8") as stream:
    try:
      tests = yaml.safe_load(stream)
    except yaml.YAMLError as ex:
      logger.error("%s", ex)

  return [Test(**t) for t in tests]

class Test:
  def __init__(self, **kwargs):
    self.id = uuid.uuid4()
    self.link = create_link(kwargs["link"])
    self.desc = kwargs["desc"]
    self.criteria = kwargs["criteria"]
    self.suite = kwargs["suite"]

  def __repr__(self):
    return f"""
id: {self.id}
link: {self.link}
desc: {self.desc}
criteria: {self.criteria}
suite: {self.suite}
    """

test_row_template = r"""
<tr>
  <td><input type="checkbox" disabled="disabled" id="{id}" /></td>
  <td class="fixed">
    <a href="{link}"
       target="_blank"
       onclick="x=document.getElementById('{id}');x.checked=true;x.disabled=false">
       report
     </a>
  </td>
  <td class="fixed">
    {criteria}
  </td>
  <td>
    <pre>{desc}</pre>
  </td>
</tr>
"""

test_table_template = r"""
<table>
  <caption>
    <h2>{title}</h2>
  </caption>
  <tbody>
    {rows}
  </tbody>
</table>
"""

checklist_template = r"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Reporting Checklist</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Reporting QA Checklist</h1>
    {tests}
  </body>
</html>
"""

def timestamp():
  return dt.strftime(dt.now(), "%Y%m%d%H%M%S")

def render():
  return checklist_template.format(
      tests="".join([
        test_table_template.format(
          title="Report Field Editor Tests",
          rows="".join([
            test_row_template.format(
              id=t.id,
              link=t.link,
              desc=t.desc,
              criteria=t.criteria,
              suite=t.suite) for t in load_yaml()
            ]))
          ]))

def get_args():
  args = argparse.ArgumentParser()
  args.add_argument("-k", "--keep", action="store_true")
  args.add_argument("-v", "--verbose", action="store_true")
  return args.parse_args()

def archive_existing_checklist():
  if os.path.exists(OUTPUT_FILE_NAME):
    contents = ""
    with open(OUTPUT_FILE_NAME, "r", encoding="utf8") as existing_file:
      contents = existing_file.read()

    if not os.path.exists("archives"):
      os.mkdir("archives")

    with open(f"archives/n{timestamp()}_{OUTPUT_FILE_NAME}", "w", encoding="utf8") as archived_file:
      archived_file.write(contents)

def create_checklist_file(keep):
  if keep:
    archive_existing_checklist()

  with open(OUTPUT_FILE_NAME, "w", encoding="utf8") as file:
    file.write(render())
    logger.debug("DONE")

def main(args):
  if args.verbose:
    logger.setLevel(logging.DEBUG)

  create_checklist_file(args.keep)

if __name__ == "__main__":
  main(get_args())
