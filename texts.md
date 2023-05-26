# Tests
The format will be `command` -> 
```
Intended results
```

## Failures
### testing one command line argument
`code_naming.py` -> 
```
Please enter a command that follows this convention: code_naming.py topic_name.ext
```

### testing more than two command line arguments
`code_naming.py topic_name.py x`-> 
```
Please enter a command that follows this convention: code_naming.py topic_name.ext
- Don't include whitespace at the end of the command
```

### testing a file name with no extension at the end
`code_naming.py topic_name` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

### testing a file name with an unknown extension
`code_naming.py topic_name.zx` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

### testing a file name with a known extension + a little extra
`code_naming.py topic_name.zx` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

### testing a file name with more than 2 parts
`code_naming.py topic_name_me.html` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

### testing a file name with 1 part
`code_naming.py topic.py` ->
```
Please use a file name that conforms to the following convention: topic_name.ext
- These are the available ext types: py, html, java, cpp, css, js, swift
```

## SUCCESSES
- testing two command line arguments
- testing two parts of the file name
- testing the correct extensions
- testing files with names that already exist
- testing files with directories that already exist
- check the contents of the files and make sure it has the correct templates
