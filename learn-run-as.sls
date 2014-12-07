
{% if grains['os'] == 'Windows' %}

#
# Write the name and home share of the user/identity that runs the salt-minion locally
# It turns out that it is SYSTEM (NT Authority\Local System) C:\Windows\System32\config\systemprofile
#
whoAmI-echo:
  cmd.run:
    - name: "echo %USERNAME% %USERPROFILE%"

whoAmI-whoami:
  cmd.run:
    - name: "whoami /USER"


#
# This state fails
# So it is commented out.
#
# Salt 2014.1.11 cannot change the user
# The error message is  "Sorry, Windows does not support runas functionality"
# Literally, this message is wrong.
# 
# Issue opened 2 October 2014  https://github.com/saltstack/salt/issues/16340
# 
#
#whoAmI-change-user:
#  cmd.run:
#    - user: markus
#    - name: "echo %USERNAME% %USERPROFILE%"



#
# Procedure to run a NON-INTERACTIVE command as a different user.
# This is a silly workaround  
#
# ISSUE cmd.run runas not implemented on Windows #16340
#       https://github.com/saltstack/salt/issues/16340


#delete file if present
huhu1:
  file.absent:
    - name: /apps/magni/learn-run-as.bat

# create file
#/apps/magni/learn-run-as.bat:
#  file.touch

#write to file
huhu2:
  file.managed:
    - name: /apps/magni/learn-run-as.bat
    - contents: 'whoami > /apps/magni/learn-run-as.txt'
    # also / in Windows

learn-run-as-1-of-3:
  cmd.run:
    # /RU Run user -- WARNING: you must escape the backslash between domain and username
    # /RP password
    # /TR task 
    # /SC run once
    # /SD and /ST some date in the far future to prevent a warning or a run
    - name: "SCHTASKS /create /RU MBOX\\markus /RP m /tn saltsch /tr c:/apps/magni/learn-run-as.bat /SC ONCE /SD 01.01.2500 /ST 12:00"

learn-run-as-2-of-3:
  cmd.run:
    # actually run
    - name: "SCHTASKS /run /tn saltsch"

learn-run-as-3-of-3:
  cmd.run:
    # remove the scheduled task
    - name: "SCHTASKS /delete /tn saltsch /F"


{% endif %}



##############################  UNIX  ##########################
{% if grains['os'] != 'Windows' %}


whoAmI-whoami:
  cmd.run:
    - name: "whoami"


whoAmI-echo:
  cmd.run:
    - name: "echo $USER"

whoAmI-change-user:
  cmd.run:
    - user: markus
    - name: "echo $USER"


{% endif %}



