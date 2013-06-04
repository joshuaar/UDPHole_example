UDPHole_example
===============

Simple example of UDP hole punching in python.

##Usage
This has a 'client' and a 'server'. They each need to know the other's IP address and port to connect on. These are
hardcoded in the clientAddr and serverAddr variables in client.py and server.py respectively. 
Then they exchange some data, and that's it. 


This was only tested between two home NATs on separate cable internet connections.


##More Info
http://en.wikipedia.org/wiki/UDP_hole_punching
