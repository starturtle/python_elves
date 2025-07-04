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

## How Many Do I Need?
The minecraft/hmdin script is basically a counting formatter that can help you keep track of large item quantities in Minecraft.
For the time being, it supports items that stack at 64 pieces, and expects single chests with 27 slots. 

Input: the amount of items to count. Output: `<number of chests>c, <number of additional stacks>s, <number of additional items>b`.