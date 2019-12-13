import Pyro4
from app1Phase2 import workflowLog

uri = input("What is the Pyro uri of the greeting object?").strip()
name = input("What is your name?").strip()

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune(name))
workflowLog('Pass App4')
