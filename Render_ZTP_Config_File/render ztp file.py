import logging
from datetime import datetime
from jinja2 import Template

data = {
  "firmware_url": "http://192.168.1.111:8000/sonic-image-v3.1.bin",  # URL for firmware to load in format http://{ip_address | hostname}/{image_name}
  "firmware_reboot_on_success": "true",  # false is the default value

  "config_db_prefix": "http://192.168.1.111:8000/",  # Prefix for where to pull the config_db.json file in the form of http://{ip_address}/
  "config_db_identifier": "hostname",  # identifier ??
  "config_db_suffix": "_config_db.json",  # name of the config file to pull IE: _config_db.json

  "provisioning_script_url": "http://192.168.1.111:8000/post_install.sh",  # URI to pull the provisioning script from in the form of http://{ip_address}/{script.sh}
  "provisioning_script_reboot_on_success": "true",  # false is the default value

  "connectivity_check_hosts": '["8.8.4.4", "yahoo.com"]',  # List of hosts to use to attempt connectivity check
}

template = """{
  "ztp": {
    "01-firmware": {
      "install": {
        "url": "{{ firmware_url }}",
        "set-default": {{ firmware_reboot_on_success }}
      },
      "reboot-on-success": true
    },
    "02-configdb-json": {
      "dynamic-url": {
        "source": {
          "prefix": "{{ config_db_prefix }}",
          "identifier": "{{ config_db_identifier }}",
          "suffix": "{{ config_db_suffix }}"
        }
      }
    },
    "03-provisioning-script": {
        "plugin": {
          "url":"{{ provisioning_script_url }}"
        },
        "reboot-on-success": {{ provisioning_script_reboot_on_success }}
    },
    "04-connectivity-check": {
        "ping-hosts": {{ connectivity_check_hosts }}
    }
  }
}
"""

template2 = """{
  "ztp": {
    "01-connectivity-check": {
      "ping-hosts": {{ connectivity_check_hosts }}
    },
    "02-provisioning-script": {
        "plugin": {
          "url":"{{ provisioning_script_url }}"
        },
        "reboot-on-success": {{ provisioning_script_reboot_on_success }}
    }
  }
}
"""

dictionary = Template(template2)

logging.basicConfig(filename='write_ztp.log', encoding='utf-8', level=logging.INFO)

now = datetime.now()


def write_ztp_file():
    logging.info(f"Writing new ztp.json file {now}...")
    with open("ztp.json", "w") as outfile:
        outfile.write(dictionary.render(data))


write_ztp_file()
