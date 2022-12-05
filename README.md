# Leveraging ZTP with Dell Enterprise SONiC

The purpose of this PoC is to provide an example of how to leverage zero touch provisioning with Dell Enterprise SONiC devices. ZTP provides an initial provisioning mechanism by which you can script any number of arbitrary operations including pushing down an initial configuation.. 

## Background 

Dell Enterprise SONiC comes with a process that starts on boot called ztp. This is a systemd daemon that will look for a few specific DHCP options in a DHCP offer and depending on the offer received, will take one of a few actions:

| DHCPv4 Offer | Action Taken                        | Notes                         |
|--------------|-------------------------------------|-------------------------------|
| option 67    | pull config file via TFTP           | can also use DHCPv6 option 59 |
| option 239   | pull config file or script via HTTP |                               |

> Note: for additional details on how ZTP within Dell Enterprise SONiC works, please reference the user guide.

## Approach

For this guide we'll be leveraging the second option - serving DHCP option 239 so the ZTP process will pull a configuration script and SSH authorized_keys file.

## How to use This Repo

Git clone this repo to a linux host (physical server or virtual machine). If there is already a DHCP server configured on the L2 segment that you will be provisioning systems on, do not run the DHCP server included in this repo, only run the HTTP server. If you need to serve DHCP, ensure the machine you clone this to is on the same L2 domain as the systems you'll be provisioning via ZTP (with the management port of the systems to be configured connected to the provisioning L2 domain).

If only serving files by HTTP (without running the DHCP server), run the command `docker compose -f docker-compose.no-dhcp.yml up`
 
Before running the DHCP server, make sure to configure the correct file in the DHCP_Server folder and specify the network interface the server should bind to. If left as the default, the DHCP server may not bind to the correct port. 

To start the DHCP server and the HTTP server, run the command `docker compose -f docker-compose.yml up`.

> Note: There are inherent dangers of running a DHCP server 
