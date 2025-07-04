import sys
import os

def read_subtree(filename):
    fileTree = {}
    with open(filename, "rb") as readFrom:
        dirPath = []
        for line in readFrom:
            shortline = line.strip()
            if len(shortline) == 0:
                pass
            elif shortline[0] == "/":
                dirPath = shortline.split("/")[1:]
                dirPath[-1] = dirPath[-1][:-1]
            else:
                dictionary = fileTree
                for directory in dirPath:
                    if directory not in dictionary.keys():
                        dictionary[directory] = {}
                    dictionary = dictionary[directory]
                dictionary[shortline] = {}
    return fileTree

def toXml(dictionary, lineIndent=""):
    text = ""
    for tag in dictionary.keys():
        if len(dictionary[tag]) > 0:
            text = text + "{indent}<{tag}>{sep}{children}{indent}</{tag}>{sep}".format(tag=tag, children=toXml(dictionary[tag], lineIndent + "  "), indent=lineIndent, sep=os.linesep)
        else:
            text = text + "{indent}<{tag} />".format(tag=tag, indent=lineIndent) + os.linesep
    return text

def print_subtree(treeDict, filename):
    with open(filename, "wb") as writeTo:
        writeTo.write(toXml(treeDict))

def format_subtree(infile, outfile):
    fileTree = read_subtree(infile)
    print_subtree(fileTree, outfile)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("usage: lsconvert infile [outfile]")
    else:
        infile = str(os.path.abspath(sys.argv[1]))
        outfile = str(os.path.dirname(os.path.abspath(sys.argv[1])))
        if len(sys.argv) == 3:
            outfile = os.path.abspath(sys.argv[2])
        print("Converting from " + infile + " to " + outfile)
        format_subtree(infile, outfile)
