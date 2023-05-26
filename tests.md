# Tests
The format will be: 

`command` -> 
```
Intended results
```

## Failures
**testing one command line argument**

`code_naming.py` -> 
```
Please enter a command that follows this convention: code_naming.py topic_name.ext
```

**testing more than two command line arguments**

`code_naming.py topic_name.py x`-> 
```
Please enter a command that follows this convention: code_naming.py topic_name.ext
- Don't include whitespace at the end of the command
```

**testing a file name with no extension at the end**

`code_naming.py topic_name` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

**testing a file name with an unknown extension**

`code_naming.py topic_name.zx` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

**testing a file name with a known extension + a little extra**

`code_naming.py topic_name.zx` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

**testing a file name with more than 2 parts**

`code_naming.py topic_name_me.html` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

**testing a file name with 1 part**

`code_naming.py topic.py` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

## SUCCESSES

**testing: two command line arguments, two parts of the file name**

`code_naming.py topic_name.py` ->

No output. You should see the file at <file_path>. If you open up the file, it should have the same contents as the file at <file_path>. The file should open its own window in Visual Studio Code.

**testing the correct extensions**

`code_naming.py topic_name.html` ->

No output. You should see the file at <file_path>. If you open up the file, it should have the same contents as the file at <file_path>. The file should open in its own window in Visual Studio Code.

Repeat this for the rest of the extensions.

**testing files with names that already exist**

Re-run any commands that you've already ran ->

`This file path already exists. Opening now ...`
The file should also open in its own window in Visual Studio Code.
