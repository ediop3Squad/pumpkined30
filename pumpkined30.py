from scapy.all import *
import os

def display_logo():
    logo = """
    ██████╗░██╗░░░██╗███╗░░░███╗██████╗░██╗░░██╗██╗███╗░░██╗███████╗██████╗░██████╗░░█████╗░
    ██╔══██╗██║░░░██║████╗░████║██╔══██╗██║░██╔╝██║████╗░██║██╔════╝██╔══██╗╚════██╗██╔══██╗
    ██████╔╝██║░░░██║██╔████╔██║██████╔╝█████═╝░██║██╔██╗██║█████╗░░██║░░██║░█████╔╝██║░░██║
    ██╔═══╝░██║░░░██║██║╚██╔╝██║██╔═══╝░██╔═██╗░██║██║╚████║██╔══╝░░██║░░██║░╚═══██╗██║░░██║
    ██║░░░░░╚██████╔╝██║░╚═╝░██║██║░░░░░██║░╚██╗██║██║░╚███║███████╗██████╔╝██████╔╝╚█████╔╝
    ╚═╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░░╚════╝░
    """
    print(logo)
    print("\nMade by ediop3Squad leader\n")

def get_user_input():
    print("pumpkined30 packet injector boii\n")
    
    # Get network interface
    interface = input("Enter the network interface (e.g., wlan0, eth0): ")

    # Get target IP
    target_ip = input("Enter the target IP address: ")

    # Get packet type (e.g., ICMP, TCP, UDP)
    print("\nSelect the packet type to inject:\n1. ICMP (Ping)\n2. TCP\n3. UDP")
    packet_type = input("Enter packet type number (1/2/3): ")

    if packet_type == '1':
        packet_type = 'ICMP'
    elif packet_type == '2':
        packet_type = 'TCP'
    elif packet_type == '3':
        packet_type = 'UDP'
    else:
        print("Invalid packet type. Defaulting to ICMP.")
        packet_type = 'ICMP'
    
    # Get target port for TCP/UDP
    target_port = None
    if packet_type in ['TCP', 'UDP']:
        target_port = int(input("Enter the target port (e.g., 80): "))

    return interface, target_ip, packet_type, target_port

def inject_packet(interface, target_ip, packet_type, target_port=None):
    print(f"\nInjecting {packet_type} packet to {target_ip} using {interface}...\n")
    
    # ICMP Packet (Ping)
    if packet_type == 'ICMP':
        packet = IP(dst=target_ip)/ICMP()
    
    # TCP Packet
    elif packet_type == 'TCP':
        packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")  # SYN packet
    
    # UDP Packet
    elif packet_type == 'UDP':
        packet = IP(dst=target_ip)/UDP(dport=target_port)
    
    else:
        print("Invalid packet type.")
        return
    
    # Inject the packet
    send(packet, iface=interface)
    print(f"{packet_type} packet sent to {target_ip} on {interface}.\n")

if __name__ == '__main__':
    # Ensure the user runs the script as root
    if os.geteuid() != 0:
        print("Please run this script as root!")
        exit(1)

    # Display logo and credits
    display_logo()

    # Get input from user
    interface, target_ip, packet_type, target_port = get_user_input()
    
    # Inject the packet
    inject_packet(interface, target_ip, packet_type, target_port)
