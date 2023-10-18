# CPE-400-Final-Project

Using the PyBluez python library to discover devices connected to the device that runs code.
Then from finding the correct device wanting to collect data transmitted between the two devices
is done through use of built-in functions.  This data can be output for observation and analysis. 

## Data Directory

This folder holds data collected thus far through use of wireshark.  Data as of now is experimental to ensure we get proper
collection from intended devices.  Up to this point, we have collected network traffic transmitted between local Wifi router
and laptops, desktops, workstations, and mobile devices connected onto wifi.

## Source Code Directory

This holds all the scripts and driver code for connecting to bluetooth devices connected to the device running this code.
Also, can create a socket to connect to specified device as of now.  Using PyBluez library to connect and explore data being 
communicated between an apple watch and a laptop (i.e., Macbook).
