Ansible wpa_supplicant role
===========================

Ansible role for managing wifi networks

Requirements
------------

Ansible 2.3 or higher

Role Variables
--------------

Here is a list of variables and defaults

wpa_cli_reconfigure: yes  # Whether or not to run `wpa_cli reconfigure` at the end

wpa_ctrl_interface: DIR=/var/run/wpa_supplicant GROUP=netdev  # The value for ctrl_interface in `/etc/wpa_supplicant/wpa_supplicant.conf`

wpa_passphrase: yes  # Whether or not to run `wpa_passphrase` to encrypt network passwords

wpa_networks: []  # A list of network dicts, see molecule/default/playbook.yml for examples

wpa_unquoted:  # A list of network keys for which to wrap the values in quotes
  - eap
  - eapol_flags
  - group
  - key_mgmt
  - pairwise
  - priority
  - scan_ssid

wpa_update_config: 1  # The value for update_config in `/etc/wpa_supplicant/wpa_supplicant.conf`

License
-------

MIT
