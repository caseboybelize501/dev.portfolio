import subprocess
import json

def scan_static_sites(tools) -> dict:
    """
    Check for available static site generators
    """
    static_sites = {}
    
    # Check Next.js
    try:
        result = subprocess.run(["npm", "list", "next"], capture_output=True, text=True)
        if "next" in result.stdout:
            static_sites["next"] = {
                "installed": True,
                "version": extract_version("next", result.stdout)
            }
    except Exception as e:
        print(f"Next.js check failed: {e}")
    
    # Check Astro
    try:
        result = subprocess.run(["npm", "list", "astro"], capture_output=True, text=True)
        if "astro" in result.stdout:
            static_sites["astro"] = {
                "installed": True,
                "version": extract_version("astro", result.stdout)
            }
    except Exception as e:
        print(f"Astro check failed: {e}")
    
    # Check Hugo
    try:
        result = subprocess.run(["hugo", "version"], capture_output=True, text=True)
        if "Hugo" in result.stdout:
            static_sites["hugo"] = {
                "installed": True,
                "version": extract_hugo_version(result.stdout)
            }
    except Exception as e:
        print(f"Hugo check failed: {e}")
    
    return static_sites

def extract_version(package, output) -> str:
    """
    Extract version from npm list output
    """
    lines = output.split('\n')
    for line in lines:
        if package in line and '@' in line:
            parts = line.split('@')
            if len(parts) > 1:
                return parts[1].split('#')[0].strip()
    return "unknown"

def extract_hugo_version(output) -> str:
    """
    Extract Hugo version from output
    """
    if 'Hugo' in output:
        return output.split('Hugo ')[1].split()[0]
    return "unknown"