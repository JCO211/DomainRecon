import sys
import socket
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = r"""
{color}    ____                        _       ____                      
   |  _ \  ___  _ __ ___   __ _(_)_ __ |  _ \ ___  ___ ___  _ __  
   | | | |/ _ \| '_ ` _ \ / _` | | '_ \| |_) / _ \/ __/ _ \| '_ \ 
   | |_| | (_) | | | | | | (_| | | | | |  _ <  __/ (_| (_) | | | |
   |____/ \___/|_| |_| |_|\__,_|_|_| |_|_| \_\___|\___\___/|_| |_|
{reset}
    """.format(color=Fore.MAGENTA, reset=Style.RESET_ALL)
    print(banner)

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"[+] IP Principal: {ip}")
        return ip
    except socket.gaierror:
        print(Fore.RED + f"[-] No se pudo resolver la IP para: {domain}")
        return None

def check_subdomains(domain):
    print(Fore.YELLOW + "\n[*] Buscando subdominios comunes...")
    subs = ["www", "mail", "ftp", "dev", "admin", "api", "test", "staging"]
    found = []
    for sub in subs:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            result = f"[+] Encontrado: {url} -> {ip}"
            print(Fore.GREEN + f"    {result}")
            found.append(result)
        except socket.gaierror:
            pass
    return found

if __name__ == "__main__":
    print_banner()
    if len(sys.argv) != 2:
        print(Fore.WHITE + "Uso: python3 domain_recon.py <dominio>")
        sys.exit()
    
    target = sys.argv[1]
    main_ip = get_ip(target)
    
    if main_ip:
        results = check_subdomains(target)
        filename = f"reporte_{target}.txt"
        with open(filename, "w") as f:
            f.write(f"REPORTE OSINT PARA: {target}\n")
            f.write(f"IP Principal: {main_ip}\n")
            f.write("-" * 40 + "\n")
            for r in results:
                f.write(r + "\n")
        print(Fore.CYAN + f"\n[!] Reporte guardado en: {filename}")
    
    print(Fore.CYAN + "\n[!] Escaneo finalizado.")
