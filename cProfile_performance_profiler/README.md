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
    git checkout file_replace.txt
    snakeviz file_replace.prof

snakeviz opens a browser.

Click on esxi.py and read:
- Cumulative time 69%
- File: c:\git\salt\salt\grains\

**Findings**
- Searching esxi grains on Windows takes 100% CPU for 11 seconds
- On Windows, no esxi grains should be searched.

## Remedy / Quick fix

Removed grains that are not Windows related and do not behave on Windows like zfs does by detecting Windows:

```

def __virtual__():
    '''
    Load zfs grains
    '''
    # NOTE: we always load this grain so we can properly export
    #       at least the zfs_support grain
    #       except for Windows... don't try to load this on Windows (#51703)
    if salt.utils.platform.is_windows():
        return False, 'ZFS: Not available on Windows'
    return __virtualname__

```

After these Grains removed (and clean -fxd), time is down from 15 to 7 seconds:


```
$ git status
On branch 3000.2
Your branch is up to date with 'upstream/3000.2'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    salt/grains/chronos.py
        deleted:    salt/grains/cimc.py
        deleted:    salt/grains/esxi.py
        deleted:    salt/grains/junos.py
        deleted:    salt/grains/marathon.py
        deleted:    salt/grains/mdadm.py
        deleted:    salt/grains/mdata.py
        deleted:    salt/grains/metadata.py
        deleted:    salt/grains/napalm.py
        deleted:    salt/grains/nvme.py
        deleted:    salt/grains/nxos.py
        deleted:    salt/grains/panos.py
        deleted:    salt/grains/philips_hue.py
        deleted:    salt/grains/rest_sample.py
        deleted:    salt/grains/smartos.py
        deleted:    salt/grains/ssh_sample.py

```