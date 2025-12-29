#!/usr/bin/env python3
import requests
import re
import sys
import time
from packaging import version

MAX_RETRIES = 3

def get_latest_version():
    url = "https://api.github.com/repos/n8n-io/n8n/releases"
    response = None
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url)
            response.raise_for_status()
            break
        except requests.exceptions.RequestException:
            if attempt == MAX_RETRIES - 1:
                raise
            time.sleep(1)
    
    releases = response.json()
    
    valid_versions = []
    
    for release in releases:
        tag_name = release.get("tag_name", "")
        
        match = re.match(r"^n8n@(\d+\.\d+\.\d+)$", tag_name)
        if match:
            ver = match.group(1)
            valid_versions.append((ver, tag_name))
    
    if not valid_versions:
        print("::set-output name=LATEST_TAG::")
        return None
    
    valid_versions.sort(key=lambda x: version.parse(x[0]), reverse=True)
    
    latest_ver, latest_tag = valid_versions[0]
    
    print(f"::set-output name=LATEST_TAG::{latest_tag}")
    return latest_tag

if __name__ == "__main__":
    latest_tag = get_latest_version()
