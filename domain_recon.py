import sys
import socket
import requests
import whois
from colorama import Fore, Style, init

init(autoreset=True)

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"[+] IP: {ip}")
        return ip
    except:
        print(Fore.RED + "[-] Error de IP")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 domain_recon.py <dominio>")
        sys.exit()
    
    target = sys.argv[1]
    print(Fore.CYAN + f"\n[*] Analizando: {target}")
    get_ip(target)
