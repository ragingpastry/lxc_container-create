# Example Playbook
```bash
---
- name: Install LXC containers
  hosts: all
  roles:
    - role: lxc_container-create
```

# Example host_vars  
```bash
---
lxc_containers:
  - galera:
    name: galera1
    template: centos
    extra_args: ""
  - keystone:
    name: keystone1
    template: centos
    extra_args: ""

container_network:
  galera1:
    ipv4_address: 10.100.10.185/24
    ipv4_gateway: 10.100.10.1
    type: veth                                                                                                                                                                                                                                                                   
    bridge: br-mgmt                                                                                                                                                                                                                                                              
    interface: eth1
  keystone1:
    ipv4_address: 10.100.10.195/24
    ipv4_gateway: 10.100.10.1
    type: veth                                                                                                                                                                                                                                                                   
    bridge: br-mgmt                                                                                                                                                                                                                                                              
    interface: eth1
```
