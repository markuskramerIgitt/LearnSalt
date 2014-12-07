###
###  This file is stored on   /srv/salt    on the server
### 
###  Requires    c:/apps/magni    directory on Windows
###
###



{% if grains['os'] == 'Windows' %}

/apps/magni/file_managed_example.txt:
  file.managed
   - source: salt://

{% endif %}

