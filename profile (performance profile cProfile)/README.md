## Profiling   100% CPU for 11 seconds

CLI

    salt-call --local file.replace /git/LearnSalt/file_replace.txt pattern="foo" repl="bar" backup=False

Profile

    pip install snakeviz
    file_replace_profile.bat
    snakeviz file_replace.prof

Click on esxi.py:
- Cumulative time 69%
- File: c:\git\salt\salt\grains\

Assumption:
- Finding esxi grains on Windows takes  100% CPU for 11 seconds

