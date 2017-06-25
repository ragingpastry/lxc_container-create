import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_lxc_service_enabled(host):
    lxc_service = host.service('lxc')
    assert lxc_service.is_running
    assert lxc_service.is_enabled
