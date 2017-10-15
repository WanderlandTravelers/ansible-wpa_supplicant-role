import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_no_passphrase_network(network_present):
    assert network_present("""
network={
    ssid="test"
    psk="testtest"
}""")
