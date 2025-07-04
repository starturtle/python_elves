import jqlcomposer.jqlcomposer
import subprocess
import filecmp

TEST_TERMS=["summer"]

def test_jqlcomposer_main_asfile():
  for i in xrange(len(TEST_TERMS)):
    idx = i+1
    with open(f"testout{idx}.txt", "w") as outfile:
      subprocess.run(["python", "jqlcomposer.py", TEST_TERMS[i], "--filename", f"test{idx}.json"], stdout=outfile)
    assert 0 == filecmp.cmp(f"testout{idx}.txt", f"expect{idx}.txt")
  
def test_jqlcomposer_main_astext():
  for i in xrange(len(TEST_TERMS)):
    idx = i+1
    json_contents = ""
    with open(f"test{idx}.json", "r") as infile:
      json_contents = infile.read()
    with open(f"testout{idx}.txt", "w") as outfile:
      subprocess.run(["python", "jqlcomposer.py", TEST_TERMS[i], f'"{json_contents}"'], stdout=outfile)
    assert 0 == filecmp.cmp(f"testout{idx}.txt", f"expect{idx}.txt")
  
