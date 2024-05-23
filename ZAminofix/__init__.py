__title__ = 'ZAmino.fix'
__author__ = 'ZOOM'
__copyright__ = 'Copyright (c) 2024 ZOOM37Z'
__version__ = '1.1.8'




from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .lib.util import exceptions, helpers, objects, headers
from .asyncfix import acm, client, sub_client, socket
from .socket import Callbacks, SocketHandler
from requests import get
from json import loads
from os import system,name
from colorama import Fore
# I will cry :(
import httpx
try:
  response = httpx.get("https://pypi.org/pypi/zamino-fix/json")
  response.raise_for_status()  
  newest_version = response.json()["info"]["version"]
except Exception as err:
  print(f"An error occurred: {err}")
  newest_version = None

if newest_version and __version__ < newest_version:
  print(Fore.YELLOW + "[!] You are using old version of zamino.fix, We will update the module automatic for you")
  system("pip install -U ZAmino.fix")
  if name == "nt": system("cls") # This for non-unix systems ( windows , etc )
  else: system("clear") # This For Unix | Unix Like Don't Edit it please
  print(Fore.YELLOW + f"[!] ZAmino Version : {__version__} - Made By : ZOOM + Adham")
else:
  print(Fore.YELLOW + f"[!] ZAmino Version : {__version__} - Made By : ZOOM + Adham") 

