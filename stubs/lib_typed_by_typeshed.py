"""
This lib isn't typed. It's not even installed locally, but there is type hint because 
the .pyi files are embded in Pyright (Pylance)
"""

import requests  # type: ignore

res = requests.get(url="https://google.com")
