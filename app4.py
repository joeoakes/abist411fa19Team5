import Pyro4

uri = input("What is the Pyro uri of the greeting object?").strip()
name = input("What is your name?").strip()

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune(name))
