#import all the required modules 
import subprocess #used to run terminal process in python
import platform #used to check the os  
import re #regular expression used to extract required data
import csv #used to extract data to a excle sheet 

def get_ip(x):
    ostype = platform.system().lower()

    if ostype == "windows":
        ops="-n"
    else:
        ops="-c"
    # the above if else statement is used to verify the type of operating system in use so that the code is cross-platform

#implemeting a error handling function 
    try:
        result = subprocess.run(
            ["ping", ops, "1", x], #"4" refers to the number of packets sent was changed to 1 to increse execution time  
            stdout=subprocess.PIPE, #capture regular output
            stderr=subprocess.PIPE, #used for error capture 
            text=True, #converts bits to text 
            timeout=2 #initallay was 5 sec reduced to 2  
        )
        
        output = result.stdout

        if result.returncode == 0:
            match = re.search(r'Average\s*=\s*(\d+)', output) or \
                    re.search(r'=\s*[\d\.]+/([\d\.]+)/', output)
        # the above block is used if ping is successful to extract avg time

            a_t = match.group(1) if match else "N/A"
            return x,"up",a_t
        else:
            return x,"down","N/A"
    #if ping ping takes to long to terminate it we use except 
    except subprocess.TimeoutExpired:
        return x,"down","Timeout"

#defining a function range incrementor 
def scan_range(base_ip, start, end):
    results = []

    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        host, status, avg = get_ip(ip)

        print(f"{host} → {status} ({avg})")
        results.append([host, status, avg])

    return results

#exporting the values to csv file with ip address || status of it || and average time
def save_to_csv(data, filename="Ping.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Status", "Average Time (ms)"])
        writer.writerows(data)

    print(f"\nResults saved to {filename}")


#main functioin 
if __name__ == "__main__":
    print("=== PING Scanner ===")

    base_ip = input("Enter base IP (e.g., 192.168.1): ")
    start = int(input("Start range: "))
    end = int(input("End range: "))

    Ping = scan_range(base_ip, start, end)
    save_to_csv(Ping)
