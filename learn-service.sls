###
###  This file is stored under   /srv/salt    on the server
### 
###  Requires    c:/apps/magni    directory on Windows Minion
###
###  Learn salt:// is relative to top.sls
### 
### 



{% if grains['os'] == 'Windows' %}

deluged:
  service:
    - running

{% endif %}

