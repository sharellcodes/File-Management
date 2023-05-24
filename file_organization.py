#!/usr/local/bin/python3.11

from pathlib import Path
import os, sys, re

"""
---- Goals ----
TEMPLATING (doing)
1. Whenever I create a new [Java, C++, HTML, CSS, Javscript, Swift, Oython] file, I want the 
   boilerplate code

ORGANIZING (not done)
1. I create a lot of practice files for specific subjects. I want the files to automatically be moved to
   the appropriate folder, no matter where I create it

---- Context ----
I constantly create files to practice various programming skills. I tend to recreate the same files, and I
also tend to add the files to folders that I forget about, with names that I forget about. This will 
help me to be intentional about my naming conventions and stay organized.
"""
   

# make sure the command line argument amount is valid
if len(sys.argv) != 2:
   print('Invalid command-line argument amount')
   sys.exit(1)
   
# goal: make sure the name fits proper conventions
file_pattern = r'([A-Za-z\d\s]+)_([A-Za-z\d\s]+)(\.(py|html|java|cpp|css|js|swift))$'
input_file = sys.argv[1]

file_validation = re.fullmatch(file_pattern, input_file)
print(file_validation[0], file_validation[1], file_validation[2], file_validation[3], file_validation[4])
print(len(sys.argv))
'''
example: pandas_testing8.py
file_validation[0] = pandas_testing8.py
file_validation[1] = pandas
file_validation[2] = testing8
file_validation[3] = .py
file_validation[4] = py
'''

if not file_validation:
   print('Please enter a file name that conforms to the following:\n'
         '- ends in .py to indicate that it\'s a python file\n'
         '- Has 2-3 parts to the name, using a _ to split up the parts of the name\n'
         '- Uses the first part of the name to specify the topic\n'
         '- Clearly specifies the type of file this is\n')
   sys.exit(1)

def name_HTML():
   html_dir = Path('/Users/sharellscott/Programming_Practice/HTML')
   os.chdir(html_dir)

   html_topic = Path(file_validation[1])
   target_file = html_topic / input_file

   os.makedirs(html_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as file:
         file.write()

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_Javascript():
   javascript_dir = Path('/Users/sharellscott/Programming_Practice/Javscript')
   os.chdir(javascript_dir)

   java_topic = Path(file_validation[1])
   target_file = java_topic / input_file

   os.makedirs(java_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as file:
         file.write()

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_CSS():
   css_dir = Path('/Users/sharellscott/Programming_Practice/CSS')
   os.chdir(css_dir)

   css_topic = Path(file_validation[1])
   target_file = css_topic / input_file

   os.makedirs(css_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as file:
         file.write()

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_Swift():
   swift_dir = Path('/Users/sharellscott/Programming_Practice/iOS')
   os.chdir(swift_dir)
   
   swift_topic = Path(file_validation[1])
   target_file = swift_topic / input_file

   os.makedirs(swift_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as file:
         file.write()

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_Java():
   java_dir = Path('/Users/sharellscott/Programming_Practice/Java')
   os.chdir(java_dir)

   java_topic = Path(file_validation[1])
   target_file = java_topic / input_file

   os.makedirs(java_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as file:
         file.write()

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_Python():
   python_dir = Path('/Users/sharellscott/Programming_Practice/Python')
   os.chdir(python_dir)

   # this is for file creation, which will make its own directory based on the file name
   python_topic = Path(file_validation[1])
   target_file = python_topic / input_file

   os.makedirs(python_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as file:
         file.write('#!/usr/local/bin/python3.11\n')
   
   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {python_topic}')

   # opens the file in an already open project
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {target_file}')

def name_CPP():
   cpp_dir = Path('/Users/sharellscott/Programming_Practice/CPP')
   os.chdir(cpp_dir)

   cpp_topic = Path(file_validation[1])
   target_file = cpp_topic / input_file

   os.makedirs(cpp_topic, exist_ok=True)

   if not target_file.exists():
      with open(target_file, 'w') as file:
         file.write()

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')


''' TESTS '''
# testing 

if __name__=='__main__':
   extensions = {
      '.py': name_Python,
      '.html': name_HTML,
      '.css': name_CSS,
      '.cpp': name_CPP,
      '.java': name_Java,
      '.js': name_Javascript,
      '.swift': name_Swift
   }

   extensions[file_validation[3]]()