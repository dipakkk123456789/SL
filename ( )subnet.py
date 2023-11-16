class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.octets = [int(octet) for octet in ip_address.split('.')]
        self.binary_ip = self.ip_decimal_to_binary()
        
    def ip_decimal_to_binary(self):
        binary_octets = [format(octet, '08b') for octet in self.octets]
        return '.'.join(binary_octets)

    def class_finder(self):
        first_octet = self.octets[0]
        if 0 <= first_octet <= 127:
            return 'Class A'
        elif 128 <= first_octet <= 191:
            return 'Class B'
        elif 192 <= first_octet <= 223:
            return 'Class C'
        elif 224 <= first_octet <= 239:
            return 'Class D'
        elif 240 <= first_octet <= 255:
            return 'Class E'
        else:
            return 'Invalid IP address'

    def subnet_generator(self, no_hosts):
        # Calculate the subnet mask based on the number of hosts
        subnet_mask = 32 - (no_hosts).bit_length()
        return subnet_mask

    def generate_network_range(self, subnet_mask):
        ip_range = 2 ** (32 - subnet_mask)
        print("Number of IPs in each subnet:", ip_range)
        # Add logic here to generate the network range for given subnet mask

def main():
    ip_address = input("Enter IP address (format: xxx.xxx.xxx.xxx): ")
    no_hosts = int(input("Enter number of hosts: "))
    
    ip = IPAddress(ip_address)
    
    print("IP in binary:", ip.binary_ip)
    print("IP belongs to:", ip.class_finder())

    subnet_mask = ip.subnet_generator(no_hosts)
    print("Subnet mask:", subnet_mask)

    # Generate the network range based on the subnet mask
    ip.generate_network_range(subnet_mask)

if __name__ == "__main__":
    main()
