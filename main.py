#### `main.py`

from scanner.network_info import get_gateway_info
from scanner.ip_scanner import scan_local_network
from scanner.port_scanner import scan_ports
from scanner.utils import save_results


def main():
    print("[*] Starting network scan...\n")

    gateway_info = get_gateway_info()
    print("[+] Gateway Info:", gateway_info)

    active_hosts = scan_local_network(gateway_info["subnet"])
    print(f"[+] Found {len(active_hosts)} active hosts.")

    for host in active_hosts:
        ports = scan_ports(host["ip"])
        host["open_ports"] = ports

    save_results(gateway_info, active_hosts)
    print("\n[+] Scan complete. Results saved to output/scan_results.json")


if __name__ == "__main__":
    main()
