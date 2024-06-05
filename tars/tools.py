# !/usr/bin/python3

# Module / Libraries
from typing import Any, Union, Callable
from whois import whois
from nmap import PortScanner

# NMap Function
def __nmap(target: str, ports: int, argument: str) -> str:
    scanner = PortScanner()
    scanner.scan(hosts=target, ports=ports, arguments=argument)
    return f"""
    Simple NMap Automation by TARS
    ======================================
    IP Target: {target}
    Port Target: {ports}
    Arguments: {argument}
    ======================================
    Tools: NMap
    Version: {scanner.nmap_version()}
    """

# Whois Function
def __whois(url_input: str) -> str:

    try:
        req_whois: Callable = whois(url_input)
        
        if req_whois.domain_name == None:
            return "Silahkan masukan nama domain yang ingin Anda periksa!\nBerikut cara penggunaannya:\n\nwhois > domain_name.com"
    except:
        return "Selamat Domain Tersedia!"

    else:
        result = f""" 
        DOMAIN SUDAH TERPAKAI!!!
        ============================
        Domain: {req_whois['domain_name']}
        Name Server: -
        1. {req_whois['name_servers'][0]}
        2. {req_whois['name_servers'][1]}
        3. {req_whois['name_servers'][2]}
        4. {req_whois['name_servers'][3]}
        5. Registrar: {req_whois['registrar']}
        """
        return result

# Helpers Function
def __helpers() -> str:
    return """
    Berikut ini adalah daftar nama tools dan cara penggunaanya:
======================================
Whois Lookup
whois > example_domain.com
-
"""
