zmq_filtering



Salt uses zeromq's pub/sub sockets. 
By default, all publish jobs are sent to all minions and filtered minion side. 
Zeromq does have publisher side filtering which can be enabled in salt using zmq_filtering.

To use zmq_filtering:

Minion step 1) 

On a minion,  create file `c:\salt\conf\minion.d\zmq_filtering.conf` with a single line of content:

    zmq_filtering: True

Minion step 2)

Restart the salt-minion service



Master step 1) 

Add line to file  /etc/salt/master.d/master.conf

    zmq_filtering: True


The Master can reach A-minion-without-zmq_filtering only by broadcast








