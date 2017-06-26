import testinfra.utils.ansible_runner
import os
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", os.path.join("../../defaults/main.yml"))["ansible_facts"]

@pytest.fixture()
def get_container_names(host, AnsibleVars):
    services = AnsibleVars['services']
    service_names = []
    for subvalue, subkey in services.items():
        service_names += subkey[0]['name']
    return service_names

    
def test_lxc_service_enabled(host):
    lxc_service = host.service('lxc')
    assert lxc_service.is_running
    assert lxc_service.is_enabled

def test_lxc_containers_running(host, get_container_names):
    for container in get_container_names:
        assert host.ansible("command","lxc-info -n %s" % container)["rc"] == 0
    
