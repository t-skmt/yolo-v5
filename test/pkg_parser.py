import pkg_resources as pkg
# import platform

# current, minimum = (platform.python_version(), "3.6.a")
# print(current, type(current))

# # pep440に規定されている規則にしたがってバージョンを解析する
# a, b = (pkg.parse_version(x) for x in (current, minimum))
# print(a, b)
# print(type(a), type(b))
# # 3.8.12 <class 'str'>
# # 3.8.12 3.6a0
# # <class 'pkg_resources.extern.packaging.version.Version'> <class 'pkg_resources.extern.packaging.version.Version'>

a = "1.2"
b = "1.2.0"
print(a == b)  # False

a, b = (pkg.parse_version(x) for x in (a, b))
print(a == b)  # True
