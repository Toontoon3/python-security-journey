port = int(input("Enter port number:"))

if port == 22:
    print("SSH: remote login")
elif port == 80:
    print("HTTP: unencryted web traffic")
elif port == 443:
    print("HTTPS: encrypted web traffic")
else: 
    print("Unknown service")