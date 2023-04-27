#!/usr/local/bin/python3.11
import sys, os, argparse, datetime, logging
from datetime import datetime as dt

OUTPUT_FILE_NAME = "checklist.html"
logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("main")

def timestamp():
  return dt.strftime(dt.now(), "%Y%m%d%H%M%S")

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
    file.write(r"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Reporting Checklist</title>
  </head>
  <body>
    Hello world
  </body>
</html>
    """)

def main(args):
  if args.verbose:
    logger.setLevel(logging.DEBUG)

  create_checklist_file(args.keep)

if __name__ == "__main__":
  main(get_args())
  logger.debug("hello")
