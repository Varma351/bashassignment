#!/usr/bin/env python3

# import required modules
import subprocess   # to run system commands (like arp -a)
import platform     # to detect operating system
import re           # for pattern matching (IP & MAC)
import sys          # for exiting program safely
import csv          # to save data in CSV file


# function to detect OS (not heavily used but useful info)
def get_os():
    return platform.system().lower()


# function to run arp command and get output
def run_arp():
    try:
        # run the command: arp -a
        result = subprocess.run(
            ['arp', '-a'],
            stdout=subprocess.PIPE,   # capture output
            stderr=subprocess.PIPE,   # capture errors
            text=True                # convert output to string
        )

        # if command runs successfully
        if result.returncode == 0:
            return result.stdout   # return arp table output
        else:
            print("Error:", result.stderr)
            return None

    except Exception as e:
        print("Error running arp:", e)
        return None


# function to extract IP and MAC addresses from output
def parse_output(output):
    entries = []   # list to store results

    # regex pattern for IP address
    ip_pattern = r'(\d{1,3}(\.\d{1,3}){3})'

    # regex pattern for MAC address
    mac_pattern = r'([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}'

    # split output into lines
    lines = output.split('\n')

    # check each line
    for line in lines:
        # skip empty lines
        if line.strip() == "":
            continue

        # skip incomplete entries
        if "incomplete" in line.lower():
            continue

        # search for IP and MAC in the line
        ip = re.search(ip_pattern, line)
        mac = re.search(mac_pattern, line)

        # if both found
        if ip and mac:
            ip_addr = ip.group()   # extract IP
            mac_addr = mac.group().upper()  # extract MAC and convert to uppercase

            # convert MAC format from - to :
            mac_addr = mac_addr.replace('-', ':')

            # skip broadcast addresses
            if mac_addr != "FF:FF:FF:FF:FF:FF" and ip_addr != "255.255.255.255":
                entries.append([ip_addr, mac_addr])  # store in list

    return entries


# function to display results in table format
def show(entries):
    # if no entries found
    if len(entries) == 0:
        print("\nNo ARP entries found")
        return

    # print table header
    print("\n" + "=" * 40)
    print("IP Address        | MAC Address")
    print("=" * 40)

    # print each entry
    for e in entries:
        print(f"{e[0]:<18} | {e[1]}")

    # print total count
    print("=" * 40)
    print("Total:", len(entries))


# function to save results into CSV file
def save(entries):
    # ask user if they want to save
    choice = input("\nSave results to CSV? (y/n): ").lower()

    if choice != 'y':
        return

    # get filename from user
    filename = input("Enter filename (default arp.csv): ").strip()

    # set default filename
    if filename == "":
        filename = "arp.csv"

    # ensure file has .csv extension
    if not filename.endswith(".csv"):
        filename += ".csv"

    try:
        # open file in write mode
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)

            # write header row
            writer.writerow(["IP Address", "MAC Address"])

            # write data rows
            for e in entries:
                writer.writerow([e[0], e[1]])

        print("Saved to", filename)

    except Exception as e:
        print("Error saving file:", e)


# main function (program starts here)
def main():
    print("=" * 40)
    print("ARP Scanner")
    print("=" * 40)

    # print OS info
    print("OS:", platform.system())

    # run arp command
    output = run_arp()

    # if command failed
    if output is None:
        return

    # extract IP-MAC pairs
    entries = parse_output(output)

    # display results
    show(entries)

    # save if entries exist
    if len(entries) > 0:
        save(entries)

# entry point of program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # handle Ctrl+C safely
        print("\nStopped by user")
        sys.exit()