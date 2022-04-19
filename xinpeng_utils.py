'''
Utils.
'''

def decimal_to_binary(decimal_number):
    # Converts decimal to binary.
    return f'{decimal_number:08b}'

def binary_to_decimal(binary_number):
    # Converts binary to decimal.
    return f'{int(binary_number, 2)}'

def decimal_to_binary_ip(decimal_ip):
    # Split ip into 4 parts.
    result = decimal_ip.split('.')

    #
    result = [decimal_to_binary(int(x)) for x in result]

    # Join the parts together.
    result = '.'.join(result)

    return result

def binary_to_decimal_ip(binary_ip):
    result = binary_ip.split('.')

    result = [binary_to_decimal(x) for x in result]

    result = '.'.join(result)

    return result

def netmask_length_to_netmask(netmask_length):
    # Converts the string input into integer.
    netmask_length = int(netmask_length)
    # Initialize the list which will contain the netmask.
    netmask = []

    # Adds a number of 1s based on the size of the netmask.
    for i in range(netmask_length):
        netmask.append('1')

    # Fills the remaining spaces in the netmask with 0s.
    for i in range(32 - netmask_length):
        netmask.append('0')

    # Join the parts together.
    netmask = ''.join(netmask)

    octet_1 = binary_to_decimal_ip(netmask[:8])
    octet_2 = binary_to_decimal_ip(netmask[8:16])
    octet_3 = binary_to_decimal_ip(netmask[16:24])
    octet_4 = binary_to_decimal_ip(netmask[24:])

    # Adds the dots to finish the netmask.
    netmask = f'{octet_1}.{octet_2}.{octet_3}.{octet_4} = {netmask_length}'

    return netmask

def netmask_length_to_wildcard(netmask_length):
    # Converts the string input into integer.
    netmask_length = int(netmask_length)
    # Initialize the list which will contain the wildcard.
    wildcard = []

    for i in range(netmask_length):
        wildcard.append('0')

    for i in range(32 - netmask_length):
        wildcard.append('1')

    wildcard = ''.join(wildcard)

    octet_1 = binary_to_decimal_ip(wildcard[:8])
    octet_2 = binary_to_decimal_ip(wildcard[8:16])
    octet_3 = binary_to_decimal_ip(wildcard[16:24])
    octet_4 = binary_to_decimal_ip(wildcard[24:])

    wildcard = f'{octet_1}.{octet_2}.{octet_3}.{octet_4}'

    return wildcard

def ip_and_netmask_to_network_ip(ip, netmask_length):
    # TODO: Add something to automatically change decimal ip to binary.

    network = [decimal_to_binary(int(x)) for x in ip.split('.')]

    netmask_length = int(netmask_length)

    network = ''.join(network)[:netmask_length] + '0' * (32 - netmask_length)

    octet_1 = binary_to_decimal(network[:8])
    octet_2 = binary_to_decimal(network[8:16])
    octet_3 = binary_to_decimal(network[16:24])
    octet_4 = binary_to_decimal(network[24:])

    network = f'{octet_1}.{octet_2}.{octet_3}.{octet_4}/{netmask_length}'

    return network

def ip_and_netmask_to_broadcast_ip(ip, netmask_length):
    # TODO: Add something to automatically change decimal ip to binary.

    broadcast = [decimal_to_binary(int(x)) for x in ip.split('.')]

    netmask_length = int(netmask_length)

    broadcast = \
        ''.join(broadcast)[:netmask_length] + '1' * (32 - netmask_length)

    octet_1 = binary_to_decimal(broadcast[:8])
    octet_2 = binary_to_decimal(broadcast[8:16])
    octet_3 = binary_to_decimal(broadcast[16:24])
    octet_4 = binary_to_decimal(broadcast[24:])

    broadcast = f'{octet_1}.{octet_2}.{octet_3}.{octet_4}'

    return broadcast

# TODO: Fix long lines here.
def ip_and_netmask_to_min_host(ip, netmask_length):
    min_host = [decimal_to_binary(int(x)) for x in ip.split('.')]

    netmask_length = int(netmask_length)

    min_host =  ''.join(min_host)[:netmask_length] + '0' * (32 - netmask_length - 1) + '1'

    octet_1 = binary_to_decimal(min_host[:8])
    octet_2 = binary_to_decimal(min_host[8:16])
    octet_3 = binary_to_decimal(min_host[16:24])
    octet_4 = binary_to_decimal(min_host[24:])

    min_host = f'{octet_1}.{octet_2}.{octet_3}.{octet_4}'

    return min_host

# TODO: Fix long lines here.
def ip_and_netmask_to_max_host(ip, netmask_length):
    max_host = [decimal_to_binary(int(x)) for x in ip.split('.')]

    netmask_length = int(netmask_length)

    max_host = ''.join(max_host)[:netmask_length] + '1' * (32 - netmask_length - 1) + '0'

    octet_1 = binary_to_decimal(max_host[:8])
    octet_2 = binary_to_decimal(max_host[8:16])
    octet_3 = binary_to_decimal(max_host[16:24])
    octet_4 = binary_to_decimal(max_host[24:])

    max_host = f'{octet_1}.{octet_2}.{octet_3}.{octet_4}'

    return max_host

def netmask_length_to_number_of_hosts(netmask_length):
    result = str(pow(2, 32 - int(netmask_length)) - 2)
    return result

def ip_and_netmask_to_all(ip, netmask_length):
    netmask = netmask_length_to_netmask(netmask_length)

    wildcard = netmask_length_to_wildcard(netmask_length)

    network_ip = ip_and_netmask_to_network_ip(ip, netmask_length)

    broadcast_ip = ip_and_netmask_to_broadcast_ip(ip, netmask_length)

    min_host = ip_and_netmask_to_min_host(ip, netmask_length)

    max_host = ip_and_netmask_to_max_host(ip, netmask_length)

    number_of_hosts = netmask_length_to_number_of_hosts(netmask_length)
    
    return netmask, wildcard, network_ip, broadcast_ip, min_host, max_host, \
        number_of_hosts

if __name__ == '__main__':
    pass