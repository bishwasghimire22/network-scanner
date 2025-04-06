import subprocess
import re
import socket


def get_gateway_info():
    result = subprocess.check_output("ip route", shell=True).decode()
    gateway = re.search(r"default via (\S+)", result).group(1)
    iface = re.search(r"dev (\S+)", result).group(1)
    ip_output = subprocess.check_output(f"ip addr show {iface}", shell=True).decode()
    ip_match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)/(\d+)", ip_output)
    ip = ip_match.group(1)
    cidr = ip_match.group(2)
    subnet = f"{ip}/{cidr}"

    return {"gateway": gateway, "interface": iface, "ip": ip, "subnet": subnet}
