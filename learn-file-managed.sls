###
###  This file is stored on   /srv/salt    on the server
### 
###  Requires    c:/apps/magni    directory on Windows Minion
###
###



{% if grains['os'] == 'Windows' %}

/apps/magni/learn_file_managed_example.txt:
  file.managed:
    - source: salt://LearnSalt/learn-file-managed.txt

{% endif %}

