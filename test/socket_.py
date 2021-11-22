import socket

print(socket.create_connection(("1.1.1.1", 443), 5))
# [ONLINE]
# <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 56078), raddr=('1.1.1.1', 443)>

# [OFFLINE]
# Traceback (most recent call last):
#   File "socket_.py", line 3, in <module>
#     print(socket.create_connection(("1.1.1.1", 443), 5))
#   File "/opt/conda/envs/dev/lib/python3.8/socket.py", line 808, in create_connection
#     raise err
#   File "/opt/conda/envs/dev/lib/python3.8/socket.py", line 796, in create_connection
#     sock.connect(sa)
# OSError: [Errno 101] Network is unreachabl
