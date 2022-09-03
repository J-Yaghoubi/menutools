from menutools import Menu
from menutools import Color
from functools import partial

"""
    An example that show how to use all power of the program and
    make customization
"""

# function without argument
def about():
    print('This is menutools')

# function with argument
def argument_func(text: str):
    print(text)

custom = partial(argument_func, 'This is argument of our function')


# Colorize the menu before initializing
Color.HEADER = 144
Color.MENU = 5
Color.PROMPT = 130
Color.INTERFACE = 245

# Create menu-object
menu = Menu(header='Example', border='=', border_length=60, align='left', splitter=')', prompt='=>')

# Add sub-menu(route)
menu.add(('First', [('About', about), ('Other', custom), ('Second route', menu.next)]))
menu.add(('Second', [('First route', menu.back), ('Third route', menu.next)]))
menu.add(('Third', [('First route', 'First'), ('Second route', menu.back), ('Exit', menu.exit)]))

# Run the program
menu.execute()
