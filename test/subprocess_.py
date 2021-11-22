from os import truncate
from subprocess import check_output, run
import subprocess

# output = check_output("ls")

# print(output)
# print(check_output(["python", "socket_.py"]))
# print(
#     check_output(["python", "socket_2.py"])
# )

# b'colorstr_.py\nlogger.py\nparse_opt.py\nsocket_.py\nsubprocess_.py\nvars-sample.py\n'
# b"<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 56372), raddr=('1.1.1.1', 443)>\n"
# python: can't open file 'socket_2.py': [Errno 2] No such file or directory
# Traceback (most recent call last):
#   File "subprocess_.py", line 10, in <module>
#     check_output(["python", "socket_2.py"])
#   File "/opt/conda/envs/dev/lib/python3.8/subprocess.py", line 415, in check_output
#     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
#   File "/opt/conda/envs/dev/lib/python3.8/subprocess.py", line 516, in run
#     raise CalledProcessError(retcode, process.args,
# subprocess.CalledProcessError: Command '['python', 'socket_2.py']' returned non-zero exit status 2.

# output = run("ls", shell=True, stdout=subprocess.PIPE, check=True).stdout
# print(output)

# b'colorstr_.py\nlogger.py\nparse_opt.py\nsocket_.py\nsubprocess_.py\nvars-sample.py\n'


cmd = "git fetch && git config --get remote.origin.url"
# url = check_output(cmd, shell=True, timeout=10)
# print(url)  # b'git@github.com:t-skmt/yolo-v5.git\n'

# url = check_output(cmd, shell=True, timeout=10).decode()
# print(url)
# # git@github.com:t-skmt/yolo-v5.git
# # 
# url = check_output(cmd, shell=True, timeout=10).decode().strip()
# print(url)  # git@github.com:t-skmt/yolo-v5.git

url = check_output(cmd, shell=True, timeout=10).decode().strip().rstrip(".git")
print(url)  # git@github.com:t-skmt/yolo-v5
branch = check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode().strip()
print(branch)

n = int(check_output(f"git rev-list {branch}..origin/master --count", shell=True))
print(n)

