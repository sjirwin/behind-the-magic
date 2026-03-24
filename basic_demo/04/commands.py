from pprint import pp
pp(Demo.__dict__)
z = Demo()
z.a
z.a = "hello"
z.b
z.b = 42
z.a
z.__dict__
