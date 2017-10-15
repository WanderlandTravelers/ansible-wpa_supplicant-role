import pytest
import sys


@pytest.fixture
def wpa_supplicant(host):
    return host.file('/etc/wpa_supplicant/wpa_supplicant.conf')


@pytest.fixture
def network_present(wpa_supplicant):
    """
    Return a method that returns True if the given network is present in the
    wpa_supplicant.conf file
    """
    def _network_present(network):
        if sys.version_info.major > 2 and sys.version_info.minor > 5:
            # Python 3.6 or greater. We have ordered dicts, yay!
            return wpa_supplicant.contains(network.replace('    ', '\t'))
        else:
            # Not quite as robust checking for Pythons with unordered dicts
            return all([
                wpa_supplicant.contains(line.replace('    ', '\t'))
                for line in network.split('\n')
            ])

    return _network_present
