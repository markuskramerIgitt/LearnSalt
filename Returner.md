On returners
====


All Salt functions return a Python dictionary, named "return data" (*ret*).

A minion sends all "return data" to the salt-master, unless the minion is setup master-less. 

The master stores all "return data" into the [default job cache](https://docs.saltstack.com/en/latest/topics/jobs/job_cache.html#default-job-cache), unless the master configuration contains `job_cache: False `


"Returners" are implemented as the 35 Python modules in salt/salt/returner/

A "returner" can be used in up to 3 distinct use cases:

## Use case 1: Minion stores "return data" ##
Named "Minion-side returner" or "external job cache"

A returner module must implement a single function: `returner(ret)`

ret is a single argument and contains the "return data" of a function executed on this minion.

[CONFUSIOIN The returner module must implement get_jid, get_fun, get_jids, get_minion?](https://docs.saltstack.com/en/latest/ref/returners/#external-job-cache-support)

All Python modules in salt/salt/returner/ implement `returner(ret)`.

The data sink may be on the minion on another host.
 


## Use case 2:  Replace the default_job_cache ##
Named "master job cache" or "master job cache support".

The returner module must implement many functions.

24 of 35 Python modules in salt/salt/returner/ implement `prep_jid()`.

[See Documentation](https://docs.saltstack.com/en/latest/ref/returners/#master-job-cache-support) 




## Use case 3: Salt-master stores "return data" ##
Named "Event returner".

The returner module must implement a single function: `event_return(events)`

Note that this is a list of return data, called events.

Example event returner: rawfile_json.py

To enable, you must configure the master with the `event_return` property.

A File  matching /etc/salt/master.d/*.conf must contain the line

    event_return: rawfile_json

And usefully

    event_return_blacklist:
      - salt/auth


You must have restarted the salt-master since then

  `service salt-master restart`

After you execute a command,
  `salt bob test.version`
You find the event data in file `/var/log/salt/events`

12 of 35 Python modules in salt/salt/returner/ implement ` event_return(events)`. Redis not.

 [This Documentation ]( https://docs.saltstack.com/en/latest/topics/jobs/external_cache.html) does not  mention  "Event returner".
 
Warning: Setting `master_job_cache: rawfile_json` results in an error. (Why?)

Live-editing /usr/lib/python2.7/dist-packages/salt/returners/rawfile_json.py


[See Documentation ]( https://docs.saltstack.com/en/latest/ref/returners/#event-returners)


