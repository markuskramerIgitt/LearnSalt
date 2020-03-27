## Configuration for Salt at Scale

### ZMQ configuration

Salt uses ZMQ for comminication.

The default settings includes `zmq_filtering: False`

Current documentation on that setting is poor: 
- https://docs.saltstack.com/en/latest/topics/transports/zeromq.html

> The pub channel is implemented using zeromq's pub/sub sockets. By default we don't use zeromq's filtering, which means that all publish jobs are sent to all minions and filtered minion side. Zeromq does have publisher side filtering which can be enabled in salt using zmq_filtering.

Warning: the setting **must** be changed on the master and (all) minions: if settings differ between master and minion they cannot communicate at all.

Why not True by default:
- [Earlier? it limited which different targeting methods can be used](https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/salt-users/Uaz8k6alFaU/Cp12ZaCEDwAJ)
- [Now? Allows publisher side minion match for use with zmq_filtering](https://github.com/saltstack/salt/pull/30518)

Explanation with 10,000 minions on a bad network, you want to send a job to 20 of them.

With "minion side filtering" (`zmq_filtering: False`) :
- The job is send to 10,000 minions (over a bad network).
- The 20 minions are filtering the job and respond.
- 19,980 minion are filtering the job and discard the job. 

With "master side filtering" (`zmq_filtering: True`) on the master and **all** minions:
- The job is (only) send to 20 minions (over a bad network)
- The 20 minions respond to the job.
- 19,980 minion will be unaware of the job, because they do not receive it.

### Master configuration

When the job is sent to a single minion by runner, you should/must 
- Protect bandwidth: set `zmq_filter: True` in all masters and minions
- Protect master load: set `skip_grains: True` in all masters. [Read on](https://github.com/saltstack/salt/pull/53603/files)

