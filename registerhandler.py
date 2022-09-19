
# Get socket
import socket   

# Request License - Hash Later
validop = input("Whats your license key? ")

# replace with domain verification with secure cdn.

# Verify License Integrity
with open('license.txt') as f:
    if validop in f.read():
        print("License Validated")
        # Failed License Action
    else:
        print("failed license verification")
        # Stops Program on failure to verify.
        exit()

# Tell user program is still running.

print("Program is auditing auth action -- sharing is not permitted. Please wait for further notice.")

# Fetch ip and pc name
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   


# Create local auth
f = open("localauth.txt", "x")
f.close()
# Write Auth info to file - hash later

f = open("localauth.txt", "a")
f.write(hostname)
f.write(IPAddr)

f.close()

# Action above writes identifying details above in a file to auth login

print("auth file written")

print("setup completed.")

