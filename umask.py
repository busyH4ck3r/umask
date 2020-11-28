"""
Description:
-----------
    If you are planning a social engineering test, try this script to mask your IP or ngrok with the domain of your choice.
    
Tip: you cannot mask a twitter url with facebook url logically    

Usage:
-----
    python3 umask.py 
    
"""

from urllib.parse import urlparse

from requests import post


banner = r"""


██    ██       ███    ███  █████  ███████ ██   ██ 
██    ██       ████  ████ ██   ██ ██      ██  ██  
██    ██ █████ ██ ████ ██ ███████ ███████ █████   
██    ██       ██  ██  ██ ██   ██      ██ ██  ██  
 ██████        ██      ██ ██   ██ ███████ ██   ██ 
                                                  
                                                                                                        
"""
#print(".......EDITED BY r00t..............")
#print("@r00t_Africa, busyH4ck3r")
developer = {
    "Names": "Mike Moima",
    "twitter": "@root_Arica",
    "youtube" : "Busy Hacker"
}

for key, value in developer.items():
    print(f"@developer {key:>16s} : {value}\n")

def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://da.gd/s/?url={big_url}").text


def MaslUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    print(f"\033[91m {banner}\033[00m")
    print("\n")
    target = input("ENTER REAL URL (http://eehhhe.ngrok.io): ")
    domain = input("ENTER THE DOMAIN TO MASK WITH (e.g https://facebook.com): ")
    keyword = input("ENTER THE KEYWORDS WITHOUT WHITESPACE (use '-' instead of whitespace): ")
    print(" YOUR MASKED DOMAIN WILL LOOK LIKE: \n")
    print(f"\033[91m {MaslUrl(target, domain, keyword)}\033[00m")
