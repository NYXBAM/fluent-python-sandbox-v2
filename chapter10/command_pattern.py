class MacroCommand:
    def __init__(self, commands):
        self.commands = list(commands)
        
    def __call__(self):
        for command in self.commands:
            command()
            

def test_command():
    print('Test command 1')

def test_command2():
    print('Test command 2')

commands = MacroCommand([test_command, test_command2])

print(commands.__dict__) # {'commands': [<function test_command at 0x109f6b380>, <function test_command2 at 0x109fd7880>]}\

commands() # Test command 1
           # Test command 2

