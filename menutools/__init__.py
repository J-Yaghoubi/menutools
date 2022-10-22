import os
import sys
import logging


logger = logging.getLogger('menutools')


class Color:
    BORDER = 0
    HEADER = 0
    MENU = 0
    PROMPT = 0
    INTERFACE = 0


class Menu:
    """
    A class for creating command-line menus


    Attributes
    ----------
    header: str
        The text that appears in the header of the program as the project name

    border: str
        Define character that repeat as border

    border_length: int
        Defining the repeat of the border character

    align: str
        This can be set to left, right, or center and define header alignment. By default is left

    splitter: str
        Character that split the index number from menu-titles

    prompt: str
        The character representing the program is waiting for a key


    Methods
    -------
    add:
        Create a new defined route by getting the tuple

    exit:
        Stop the program from running

    next:
        Set next route as selected route

    back:
        Make the previous route the selected route

    execute:
        Print a list of options in the current route by running the program
    """

    def __init__(self, header: str = None, border: str = '=', border_length: int = 50,
                 align: str = 'left', splitter: str = '.', prompt: str = '>>') -> None:
        self.header = str(header)
        self.border = str(border)
        self.border_length = int(border_length) if border_length >= 1 else 1
        self.align = '^' if align.lower(
        ) == 'center' else '>' if align.lower() == 'right' else '<'
        self.prompt = str(prompt)
        self.splitter = str(splitter)
        self._cursor = 0
        self._routes: list = []
        self._key = 0
        self._c_border = self._colorize(Color.BORDER)
        self._c_header = self._colorize(Color.HEADER)
        self._c_menu = self._colorize(Color.MENU)
        self._c_prompt = self._colorize(Color.PROMPT)
        self._c_interface = self._colorize(Color.INTERFACE)

    def _refresh(self) -> None:
        """Clear the screen"""
        os.system('clear') if os.name == 'posix' else os.system('cls')

    def _colorize(self, value: int) -> str:
        """Validate the selected color code"""
        try:
            value = int(value)
            if 0 <= value <= 255:
                return u"\u001b[38;5;" + str(value) + "m"
        except Exception:
            pass

        return u"\u001b[38;5;0m"

    def _waiting(self, any=False) -> int | str:
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
        except Exception:
            self._refresh()
            self._show()
            return self._waiting()
        else:
            return key - 1

    def _print_header(self, job: str = None) -> None:
        """
        The functionality of this method is clearing the screen and printing the header
        """
        self._refresh()
        if self.header:
            print(self._c_border + self.border * self.border_length)
            job_title = f'::{job}' if job else ''
            title = f'{self.header}::{self._routes[self._cursor][0]}{job_title}'
            adjust = self.border_length * len(self.border)
            print(f'{self._c_header}{title:{self.align}{adjust}}')
            print(self._c_border + self.border *
                  self.border_length + self._c_interface + '\n')

    def _show(self) -> None:
        """
        The functionality of this method is clearing the screen, printing the header
        and, printing the menu list
        """
        self._print_header()
        order = 1
        for m in self._routes[self._cursor][1]:
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
        for cur in self._routes:
            if cur[0] == route:
                self._cursor = self._routes.index(cur)
                break

    def next(self) -> None:
        """Select next route if exists"""
        if self._cursor < len(self._routes) - 1:
            self._cursor += 1
        self.execute()

    def back(self) -> None:
        """Select previous route if exists"""
        if self._cursor > 0:
            self._cursor -= 1
        self.execute()

    def exit(self) -> None:
        """Exit from program"""
        logger.debug('Program has been closed')
        sys.exit()

    def add(self, sub_menu: tuple) -> None:
        """Define new route"""
        self._routes.append(sub_menu)

    @property
    def _current_title(self):
        return self._routes[self._cursor][1][self._key][0]

    @property
    def _current_function(self):
        return self._routes[self._cursor][1][self._key][1]

    def execute(self) -> None:
        """Execute the menu"""
        self._show()
        self._key = int(self._waiting())

        # if user selection is out of the range, repeat the process
        if self._key > len(self._routes[self._cursor][1])-1 or self._key < 0:
            self.execute()

        # do it in valid range
        else:

            # if selected option is string, switch to selected route
            if isinstance(self._current_function, str):
                self._select(self._current_function)
                self.execute()

            # if selected option is callable, execute it
            else:
                self._print_header(self._current_title)
                func = self._current_function
                logger.debug(f'{func} has been executed')
                result = func()
                if isinstance(result, str):
                    self._select(result)
                self._waiting(any=True)
                self.execute()
