## Install minion 3000.2 from Git


new vm

new admin powershell

    git clone salt
    git checkout 3000.2

    Set-ExecutionPolicy RemoteSigned
    Set-MpPreference -DisableRealtimeMonitoring $true
    cd .\pkg\windows\
    .\build_env_3.ps1
    Set-MpPreference -DisableRealtimeMonitoring $false

run .\build_env_3.ps1 twice:
- it hangs on "Successfully installed CherryPy-17.4.1 ... zc.lockfile-2.0"

ignore:
- You are using pip version 9.0.1, however version 20.1.1 is available.

new admin powershell

    pip install -e .
    

new admin powershell

    salt-call --local test.version

## On install salt-master on UNIX 

### Leave file `/etc/salt/master` unchanged

Instead, use `/etc/salt/master.d/*.conf` files. A Salt version upgrade can only automatically update an unchanged /etc/salt/master file. Think of this file as part of the Salt documentation under version control of SaltStack Inc.

