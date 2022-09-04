# MenuTools
A powerful tool to create customizable command prompt menu as simple as possible.

+ [Instalation](#instalation)
+ [How to use it](#how-to-use-it)
+ [Customization](#customization)
+ [Some more](#more)

## Instalation:
just write this code on the python command line:

```bash
pip install menutools
```

## How to use it:
In the simplest way, all things to do is create a menu object, add a route, then execute the menu.      
The route should add in form of a tuple. The first member of this tuple should be unique string that represents the name of the route, the second member is a list of the tuple that defines the menu and their functionality. For functionality, there is some pre-defined option that you can choose in addition to custom functionality:

+ **next**: the next route will be taken.
+ **back**: the previous one will be select.
+ **exit**: will closes the program.
+ **string**: the name of the route can be passed as a string if you want to jump over routes and go to the special one.
+ **functions**: the menu will accept the name of your preferred function without parentheses. So if the function does not get any arguments, all should do is pass its name. But if the function needs some argument it's required to make and partial object and pass this new object to the menu.

```python
from menutools import Menu
from functools import partial

# Simple function
def simple_function():
    pass

# Argument function
def argument_function(subject: str):
    print(subject)
    # we want switch to second route after finishing the job
    return 'Second'

custom = partial(argument_function, 'argument')

# Create menu-object
menu = Menu(header='Example')

# Add sub-menu(route)
menu.add(('First', [('About', custom), ('More', menu.next)]))
menu.add(('Second', [('One', menu.back), ('Two', 'First'), ('Exit', menu.exit)]))

# Run
menu.execute()
```

One another option that can benefit from it is switching between routes after executing a function. For example suppose we are in route First and run a custom function. If at the end we return a string that matches one defined route, then the menu will appear from that menu instead of the First route.


## Customization:
For colorization, import Color class from project and choose your favorite colors in the form of integer number between 0~255. In this case you can customize the color of header, menu, interface, and prompt. Note that Colorizing should be done before creating the menu-object. The following is an example:

```python
from menutools import Color

Color.BORDER = 100
Color.HEADER = 144
Color.MENU = 5
Color.PROMPT = 130
Color.INTERFACE = 245
```


In addition to color, it is possible to do some interface changes when we create a new menu object. At this level, we can customize the border, align of header text, choose the splitter, and etc:

```python
from menutools import Menu

menu = Menu(header='Example', border='=', border_length=60,
    align='center', splitter=')', prompt='=>')
```

![Mneu](/src/example.png)


## More:
If need to know more about using this tools can check the Example directory.
