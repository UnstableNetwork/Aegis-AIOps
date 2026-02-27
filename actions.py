from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

load_dotenv()

def quarantine_mac(mac_address):
    device = {
        'device_type': 'cisco_ios', # Change to your hardware type
        'host': os.getenv('SWITCH_IP'),
        'username': os.getenv('SSH_USER'),
        'password': os.getenv('SSH_PASS'),
    }
    
    with ConnectHandler(**device) as net_connect:
        # Find port by MAC
        output = net_connect.send_command(f"show mac address-table | i {mac_address}")
        # Simplistic parsing - in production, use Regex
        if output:
            port = output.split()[-1]
            commands = [f"interface {port}", "shutdown", "description QUARANTINED_BY_AEGIS"]
            net_connect.send_config_set(commands)
            return port
    return None
