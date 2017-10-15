Ansible wpa_supplicant role
===========================

[![Travis](https://img.shields.io/travis/WanderlandTravelers/ansible-wpa_supplicant-role.svg)](https://travis-ci.org/WanderlandTravelers/ansible-wpa_supplicant-role) [![Ansible Role](https://img.shields.io/ansible/role/21206.svg)](https://galaxy.ansible.com/WanderlandTravelers/wpa_supplicant/)

Ansible role for managing wifi networks. Run `man wpa_supplicant.conf` for more information

Requirements
------------

Ansible 2.3 or higher

Role Variables
--------------

Here is a list of variables you can use to control playback:

* `wpa_cli_reconfigure`: Controls whether or not to run `wpa_cli reconfigure` at the end of playback. Defaults to `yes`

* `wpa_ctrl_interface`: The value for `ctrl_interface` in `/etc/wpa_supplicant/wpa_supplicant.conf`. Defaults to `DIR=/var/run/wpa_supplicant GROUP=netdev`

* `wpa_passphrase`: Controls whether or not to run `wpa_passphrase` to encrypt network passwords. Defaults to `yes`

* `wpa_networks`: A list of network dicts, see molecule/default/playbook.yml for examples. Defaults to `[]`

* `wpa_update_config`: The value for `update_config` in `/etc/wpa_supplicant/wpa_supplicant.conf`. Defaults to `1`

License
-------

MIT
