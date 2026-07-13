#!/usr/bin/env python3
import sys, os

DNS = {'shecan': ['178.22.122.100', '185.51.200.2'], 'electro': ['78.157.42.100', '78.157.42.101'], 'radar': ['10.202.10.10', '10.202.10.11'], 'google': ['8.8.8.8', '8.8.4.4'], 'clear': []}

def set_dns(dns_list):
    if os.geteuid() != 0:
        print('❌ Run as root (sudo)')
        sys.exit(1)
    try:
        with open('/etc/resolv.conf', 'w') as f:
            f.write('# Generated\n')
            for ip in dns_list:
                f.write(f'nameserver {ip}\n')
            if not dns_list:
                f.write('nameserver 8.8.8.8\nnameserver 1.1.1.1\n')
        print('✅ DNS updated!')
    except Exception as e:
        print(f'❌ Failed: {e}')

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in DNS:
        print('Usage: python3 dns.py [shecan|electro|radar|google|clear]')
        sys.exit(0)
    set_dns(DNS[sys.argv[1]])