import argparse

def hmdin(count):
  BPS = 64
  SPC = 27
  b = count % BPS
  s_raw = count // BPS
  s = s_raw % SPC
  c = s_raw // SPC
  return c, s, b

def pretty_print(chests, stacks, blocks):
  components = []
  if chests > 0:
    components.append(f"{chests} chests")
  if stacks > 0:
    components.append(f"{stacks} stacks")
  if blocks > 0 or len(components) == 0:
    components.append(f"{blocks} blocks")
  if len(components) == 1:
    return components[0]
  return ", ".join(components[:-1]) + " and " + components[-1]
  
def csv_print(chests, stacks, blocks, separator=","):
  return separator.join(chests, stacks, blocks)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-count", help="Number of blocks to pretty-print", type=int)
  args = parser.parse_args()
  print(f"{args.count} blocks are {pretty_print(*hmdin(args.count))}.")
  