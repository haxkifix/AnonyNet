import subprocess

def open_openvpn_connect():
    try:
        subprocess.Popen("C:\Program Files\OpenVPN Connect\OpenVPNConnect")  # Replace with the correct executable name
    except FileNotFoundError:
        print("OpenVPN Connect executable not found.")

