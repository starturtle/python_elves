import subprocess
import filecmp
import jqlcomposer
import contextlib

TEST_TERMS=["summer"]

def test_jqlcomposer_main_asfile():
  for i in range(len(TEST_TERMS)):
    idx = i+1
    with open(f"tests/testout{idx}.txt", "w") as outfile:
      subprocess.run(["python", "src/jqlcomposer.py", TEST_TERMS[i], "--filename", f"tests/test{idx}.json"], stdout=outfile)
    assert 0 == filecmp.cmp(f"tests/testout{idx}.txt", f"tests/expect{idx}.txt")
  
def test_jqlcomposer_main_astext():
  for i in range(len(TEST_TERMS)):
    idx = i+1
    json_contents = ""
    with open(f"tests/test{idx}.json", "r") as infile:
      json_contents = infile.read()
    with open(f"tests/testout{idx}.txt", "w") as outfile:
      subprocess.run(["python", "src/jqlcomposer.py", TEST_TERMS[i], f'"{json_contents}"'], stdout=outfile)
    assert 0 == filecmp.cmp(f"tests/testout{idx}.txt", f"tests/expect{idx}.txt")
  
def test_jqlcomposer_compose_from_file():
  for i in range(len(TEST_TERMS)):
    idx = i+1
    with open(f"tests/testout{idx}.txt", "w") as outfile:
      with contextlib.redirect_stdout(outfile):
        jqlcomposer.create_from_file(f"tests/test{idx}.json", TEST_TERMS[i])
    assert 0 == filecmp.cmp(f"tests/testout{idx}.txt", f"tests/expect{idx}.txt")
  
def test_jqlcomposer_compose_from_string():
  for i in range(len(TEST_TERMS)):
    idx = i+1
    json_contents = ""
    with open(f"tests/test{idx}.json", "r") as infile:
      json_contents = infile.read()
    with open(f"tests/testout{idx}.txt", "w") as outfile:
      with contextlib.redirect_stdout(outfile):
        jqlcomposer.create_from_string(json_contents, TEST_TERMS[i])
    assert 0 == filecmp.cmp(f"tests/testout{idx}.txt", f"tests/expect{idx}.txt")

def test_cut_next():
  is_token, next_slice, remainder = jqlcomposer.cut_next("if in {doubt}, flail about")
  assert not is_token
  assert next_slice == "if in "
  assert remainder == "{doubt}, flail about"
  is_token, next_slice, remainder = jqlcomposer.cut_next("{doubt} leads to hostility")
  assert is_token
  assert next_slice == "doubt"
  assert remainder == " leads to hostility"
  is_token, next_slice, remainder = jqlcomposer.cut_next("nothing to cut here")
  assert not is_token
  assert next_slice == "nothing to cut here"
  assert remainder == ""
  