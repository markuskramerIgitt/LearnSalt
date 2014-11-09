###
### WARNING: requires c:/apps/magni directory on Windows
###
###



{% if grains['os'] == 'Windows' %}

#
# Touch this file always
#
/apps/magni/touched-by-last-salt-run:
  file.touch


#
# Touch this file only if it does not exist
#     in Salt 2014.1.11 there is no os-independant way to test if a file exists.
#     The Windows IF command can test if a file exist, but
#        unless needs 0 or 1 so IF needs the ELSE branch.
#
#
type nul > /apps/magni/touched-by-first-salt-run:
  cmd:
    - run
    - unless: 'IF EXIST /apps/magni/touched-by-first-salt-run (EXIT /B 0) ELSE EXIT /B 1'
#    -creates: /apps/magni/touched-by-first-salt-run  # requires 2014.7


{% endif %}



##############################  UNIX  ##########################
{% if grains['os'] != 'Windows' %}

#
# Touch this file always
# http://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html
#
/srv/salt/touched-by-last-salt-run:
  file.touch

#
# Touch this file only once 
# https://groups.google.com/d/msg/salt-users/Qk8Gbo6KBKM/T6eSoT2F4WAJ
# 
touch /srv/salt/touched-by-first-salt-run:
  cmd:
  - run
  - unless: 'test -e /srv/salt/touched-by-first-salt-run'



########### WARNING
#
# "Unless" only works with commands, which are OS-dependant.
# It silently ignores everything else!!!
# https://groups.google.com/forum/#!msg/salt-users/Qk8Gbo6KBKM/T6eSoT2F4WAJ
#
########### WARNING



########### WARNING
#
# file.touch   does not understand    unless
# 
# Therefore, this is illegal code and commented out:
#
#/srv/salt/touched-by-first-salt-run__filetouch:
#  file.touch
#  - unless: 'test -e /srv/salt/touched-by-first-salt-run__filetouch'
#
########### WARNING


{% endif %}



