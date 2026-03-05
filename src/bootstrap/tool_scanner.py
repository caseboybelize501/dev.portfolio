import subprocess
import json

def scan_tools() -> dict:
    """
    Inventory node/python3/git installations
    """
    tools = {}
    
    # Check node
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        tools["node"] = {
            "version": result.stdout.strip(),
            "path": find_executable("node")
        }
    except Exception as e:
        print(f"Node not found: {e}")
    
    # Check python3
    try:
        result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
        tools["python"] = {
            "version": result.stdout.strip(),
            "path": find_executable("python3")
        }
    except Exception as e:
        print(f"Python not found: {e}")
    
    # Check git
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        tools["git"] = {
            "version": result.stdout.strip(),
            "path": find_executable("git")
        }
    except Exception as e:
        print(f"Git not found: {e}")
    
    return tools

def find_executable(name) -> str:
    """
    Find executable path
    """
    try:
        result = subprocess.run(["which", name], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        return "unknown"