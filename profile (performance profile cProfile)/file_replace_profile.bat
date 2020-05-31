python -m cProfile -o file_replace.prof /Python35/Scripts/salt-call --local file.replace /git/LearnSalt/file_replace.txt pattern="foo" repl="bar" backup=False
