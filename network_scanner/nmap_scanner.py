#!/usr/bin/env python3  

# Import the subprocess module to run system commands
import subprocess  
import csv

# Function to check if Nmap is installed and accessible
def check_nmap():
    try:
        # Run 'nmap -V' to check version
        # Output and errors are discarded using DEVNULL
        subprocess.run(
            ["nmap", "-V"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True  # If command runs successfully, Nmap is installed
    except:
        return False  # If an error occurs, Nmap is not installed

# Function to return the appropriate Nmap scan option based on user input
def get_scan_command(choice):
    if choice == "1":
        return "-sn"  # Ping scan (host discovery only)
    elif choice == "2":
        return "-p 1-1000"  # Scan ports from 1 to 1000
    elif choice == "3":
        return "-sV"  # Detect service versions
    else:
        return None  # Invalid input

#save results to csv 
def save_to_csv(data):
    filename = "nmap_results.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(["Port", "State", "Service"])
        
        # Write data rows
        for row in data:
            writer.writerow(row)
    
    print(f"Results saved to {filename}")

# save host discovery results to csv
def save_host_csv(data):
    filename = "nmap_results.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Host", "Status"])
        writer.writerows(data)
    
    print(f"Results saved to {filename}")

# Function to execute the Nmap scan
def run_scan(target, scan_option):
    # Construct the full Nmap command safely (no shell=True)
    command = ["nmap"] + scan_option.split() + [target]
    
    print("Scanning... (this may take a while)")  
    
    # Run the command using subprocess
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    
    # Check if the command executed successfully
    if result.returncode == 0:
        print("Scan completed successfully")

        # Handle Basic Host Discovery separately
        if scan_option == "-sn":
            print("Results:")
            print("=" * 45)
            print(f"{'HOST':<20}{'STATUS':<10}")
            print("-" * 45)

            host_data = []
            current_host = ""

            for line in result.stdout.split("\n"):
                if "Nmap scan report for" in line:
                    current_host = line.split("for")[-1].strip()
                if "Host is up" in line:
                    print(f"{current_host:<20}{'UP':<10}")
                    host_data.append([current_host, "UP"])

            print("=" * 45)

            if host_data:
                save_host_csv(host_data)
            else:
                print("No host data to save.")

            return  # stop further processing

        # Port scan / service scan output
        print("Results:")
        print("=" * 45)
        print(f"{'PORT':<10}{'STATE':<10}{'SERVICE':<10}")
        print("-" * 45)

        parsed_data = []

        for line in result.stdout.split("\n"):
            if "/" in line and ("open" in line or "closed" in line):
                parts = line.split()
                if len(parts) >= 3:
                    port = parts[0]
                    state = parts[1]
                    service = parts[2]
                    
                    parsed_data.append([port, state, service])
                    
                    # print in formatted way
                    print(f"{port:<10}{state:<10}{service:<10}")

        print("=" * 45)
        
        # Save results
        if parsed_data:
            save_to_csv(parsed_data)
        else:
            print("No port data to save.")
    else:
        print("Scan failed")
        print(result.stderr)  # Display error message

# Main function to control program flow
def main():
    print("=== Nmap Scanner ===")
    
    # Check if Nmap is installed before proceeding
    if check_nmap():
        print("Nmap is installed")
    else:
        print("Nmap is NOT installed")
        return  # Exit program if Nmap is not available
    
    # Take target input from user (IP address or network range)
    target = input("Enter target IP or network: ")
    
    # Display scan options
    print("Select scan type:")
    print("1. Basic Host Discovery (-sn)")
    print("2. Port Scan (1-1000)")
    print("3. Service Version Detection (-sV)")
    
    # Get user choice
    choice = input("Enter choice (1-3): ")
    
    # Get corresponding scan option
    scan_option = get_scan_command(choice)
    
    # Handle invalid input
    if scan_option is None:
        print("Invalid choice")
        return
    
    # Run the selected scan
    run_scan(target, scan_option)

# Entry point of the script
if __name__ == "__main__":
    main()