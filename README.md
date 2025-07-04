# python_elves: Little helpers written in Python

This repository is meant as a loose collection of python tools for various purposes.

## lsconvert
The script takes ls -R output and turns it into a XML file. 
Sample:

    ls -R /home/my_dir > input.log
    python lsconvert.py input.log output.xml

-------- input.log -------

    /home/my_dir:
    oneFile.txt
    anotherFile.log
    someDirectory
    pink_elephant.sh
    
    /home/my_dir/someDirectory:
    someMoreFiles
    someScript.py
    someNestedDirectory
    
    /home/my_dir/someDirectory/someMoreFiles:
    very_nested_file.txt
    very_nested_program.sh
    
    /home/my_dir/someDirectory/someNestedDirectory:

-------- output.xml -------

    <home>
      <my_dir>
        <oneFile.txt />
        <anotherFile.log />
        <someDirectory>
          <someMoreFiles>
            <very_nested_file.txt />
            <very_nested_program.sh />
          </someMoreFiles>
        </someDirectory>
        <someScript.py />
        <someNestedDirectory />
      </my_dir>
    </home>

## JQL Composer
The script is used to compose complex JQL queries from a JSON-encoded dictionary of simpler sub-queries.

It will enclose the expansion of sub-queries in parentheses while expanding, in order to ensure the original precedence.

In order to use one query inside another, use the sub-query's name in brackets inside the outer query. See sample.json for an example.

Sample input:

    {
      "home": "{go_to} next {corner}",
      "go_to": "See you",
      "corner": "Saturday"
    }

Sample output:

    (See you) next (Saturday)

## How Many Do I Need?
The minecraft/hmdin script is basically a counting formatter that can help you keep track of large item quantities in Minecraft.
By default, it will print a human-readable listing of all nonzero "units of quantity" necessary to amass the specified amount of items.

You can specify a nonstandard stack size (e.g. 16 for eggs or similar) using `--stack-size`.

    python hmdin.py 256 --stack_size=16
	> 256 items are 16 stacks
	
	python hmdin.py 256
	> 255 items are 3 stacks and 63 items
	
	python hmdin.py 2000
	> 2000 items are 1 chest, 4 stacks and 16 items
	
The actual helper/split functions are:

    # will return the tuple of <chests>, <stacks>, <items>
	hmdin(count, stack_size=64, container_size=27) 
	# will format the list of items as human readable (without prefix), e.g. "3 chests and 14 items"
	pretty_print(chests, stacks, items) 
	#will format the list of all three items for CSV output, e.g. comma-separated
	csv_print(chests, stacks, items, separator=",") 