# Ansible Role: wpa_supplicant

[![Build Status][badge-travis]][link-travis]

Configures wpa_supplicant for managing wifi networks.

> Forked from https://github.com/WanderlandTravelers/ansible-wpa_supplicant-role.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    wpa_cli_reconfigure: yes

Whether to run `wpa_cli reconfigure` at the end of playback.

    wpa_ctrl_interface: DIR=/var/run/wpa_supplicant GROUP=netdev

The value for `ctrl_interface` in `/etc/wpa_supplicant/wpa_supplicant.conf`.

    wpa_passphrase: yes

Whether to run `wpa_passphrase` to encrypt network passwords.

    wpa_networks: []

A list of network dicts, see [tests/test.yml](tests/test.yml) for an example.

    wpa_update_config: 1

The value for `update_config` in `/etc/wpa_supplicant/wpa_supplicant.conf`.

## Dependencies

None.

## Example Playbook

    - hosts: servers
      vars_files:
        - vars/main.yml
      roles:
        - { role: jason-riddle.wpa_supplicant }

## License

[MIT][link-license]

## Author Information

The original role, [ansible-wpa_supplicant-role][original-role],
was created in 2017 by [Wanderland Travelers][wanderland-travelers].
This role was forked to
[ansible-role-wpa_supplicant][forked-role]
and this fork is maintained by [Jason Riddle][jason-riddle].

#### Maintainer(s)

- [Jason Riddle][jason-riddle]

[jason-riddle]: https://github.com/jason-riddle
[wanderland-travelers]: https://github.com/WanderlandTravelers
[original-role]: https://github.com/WanderlandTravelers/ansible-wpa_supplicant-role
[forked-role]: https://github.com/jason-riddle/ansible-role-wpa_supplicant
[badge-travis]: https://travis-ci.org/jason-riddle/ansible-role-wpa_supplicant.svg?branch=master
[link-license]: https://raw.githubusercontent.com/jason-riddle/ansible-role-wpa_supplicant/master/LICENSE
[link-travis]: https://travis-ci.org/jason-riddle/ansible-role-wpa_supplicant
