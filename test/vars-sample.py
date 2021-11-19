class Test:
    def __init__(self, a=5, b=4):
        self.a = a
        self.b = b


obj = Test()

# The vars() function returns the __dict__ attribute of the given object.
# If the object passed to vars() doesn't have the __dict__ attribute, it raises a TypeError exception.

print(vars(obj))
# print(vars())
# print(obj.__dict__)
print(vars(obj).items())
for k, v in vars(obj).items():
    print(k, v)

print("name: "+ ",".join(f"{k}={v}" for k, v in vars(obj).items()))
