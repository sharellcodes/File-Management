# File-Management

### Context
I constantly create files to practice various programming skills for various languages. I tend to recreate the same files, and I
also tend to add the files to folders that I forget about, with names that I forget about. This will 
help me to be intentional about my naming conventions and stay organized.

### Purpose
1. Whenever I create a new [Java, C++, HTML, CSS, Javscript, Swift, Python] file, I want the 
   boilerplate code automatically added.
2. I create a lot of practice files for specific subjects. I want the files to automatically be created in the appropriate folder when it's created.

### Algorithm for code_naming.py
1. Get the file’s name from the command line arguments. It will be referred to as `target_file` from now on.
2. Use `target_file`’s extension to find the applicable practice folder and template (boilerplate code) file path.
3. Change the current directory to the applicable practice folder.
4. Use `target_file`’s topic name to create a new folder of the same name.
5. If `target_file` doesn’t exist under `/topic`, copy the template file’s content to it.
6. Open up the file in the desired IDE.

### Notes
- I would like to create automated tests for this at some point, but for now I just provided the types of testing commands that can be ran in [code_naming_tests.md](https://github.com/sharellcodes/File-Organization/blob/main/tests.md).
- If you download this to use
   - at lines 40, 45 & 62 - replace 'xxx' with your own file path and IDE (I used Visual Studio Code).
   - Be sure to create the necessary language folders (Python, HTML, etc. under whichever file path you choose)
   - Note that I set up my local environment to be able to run the commands in any directory
