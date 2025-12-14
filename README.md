# File-integrity-checker

At first, i want to implement a basic version of this script, which means including core functionality:

Detect the integrity of files by comparing their hashes with those previously generated and stored in a JSON file.

Flow example:

- Read all the files in a directory
- Calculate the hash of each file
- Save the hashes in a DB (JSON or CSV)
- Later, recalculate the hashes and compare the new ones with the previously generated ones

I thought about using Python as the programming language for this script because I want to get familiar with the hashlib library.

After completing this, i can add more functionality, such as:

- Support for subdirectories 
- Detailed log of modified, removed or added files
- A GUI with options like scan, update and report
- Some input validation for the user