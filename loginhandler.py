import socket   


# Print TItle

print("Log In Manager")

# Set Keypins

keypins = 1

#Key Request 

key = input("license key: ")

# Fetch information for hwid logic

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname) 

#hwid logic 

hwid = hostname+IPAddr
print(hwid)

# Math licencse verification.

with open('license.txt') as f:
    if key in f.read():
        print("License Key Valid")
        keypins = + 1
        # Failed License Action
    else:
        print("failed license verification")
        # Stops Program on failure to verify.
        exit()

# Alert users for wait

print("Please wait while we validate your hardware id.")

# Logic for mathching hwid

with open('localauth.txt') as f:
    if hwid in f.read():
        print("HWID Matches License")
        keypins = + 1
        # Failed hwid
    else:
        print("failed hwid verification")
       
        exit()

# Add keypin for passing HWID

keypins = + 1

# Verify keypins for secure auth


if keypins == 3:
    print("Keypins: ", keypins, "  Auth Valid")
