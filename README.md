# dev_PythonMicroservices
Python Microservice Development

##### Notes
- Docker MacOS
  - Virtualbox is 
    `$VBoxManage list -l hostonlyifs`
  - Docker-machine Virtualbox
    - On Linux, MacOS ... Virtualbox only allow IP addresses in 192.168.56.0/21 range to be assigned to host-only adapters (192.168.56.1 - 192.168.63.255)
    - Docker-machine tries to move HostOnly network to 192.168.99.1/24
      `docker-machine create -d virtualbox --virtualbox-hostonly-cidr "192.168.61.1/24" default`
