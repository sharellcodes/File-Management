#!/usr/local/bin/python3.11

from pathlib import Path
import os, sys, re

"""
---- Goals ----
TEMPLATING
1. Whenever I create a python file anywhere on the computer, I want the hashbang comment in it (done)
2. Whenever I create a new [Java, C++, HTML, etc] file, I want the foundation syntax in it (not done)

ORGANIZING (not done)
1. I create a lot of practice files for specific subjects. I want the files to automatically be moved to
   the appropriate folder, no matter where I create it

---- Context ----
I constantly create files to practice various programming skills. I tend to recreate the same files, and I
also tend to add the files to folders that I forget about, with names that I forget about. This will 
encourage me to be intentional about my naming conventions and stay organized.
"""

python_dir = Path('/Users/sharellscott/Programming_Practice/Python')
os.chdir(python_dir)

print('- If you\'re specifying the directory and it doesn\'t match the py_topic,'
      ' please continue to specify that directory if you go to open the file \n')
   

# goal: make sure the command line argument amount is valid
if 3 < len(sys.argv) < 2:
   print('Invalid command-line argument amount')
   sys.exit(1)
   
# goal: make sure it's a python file
file_pattern = r'([A-Za-z\d\s]+)_([A-Za-z\d\s]+)(_[A-Za-z\d\s]+)?(\.py)$'
input_file = sys.argv[1]

py_validation = re.fullmatch(file_pattern, input_file)
# print(py_validation[0], py_validation[1])

if not py_validation:
   print('Please enter a file name that conforms to the following:\n'
         '- ends in .py to indicate that it\'s a python file\n'
         '- Has 2-3 parts to the name, using a _ to split up the parts of the name\n'
         '- Uses the first part of the name to specify the topic\n'
         '- Clearly specifies the type of file this is\n')
   sys.exit(1)

# this is for file creation, which will make its own directory based on the file name
if len(sys.argv) == 2:
   python_topic = Path(py_validation[1])
   target_file = python_topic / input_file

   os.makedirs(python_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as test:
         test.write('#!/usr/local/bin/python3.11\n')
   
   # opens the file in its own window
   os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {python_topic}')

   # opens the file in an already open project
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {target_file}')
# this is for direct directory creation. For people that want to specify the directory of a file
else:
   input_dir = Path(sys.argv[2])
   # os.makedirs(python_dir / input_dir, exist_ok=True)
   os.makedirs(input_dir, exist_ok=True)

   # target_file = python_dir / input_dir / input_file
   target_file = input_dir / input_file

   if not target_file.exists():
      with open(target_file, 'w') as test:
         test.write('#!/usr/local/bin/python3.11\n')
   
   # opens the file in its own window
   os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {input_dir}')

   # opens the file in an already open project
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {target_file}')


''' TESTS '''
# testing 