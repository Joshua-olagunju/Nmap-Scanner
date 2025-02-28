import subprocess

def nmap_scan():
    print("Welcome to the Scanner!")
    print("This tool helps you perform different kinds of Nmap scans to check for open ports or identify the OS of a target.")
    print("Note: All scan types except -sT require sudo\n")
    print("Nmap must be installed on your system!")

    target = input("Enter the address you want to scan: ")

    valid_scan = ["-sS", "-sT", "-sU", "-O"]

    while True:
        scantype = input("Enter the type of Nmap scan (-sS, -sT, -sU, -O): ")
        if scantype in valid_scan:
            break
        print("Invalid scan type! Please enter a valid option: -sS, -sT, -sU, -O, press CTRL + D or CTRL + Z to exit")

    print("Please wait, your scan is loading...\n")

    command = ["nmap", scantype, "-Pn", target]
    result = subprocess.run(command, capture_output=True, text=True)

    filename = f"scan_results_{target.replace('.', '_')}.txt"
    with open(filename, "w") as file:
        file.write(result.stdout)

    print("Scan completed! Results have been saved to:", filename, "in your current directory")

nmap_scan()
