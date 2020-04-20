from general import *
from domain import *
from ipAddress import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'companies'
create_dir ( ROOT_DIR )

def gather_info( name, url):
    robots_txt  = get_robots(url)
    domain_name = get_domain(url)
    whois       = get_whois(url)
    ip_address  = get_ip(url)
    nmap        = get_nmap("-F", ip_address)
    create_report(
        name,
        url,
        domain_name,
        nmap,
        robots_txt,
        whois,
        ip_address
    )

def create_report(name,url,domain_name,nmap,robots_txt,whois):
    project_dir = ROOT_DIR + "/" + name
    create_dir( project_dir )
    write_file( project_dir + "/full_url.txt", url )
    write_file( project_dir + "/domain_name.txt", domain_name )
    write_file( project_dir + "/nmap.txt", nmap )
    write_file( project_dir + "/robots.txt", robots_txt )
    write_file( project_dir + "/whois.txt", whois )
    write_file( project_dir + "/ip_address.txt", ip_address)

gather_info( "google", "https://www.google.com/" )
print("................Scanning..............")
print("Scan Completed!!")