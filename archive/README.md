Learn Salt
====

On Windows, how do I tell that the salt-minion is running?
 - Look for a service called salt-minion
 - Look for a process called salt-minion.exe run by SYSTEM

On Windows, why there is no command "salt"?
 - salt is a command only on the server
 - see salt-call

On Windows, why `salt-call` is not found?
 - c:\salt is not in the PATH

On the Server emacs /etc/salt/master.d/markus_saltmaster.conf

```
# Make the eventbus more silent
# https://github.com/saltstack/salt/pull/45358
auth_events: False
minion_data_cache_events: False

# Make the log more silent
log_level: error
log_level_logfile: info

```
emacs /etc/salt/master.d/reactor.conf

```

#
# After editing: systemctl restart salt-master

reactor:
  - 'salt/minion/*/start':
    # - /srv/salt/minion_schedule_heartbeat_state.sls   // DONT: MUST BE A RENDER REACTION
    - /srv/salt/reactor/minion_start_reactor.sls


```
emacs /srv/salt/reactor/minion_start_reactor.sls

```
minion_start_reaction:
  local.state.sls:
    - tgt: {{ data.id }}
    - arg: 
      - minion_schedule_heartbeat_state


```


emacs /srv/salt/minion_schedule_heartbeat_state.sls

```
    

```
  
