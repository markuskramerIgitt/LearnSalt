## Install minion from Git

    git clone salt
    git checkout 3000.2
    ./build_env.ps1 

if hangs run again new powershell

    pip install -e .

new powershell

    salt-call --local test.ping

## On install salt-master on UNIX 

### Leave file `/etc/salt/master` unchanged

Instead, use `/etc/salt/master.d/*.conf` files. A Salt version upgrade can only automatically update an unchanged /etc/salt/master file. Think of this file as part of the Salt documentation under version control of SaltStack Inc.

