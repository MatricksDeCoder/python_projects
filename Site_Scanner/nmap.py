import os
# Function to get Nmap Port Scan
def get_nmap ( options, ip ):
    command = "nmap " + options + " " + ip
    process = os.popen( command )
    results = str( process.read() )
    # Returning the final result
    print("Nmap Scan done!")
    return results