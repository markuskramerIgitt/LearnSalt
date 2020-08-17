
## Install minion 3000.2 from Git

Open a new admin powershell console

Go to your salt git repo

Checkout the tag 

    git checkout v3000.2

Verify `HEAD detached at v3000.2`
 
    git status
    
Remove cache (__pycache__)  from previous build
    
    git clean -fxd

Run .\build_env_3.ps1 once or twice
- It may hangs on "Successfully installed CherryPy-17.4.1 ... zc.lockfile-2.0"
- "Installing visualcppbuildtools_full.exe" takes several 2 minutes 

    Set-ExecutionPolicy RemoteSigned
    cd .\pkg\windows\
    .\build_env_3.ps1

Open a new admin powershell console!

Install salt (don't overlook the dot)

    cd c:\git\salt
    pip install -e .
    
Open a new admin powershell console!

Do a smoke test

    cd c:\git\salt
    salt-call --local test.version
    
    
END OF  Install minion 3000.2 from Git
    
    

## On install salt-master on UNIX 

### Leave file `/etc/salt/master` unchanged

Instead, use `/etc/salt/master.d/*.conf` files. A Salt version upgrade can only automatically update an unchanged /etc/salt/master file. Think of this file as part of the Salt documentation under version control of SaltStack Inc.

