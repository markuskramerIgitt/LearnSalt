Space to assemble documentation pull requests.




## Advise for non UNIX experts

### Leave file `/etc/salt/master` unchanged

Instead, use `/etc/salt/master.d/*.conf` files. A Salt version upgrade can only automatically update an unchanged/etc/salt/master file. Think of this file as part of the documentation under version control of the vendor.

