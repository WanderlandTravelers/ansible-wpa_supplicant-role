import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_wpa_supplicant_is_installed(host):
    wpa_supplicant = host.package("wpasupplicant")
    assert wpa_supplicant.is_installed


def test_wpa_country(wpa_supplicant):
    assert not wpa_supplicant.contains('country=')


def test_ap_scan(wpa_supplicant):
    assert not wpa_supplicant.contains('ap_scan=')


def test_control_interface(wpa_supplicant):
    assert wpa_supplicant.contains(
        'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev')


def test_update_config(wpa_supplicant):
    assert wpa_supplicant.contains('update_config=1')


def test_network(wpa_supplicant):
    assert not wpa_supplicant.contains('network={')


def test_wpa_cli_exists(host):
    assert host.file("/sbin/wpa_cli").exists
