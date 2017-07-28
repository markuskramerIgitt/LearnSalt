zmq_filtering



Salt uses zeromq's pub/sub sockets. 
By default, all publish jobs are sent to all minions and filtered minion side. 
Zeromq does have publisher side filtering which can be enabled in salt using zmq_filtering.

To use zmq_filtering:

Step 1) 
On a minion,  create file `c:\salt\conf\minion.d\zmq_filtering.conf` with a single line of content:

    zmq_filtering: True

Step 2)
Restart the salt-minion service



2) On the master, add line to file  /etc/salt/master.d/master.conf

    zmq_filtering: True


If a minion has not enabled zmq_filtering, but the master has, then the Salt-Master cannot contact the minion.








