import argparse
import sys

def hmdin(count, stack_size=64, container_size=27):
  i = count % stack_size
  s_raw = count // stack_size
  s = s_raw % container_size
  c = s_raw // container_size
  return c, s, i

def pretty_print_kind(count, name):
  return f"{count} {name}{'' if count == 1 else 's'}"

def pretty_print(chests, stacks, items):
  components = []
  if chests > 0:
    components.append(pretty_print_kind(chests, "chest"))
  if stacks > 0:
    components.append(pretty_print_kind(stacks, "stack"))
  if items > 0 or len(components) == 0:
    components.append(pretty_print_kind(items, "item"))
  if len(components) == 1:
    return components[0]
  return ", ".join(components[:-1]) + " and " + components[-1]
  
def csv_print(chests, stacks, items, separator=","):
  return separator.join(chests, stacks, items)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("count", help="Number of items to evaluate", type=int)
  parser.add_argument("--stack_size", help="Stack size of the respective item", type=int, default=64)
  parser.add_argument("--as_csv", action="store_true")
  args = parser.parse_args()
  printer = csv_print if args.as_csv else pretty_print
  if args.count < 0:
    print(f"-{pretty_print_kind(-args.count, 'item')} {'are' if args.count != 1 else 'is'} imaginary.")
    sys.exit(1)
  print(f"{pretty_print_kind(args.count, 'item')} {'are' if args.count != 1 else 'is'} {printer(*hmdin(args.count, args.stack_size))}.")
  