

import subprocess
def change_mac(interface, Mac):
    print("[+]Program were stated")

    subprocess.call(["ifconfig", interface, "down"])
    print("[/]Down been completed")

    print("[/] Mac is changing")
    subprocess.call(["ifconfig", interface, "hw", "ether", Mac])

    subprocess.call(["ifconfig", interface, "up"])
    print("[/]Up been completed")

def print_mac(interface):
	print("[/] Your new MAC is -> ")
	subprocess.call("ifconfig "+interface+" | grep ether", shell=True)