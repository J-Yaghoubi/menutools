from menutools import Menu

"""
    This example shows how to use the menu, define submenus, 
    switch between routes, and call functions.
"""

# Simple function as an example
def about():
    print('Menu maker')


# Create menu-object
menu = Menu('Example')

# Add sub-menu(route)
menu.add(('First', [
    ('About', about),
    ('Second route', menu.next),
    ('Exit', menu.exit)
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
