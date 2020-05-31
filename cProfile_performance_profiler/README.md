## Profiling   100% CPU for 11 seconds


Replacing foo with bar in a text files of 5 lines should take milliseconds.
Why does Salt 3000.2 takes 11 seconds?

Command on CLI

    salt-call --local file.replace /git/LearnSalt/file_replace.txt pattern="foo" repl="bar" backup=False

How to profile?

    pip install snakeviz
    file_replace_profile.bat
    snakeviz file_replace.prof

Click on esxi.py:
- Cumulative time 69%
- File: c:\git\salt\salt\grains\

Assumption:
- Searching esxi grains on Windows takes  100% CPU for 11 seconds
- On Windows, no esxi grains should be searched.
