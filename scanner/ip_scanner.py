import nmap


def scan_local_network(subnet):
    nm = nmap.PortScanner()
    print(f"[*] Scanning subnet: {subnet}")
    nm.scan(hosts=subnet, arguments="-sn")
    hosts = []

    for host in nm.all_hosts():
        if "mac" in nm[host]["addresses"]:
            mac = nm[host]["addresses"]["mac"]
        else:
            mac = "N/A"
        hosts.append({"ip": host, "hostname": nm[host].hostname(), "mac": mac})

    return hosts
