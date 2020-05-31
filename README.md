## Install minion from Git


new vm

new admin powershell

    git clone salt
    git checkout 3000.2
    cd .\pkg\windows\
    .\build_env.ps1 

if it hangs run again 

new admin powershell

    pip install -e .

new admin powershell

    salt-call --local test.version

## On install salt-master on UNIX 

### Leave file `/etc/salt/master` unchanged

Instead, use `/etc/salt/master.d/*.conf` files. A Salt version upgrade can only automatically update an unchanged /etc/salt/master file. Think of this file as part of the Salt documentation under version control of SaltStack Inc.

