import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_wpa_passphrase_exists(host):
    assert host.file("/usr/bin/wpa_passphrase").exists


@pytest.mark.parametrize('line', [
    'country=GB',
    'ap_scan=1',
    'ctrl_interface=madeup',
    'update_config=0',
])
def test_one_liners(wpa_supplicant, line):
    assert wpa_supplicant.contains(line)


@pytest.mark.parametrize('network', ["""
network={
    ssid="test"
    psk=e0b3e76d15f938fcd6ce682459a868312a0e0b779aee825a66aca6837701e685
    priority=1
    id_str="testOne"
}""", """
network={
    ssid="test2"
    psk=1d38836715b27c7e4812db576ff51e43c77ac17a76314ffb5551002b4217c1eb
    priority=2
    id_str="testTwo"
}""", """
network={
    ssid="testing"
    key_mgmt=NONE
}""", """
network={
    ssid="yourHiddenSSID"
    scan_ssid=1
    psk=f4457c4b9ba5635ff9d694125cf8587e4b0f48b700c8dfb2f6eb4b5b57df9a14
}""", """
network={
    ssid="1x-test"
    scan_ssid=1
    key_mgmt=IEEE8021X
    eap=TLS
    identity="user@example.com"
    ca_cert="/etc/cert/ca.pem"
    client_cert="/etc/cert/user.pem"
    private_key="/etc/cert/user.prv"
    private_key_passwd="password"
    eapol_flags=3
}"""])
def test_network(network_present, network):
    assert network_present(network)
