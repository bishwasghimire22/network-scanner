import json
import os


def save_results(gateway_info, hosts):
    if not os.path.exists("output"):
        os.makedirs("output")
    data = {"gateway": gateway_info, "hosts": hosts}
    with open("output/scan_results.json", "w") as f:
        json.dump(data, f, indent=4)
