import scapy.all as scapy
from brain import analyze_threat
from actions import quarantine_mac

KNOWN_DEVICES = ["00:11:22:33:44:55"] # Replace with your real whitelist

def process_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        src_mac = packet[scapy.ARP].hwsrc
        
        if src_mac not in KNOWN_DEVICES:
            print(f"[!] Unknown MAC {src_mac} detected. Consulting AI...")
            
            # Consult the AI Brain
            decision = analyze_threat(src_mac, "Unknown device broadcasting ARP on protected segment.")
            print(f"[AI Verdict]: {decision}")
            
            if "ISOLATE" in decision.upper():
                print(f"[*] Executing Isolation Playbook for {src_mac}...")
                port = quarantine_mac(src_mac)
                print(f"[SUCCESS] Port {port} disabled.")

print("Aegis AIOps Core Active. Sniffing for threats...")
scapy.sniff(prn=process_packet, filter="arp", store=0)
