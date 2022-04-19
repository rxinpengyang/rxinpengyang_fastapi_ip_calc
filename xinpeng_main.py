from fastapi import FastAPI
from xinpeng_utils import *

app = FastAPI()

# TODO: fix all the naming inconsistencies.

@app.post('/to_binary')
def post_to_binary(number):
    result = decimal_to_binary(int(number))
    return {'value': result}

@app.post('/to_decimal')
def post_to_decimal(number):
    result = binary_to_decimal(number)
    return {'value': result}

@app.post('/decimal_to_binary_ip')
def post_decimal_to_binary_ip(ip):
    result = decimal_to_binary_ip(ip)
    return {'binary ip': result}

@app.post('/binary_to_decimal_ip')
def post_binary_to_decimal_ip(ip):
    result = binary_to_decimal_ip(ip)
    return {'decimal_ip': result}

@app.post('/netmask_length_to_netmask')
def post_netmask_length_to_netmask(number):
    result = netmask_length_to_netmask(number)
    return {'netmask': result}

@app.post('/netmask_length_to_wildcard')
def post_netmask_length_to_wildcard(number):
    result = netmask_length_to_wildcard(number)
    return {'wildcard': result}

@app.post('/ip_and_netmask_to_network_ip')
def post_ip_and_netmask_to_network_ip(ip, netmask):
    result = ip_and_netmask_to_network_ip(ip, netmask)
    return {'network_ip': result}

@app.post('/ip_and_netmask_to_broadcast_ip')
def post_ip_and_netmask_to_broadcast_ip(ip, netmask):
    result = ip_and_netmask_to_broadcast_ip(ip, netmask)
    return {'broadcast_ip': result}

@app.post('/ip_and_netmask_to_min_host')
def post_ip_and_netmask_to_min_host(ip, netmask):
    result = ip_and_netmask_to_min_host(ip, netmask)
    return {'min_host': result}

@app.post('/ip_and_netmask_to_max_host')
def post_ip_and_netmask_to_max_host(ip, netmask):
    result = ip_and_netmask_to_max_host(ip, netmask)
    return {'max_host': result}

@app.post('/netmask_length_to_total_hosts')
def netmask_length_to_total_hosts(netmask_length):
    result = netmask_length_to_number_of_hosts(netmask_length)
    return {'total_hosts': result}

@app.post('/ip_and_netmask_length_to_everything')
def post_ip_and_netmask_length_to_everything(ip, netmask_length):
    netmask, wildcard, network_ip, broadcast_ip, min_host, max_host, \
        number_of_hosts = ip_and_netmask_to_all(ip, netmask_length)
    return {'address': ip, 'netmask': netmask, 'wildcard': wildcard, \
        'network_ip': network_ip, 'broadcast_ip': broadcast_ip, \
            'min_host': min_host, 'max_host': max_host, \
                'number_of_hosts': number_of_hosts}