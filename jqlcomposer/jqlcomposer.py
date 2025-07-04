import argparse
import json
import sys

def err(msg, rv=1):
  print(msg)
  sys.exit(rv)

def cut_next(query_text):
  if query_text[0] == "{":
    length = 1
    while query_text[length] != "}":
      length += 1
    return True, query_text[1:length], query_text[length+1:]
  
  length = 1
  while length < len(query_text) and query_text[length] != "{":
    length += 1
  return False, query_text[0:length], query_text[length:] if length < len(query_text) else ""

def compose(json_struct, token):
  if token not in json_struct:
    err(f"No rule to compose {repr(token)}!")
  outcome = []
  base = json_struct[token]
  while len(base) > 0:
    translate, next, base = cut_next(base)
    # print(f"Add {'translated ' if translate else ''} {repr(next)} and continue to parse {repr(base)}")
    if translate:
      outcome.append(f"({compose(json_struct, next)})")
    else:
      outcome.append(next)
  return "".join(outcome)
  
def compose_from_file(filename, token):
  with open(filename) as f:
    return compose(json.load(f), token)

def compose_from_string(json_text, token):
  return compose(json.loads(json_text), token)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
                    prog='jqlcomposer',
                    description='Create a full JQL query from a JSON-encoded dictionary of tokens')
  parser.add_argument("token")
  parser.add_argument("input")
  parser.add_argument("--filename", action="store_true")
  settings = parser.parse_args()
  if settings.filename:
    print(compose_from_file(settings.input, settings.token))
  else:
    print(compose_from_string(settings.input, settings.token))
 
