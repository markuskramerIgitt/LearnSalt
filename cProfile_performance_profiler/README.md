## Profiling   file.replace 

Replacing foo with bar in a text files of 5 lines takes 100% CPU for 11-13 seconds.
This is a candidate for profiling.

**Command on CLI**

    salt-call --local file.replace /git/LearnSalt/cProfile_performance_profiler/file_replace.txt pattern="foo" repl="bar" backup=False

**Profile on CLI**

    python -m cProfile -o file_replace.prof /Python35/Scripts/salt-call --local file.replace /git/LearnSalt/cProfile_performance_profiler/file_replace.txt pattern="foo" repl="bar" backup=False

**Step by step instructions**

[Install minion 3000.2 from Git](https://github.com/markuskramerIgitt/LearnSalt)

    pip install snakeviz
    file_replace_profile.bat
    snakeviz file_replace.prof

snakeviz opens a browser.

Click on esxi.py and read:
- Cumulative time 69%
- File: c:\git\salt\salt\grains\

**First assumptions**
- Searching esxi grains on Windows takes 100% CPU for 11 seconds
- On Windows, no esxi grains should be searched.
