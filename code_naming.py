#!/usr/local/bin/python3.11

from pathlib import Path
import os, sys, re
   

# Validate the amount of command line arguments
if len(sys.argv) != 2:
   print('Please enter a command that follows this convention: code_naming.py topic_name.ext'
        '- Don\'t include whitespace at the end of the command')
   sys.exit(1)

# Database for a file's attributes based on its extension
languages = {
      '.py': ['Python', 'python.py'],
      '.html': ['HTML', 'html.html'],
      '.css': ['CSS', 'css.css'],
      '.cpp': ['CPP', 'cpp.cpp'],
      '.java': ['Java', 'java.java'],
      '.js': ['Javascript', 'javascript.js'],
      '.swift': ['iOS', 'swift.swift']
   }

# Get the file's name. Validate file's name.
target_file = sys.argv[1]

file_pattern = r'([A-Za-z\d\s]+)_([A-Za-z\d\s]+)(\.(py|html|java|cpp|css|js|swift))$'
file_validation = re.fullmatch(file_pattern, target_file)
if not file_validation:
   print('Please use a file name that conforms to the following convention: topic_name.ext\n'
         '- These are the available ext types: py, html, java, cpp, css, js, swift\n')
   sys.exit(1)

# Get the file's type (ext) and topic
file_ext = file_validation[3]
topic = file_validation[1]

# Create the path for the language folder that the file will go in
language_subdirectory = languages[file_ext][0]
language_directory = Path(f'/Users/sharellscott/Programming_Practice/{language_subdirectory}')
os.chdir(language_directory)

# Create the path for the file that contains the applicable template
template_name = languages[file_ext][1]
template_path = f'/Users/sharellscott/Documents/Side Projects/General Scripts/file mgmt script/Boilerplate Code/template_{template_name}'
template_path = Path(template_path)

# Create the path for the file
os.makedirs(topic, exist_ok=True)
target_file_path = Path(topic) / target_file

# Copy the template to the file if it doesn't exist. Otherwise, just open the file
if not target_file_path.exists():
   with open(template_path, 'r') as file:
        template = file.readlines()
    
   with open(target_file_path, 'w') as file:
      file.writelines(template)
else:
    print('This file path already exists. Opening now ...')

os.system(f'chmod +x {target_file_path} && open -a \'Visual Studio Code\' {topic}')
