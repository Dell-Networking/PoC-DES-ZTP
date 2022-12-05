#!/bin/bash -eux

sleep 10  # SONiC ZTP will reset the network interfaces right before executing the script - this allows enough time to ensure the interfaces are all healthy

mkdir /home/admin/.ssh

curl http://192.168.1.111:8000/authorized_keys > /home/admin/.ssh/authorized_keys

chown -R admin /home/admin/.ssh/

chmod 700 /home/admin/.ssh/

passwd -d admin # This will wipe out the admin password, preventing SSH login without a key cheaply but will also allow local console access without creds
                # default for these images is YourPaSsWoRd

decode-syseeprom > /home/admin/eeprom_info.txt

chown admin /home/admin/eeprom_info.txt

#apt-get update

#apt-get install facter

#facter --json > /admin/facter-output.json
