import subprocess

p = subprocess.Popen("/bin/ls", stdout=subprocess.PIPE)
(stdout, stderr) = p.communicate()

print stdout
