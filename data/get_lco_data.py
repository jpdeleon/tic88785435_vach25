#!/usr/bin/env python
"""
This scripts downloads photometry (.csv files) from exofop
Next:Use prepare_lco_data.py
"""
import requests
import pandas as pd
import re
from pathlib import Path

# add url below; right click in exofop to copy and paste url here
urls = [
"https://exofop.ipac.caltech.edu/tess/get_file.php?id=975278",
"https://exofop.ipac.caltech.edu/tess/get_file.php?id=972748",
"https://exofop.ipac.caltech.edu/tess/get_file.php?id=970534",
"https://exofop.ipac.caltech.edu/tess/get_file.php?id=965919",
]

def get_filename_from_url(url: str) -> str:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    cd = response.headers.get('Content-Disposition')
    if cd:
        # Try to extract filename from content-disposition header
        fname_match = re.findall('filename="?([^";]+)"?', cd)
        if fname_match:
            return fname_match[0]

    # Fallback: get the last part of the URL
    return url.split("/")[-1].split("?")[0]

def download_file_from_exofop(url: str, dest_folder: str = "."):
    filename = get_filename_from_url(url)
    dest_path = Path(dest_folder) / filename
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Saved: ", dest_path)
    return str(dest_path)


if __name__=='__main__':
    for url in urls:
        download_file_from_exofop(url)
