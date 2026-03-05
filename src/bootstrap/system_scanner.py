import os
import hashlib
import subprocess
import json
from pathlib import Path
from src.bootstrap.system_profile import SystemProfile
from src.bootstrap.model_scanner import scan_models
from src.bootstrap.tool_scanner import scan_tools
from src.bootstrap.static_site_scanner import scan_static_sites
from src.bootstrap.port_registry import get_active_ports

def scan_system() -> SystemProfile:
    """
    Scan system for local assets and configurations
    """
    print("Starting system scan...")
    
    # Walk C:\ D:\ for model files
    models = scan_models(["C:\", "D:\"])
    
    # Probe inference servers
    inference_servers = probe_inference_servers()
    
    # Inventory node/python3/git
    tools = scan_tools()
    
    # Check static site generators
    static_sites = scan_static_sites(tools)
    
    # Get active ports
    ports = get_active_ports()
    
    # Create system profile
    system_profile = SystemProfile(
        models=models,
        inference_config=inference_servers,
        tools=tools,
        static_sites=static_sites,
        ports=ports
    )
    
    # Write to file
    with open("SystemProfile.json", "w") as f:
        json.dump(system_profile.dict(), f, indent=2)
    
    print("System scan complete.")
    return system_profile

def probe_inference_servers() -> dict:
    """
    Probe for available inference servers
    """
    # Placeholder implementation
    return {
        "llm": "llama-2-7b",
        "api_url": "http://localhost:8080",
        "status": "available"
    }