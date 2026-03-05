import subprocess

def get_active_ports() -> list:
    """
    Get list of active ports
    """
    try:
        result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
        ports = []
        for line in result.stdout.split('\n'):
            if 'LISTEN' in line and ':' in line:
                parts = line.split(':')
                if len(parts) > 1:
                    port = parts[-1].strip()
                    if port.isdigit():
                        ports.append(int(port))
        return list(set(ports))  # Remove duplicates
    except Exception as e:
        print(f"Error getting active ports: {e}")
        return []