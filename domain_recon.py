import sys
import socket
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"[+] IP Principal: {ip}")
        return ip
    except:
        print(Fore.RED + "[-] No se pudo resolver la IP principal.")
        return None

def check_subdomains(domain):
    print(Fore.YELLOW + "\n[*] Buscando subdominios comunes...")
    # Lista de prueba rápida
    subs = ["www", "mail", "ftp", "dev", "admin", "api", "test", "staging"]
    
    for sub in subs:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            print(Fore.GREEN + f"    [+] Encontrado: {url} -> {ip}")
        except socket.gaierror:
            pass # Si no existe, pasamos al siguiente
import sys
import socket
import requests
def print_banner():
    banner = f"""
{Fore.MAGENTA}    ____                        _       ____                      
   |  _ \  ___  _ __ ___   __ _(_)_ __ |  _ \ ___  ___ ___  _ __  
   | | | |/ _ \| '_ ` _ \ / _` | | '_ \| |_) / _ \/ __/ _ \| '_ \ 
   | |_| | (_) | | | | | | (_| | | | | |  _ <  __/ (_| (_) | | | |
   |____/ \___/|_| |_| |_|\__,_|_|_| |_|_| \_\___|\___\___/|_| |_|
{Style.RESET_ALL}
    """
    print(banner)
if __name__ == "__main__":
    print_banner()  # <--- Agrega esto aquí
    if len(sys.argv) != 2:
        # ... resto del código ...
from colorama import Fore, Style, init

init(autoreset=True)

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"[+] IP Principal: {ip}")
        return ip
    except:
        print(Fore.RED + "[-] No se pudo resolver la IP principal.")
        return None

def check_subdomains(domain):
    print(Fore.YELLOW + "\n[*] Buscando subdominios comunes...")
    # Lista de prueba rápida
    subs = ["www", "mail", "ftp", "dev", "admin", "api", "test", "staging"]
    
    for sub in subs:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            print(Fore.GREEN + f"    [+] Encontrado: {url} -> {ip}")
        except socket.gaierror:
            pass # Si no existe, pasamos al siguiente

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.WHITE + "Uso: python3 domain_recon.py <dominio>")
        sys.exit()
    
    target = sys.argv[1]
    print(Fore.CYAN + f"\n" + "="*30)
    print(Fore.CYAN + f" ANALIZANDO: {target}")
    print(Fore.CYAN + "="*30)
    
    if get_ip(target):
        check_subdomains(target)
    
    print(Fore.CYAN + "\n[!] Escaneo finalizado.")
