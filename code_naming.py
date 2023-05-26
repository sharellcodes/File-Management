#!/usr/local/bin/python3.11

from pathlib import Path
import os, sys, re
   

# make sure the command line argument amount is valid
if len(sys.argv) != 2:
   print('Invalid command-line argument amount')
   sys.exit(1)
   
# goal: make sure the name fits proper conventions
file_pattern = r'([A-Za-z\d\s]+)_([A-Za-z\d\s]+)(\.(py|html|java|cpp|css|js|swift))$'
input_file = sys.argv[1]

file_validation = re.fullmatch(file_pattern, input_file)

if not file_validation:
   print('Please enter a file name that conforms to the following:\n'
         '- ends in .py, .html, .css, .js, .java, .swift or .cpp\n'
         '- Has 2 parts to the name, using a _ to split up the parts of the name\n'
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
      with open('/Users/sharellscott/Documents/Side Projects/General Scripts/template_html.html', 'r') as file:
         template = file.readlines()
      
      with open(target_file, 'w') as file:
         for line in template:
            file.write(line)

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_Javascript():
   javascript_dir = Path('/Users/sharellscott/Programming_Practice/Javscript')
   os.chdir(javascript_dir)

   java_topic = Path(file_validation[1])
   target_file = java_topic / input_file

   os.makedirs(java_topic, exist_ok=True)

   if not target_file.exists():
      with open('/Users/sharellscott/Documents/Side Projects/General Scripts/template_javascript.js', 'r') as file:
         template = file.readlines()
      
      with open(target_file, 'w') as file:
         for line in template:
            file.write(line)

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_CSS():
   css_dir = Path('/Users/sharellscott/Programming_Practice/CSS')
   os.chdir(css_dir)

   css_topic = Path(file_validation[1])
   target_file = css_topic / input_file

   os.makedirs(css_topic, exist_ok=True)

   if not target_file.exists():
      with open('/Users/sharellscott/Documents/Side Projects/General Scripts/template_css.css', 'r') as file:
         template = file.readlines()
      
      with open(target_file, 'w') as file:
         for line in template:
            file.write(line)

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_Swift():
   swift_dir = Path('/Users/sharellscott/Programming_Practice/iOS')
   os.chdir(swift_dir)
   
   swift_topic = Path(file_validation[1])
   target_file = swift_topic / input_file

   os.makedirs(swift_topic, exist_ok=True)

   if not target_file.exists():
      with open('/Users/sharellscott/Documents/Side Projects/General Scripts/template_swift.swift', 'r') as file:
         template = file.readlines()
      
      with open(target_file, 'w') as file:
         for line in template:
            file.write(line)

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')

def name_Java():
   java_dir = Path('/Users/sharellscott/Programming_Practice/Java')
   os.chdir(java_dir)

   java_topic = Path(file_validation[1])
   target_file = java_topic / input_file

   os.makedirs(java_topic, exist_ok=True)

   if not target_file.exists():
      with open('/Users/sharellscott/Documents/Side Projects/General Scripts/template_java.java', 'r') as file:
         template = file.readlines()
      
      with open(target_file, 'w') as file:
         for line in template:
            file.write(line)

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
      with open('/Users/sharellscott/Documents/Side Projects/General Scripts/template_python.py', 'r') as file:
         template = file.readlines()
      
      with open(target_file, 'w') as file:
         for line in template:
            file.write(line)
   
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
      with open('/Users/sharellscott/Documents/Side Projects/General Scripts/template_cpp.cpp', 'r') as file:
         template = file.readlines()
      
      with open(target_file, 'w') as file:
         for line in template:
            file.write(line)

   # opens the file in its own window
   # os.system(f'chmod +x {target_file} && open -a \'Visual Studio Code\' {cpp_topic}')


''' 
TESTS 
---- Failures ----
- testing one command line argument
- testing more than two command line arguments
- testing a file name with no extension at the end
- testing a file name with an unknown extension
- testing a file name with an extension + a little extra
- testing a file name with more than 2 parts
- testing a file name with 1 part 

---- SUCCESSES ----
- testing two command line arguments
- testing two parts of the file name
- testing the correct extensions
- testing files with names that already exist
- testing files with directories that already exist
- check the contents of the files and make sure it has the correct templates
'''

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
