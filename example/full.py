from menutools import Menu
from menutools import Color
from functools import partial

"""
    Here is an example that shows how you can customize the menu 
    and use all the powers of the program
"""

# function without argument
def about():
    print('This is menutools')

# function with argument
def argument_func(text: str):
    print(text)
    # we want switch to second route after finishing the job
    return 'Second'


custom = partial(argument_func, 'This is argument of our function')


# Colorize the menu before initializing
Color.BORDER = 32
Color.HEADER = 144
Color.MENU = 5
Color.PROMPT = 130
Color.INTERFACE = 245

# Create menu-object
menu = Menu(
    header='Example',
    border='=',
    border_length=60,
    align='center',
    splitter=')',
    prompt='=>'
)

# Add sub-menu(route)
menu.add(('First', [
    ('About', about),
    ('Other', custom),
    ('Second route', menu.next)
]))

menu.add(('Second', [
    ('First route', menu.back),
    ('Third route', menu.next)
]))

menu.add(('Third', [
    ('First route', 'First'),
    ('Second route', menu.back),
    ('Exit', menu.exit)
]))

# Run the program
menu.execute()
