import os
import sys


class Color:
    HEADER = 0
    MENU = 0
    PROMPT = 0
    INTERFACE = 0


class Menu:
    """
    A class for creating command-line menus

    Attributes
    ----------
    header : str
        text that print on head of program
    splitter : str
        character that split the index number from menu-title
    prompt : str
        character representing that program is waiting for a key

    Methods
    -------
    add(sub_menu):
        Get the tuple and save it as new defined route   

    exit:
        Close the program and end the program

    select:
        Get a sub_menu title and set the cursor on this route and 
        make it current route

    next:
        Select next route as a current route

    back:
        Select previous route as a current route

    execute:
        run the program and print list of options in the current route
    """

    def __init__(self, header: str = None, border: str = '=', border_length: int = 50, align : str = 'center', splitter: str = '.', prompt: str = '>>') -> None:
        self.header = header
        self.border = border
        self.border_length = border_length
        self.align = '^' if align.lower() == 'center' else '>' if align.lower() == 'right' else '<'
        self.prompt = prompt
        self.splitter = splitter
        self._cursor = 0
        self._sub = []
        self._key = 0
        self._c_header = u"\u001b[38;5;" + str(Color.HEADER) + "m"
        self._c_menu = u"\u001b[38;5;" + str(Color.MENU) + "m"
        self._c_prompt = u"\u001b[38;5;" + str(Color.PROMPT) + "m" 
        self._c_interface = u"\u001b[38;5;" + str(Color.INTERFACE) + "m" 

    def _refresh(self) -> None:
        """Clear screen"""
        os.system('clear') if os.name == 'posix' else os.system('cls')

    def _waiting(self, any=False) -> int:
        """
        Waiting for receiving user selection key

        Parameters
        ----------
        any : boolean
            it will wait for all keys if 'any' sets to true
        """
        print(self._c_prompt)

        if any:
            print('Press any key...')
            return input(self.prompt + ' ' + self._c_interface)
        try:
            key = int(input(self.prompt + ' ' + self._c_interface))
        except:
            self._refresh()
            self._show()
            return self._waiting()
        else:
            return key - 1

    def _print_header(self) -> None:
        """
        The functionality of this method is clearing the screen and printing the header
        """
        self._refresh()
        if self.header:
            print(f'{self._c_header}{self.border * self.border_length}')
            title = f'{self.header}::{self._sub[self._cursor][0]}'
            print(f'{title:{self.align}{self.border_length}}')
            print(self.border * self.border_length + self._c_interface + '\n')

    def _show(self) -> None:
        """
        The functionality of this method is clearing the screen, printing the header 
        and, printing the menu list
        """
        self._print_header()
        order = 1
        for m in self._sub[self._cursor][1]:
            print(self._c_menu + str(order) + self.splitter, m[0])
            order += 1

    def _select(self, route: str) -> None:
        """
        Set menu cursor on preferred route

        Parameters
        ----------
        route : str
            it will search the input str in menu routes and set cursor on requested route
        """
        for cur in self._sub:
            if cur[0] == route:
                self._cursor = self._sub.index(cur)
                break

    def next(self) -> None:
        """Select next route if exists"""
        if self._cursor < len(self._sub) - 1:
            self._cursor += 1
        self.execute()

    def back(self) -> None:
        """Select previous route if exists"""
        if self._cursor > 0:
            self._cursor -= 1
        self.execute()

    def exit(self) -> None:
        """Exit from program"""
        sys.exit()

    def add(self, sub_menu: tuple) -> None:
        """Define new route"""
        self._sub.append(sub_menu)

    @property
    def _current_title(self):
        return self._sub[self._cursor][1][self._key][0]

    @property
    def _current_function(self):
        return self._sub[self._cursor][1][self._key][1]

    def execute(self) -> None:
        """Execute the menu"""
        self._show()
        self._key = self._waiting()

        if self._key > len(self._sub[self._cursor][1])-1 or self._key < 0:
            self.execute()
        else:
            if isinstance(self._current_function, str):
                self._select(self._current_function)
                self.execute()
            else:
                self._print_header()
                situation = self._current_function()
                if situation:
                    self._select(situation)
                self._waiting(any=True)
                self.execute()
