# python_elves
Little helpers written in Python

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