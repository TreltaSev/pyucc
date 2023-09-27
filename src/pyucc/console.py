import re
import traceback
from typing import Any, Union, List, Optional, Literal
class console:
  """
  Uses ANSI escape codes and 30 minutes of stitching to display
  colored text inside console. All of the methods are optional, fully configurable and better
  yet, completly modularizable. which im not sure if its a word but im going with it.
  """

  def __init__(self, *values: Any, sep: Optional[str] = " ", end: Union[str, None] = "\n", file: Union[None, None] = None, flush: Literal[True, False] = False):
    """
    This just copies :method:`console.cprint`, input values in this as you would console.cprint.
    this is here for easier importing and usage.

    ---

    An "Inherited" print method, utilizes `python's builtin print method` to immediatly print out a formated string.

    :param values: Just like any `print statement` in python, these are the things that will be printed out.
    :param sep: The `seperator` between all the values.
    :param end: The end of the `print statement`, defaults to `\\n`
    :param file: a file-like object (stream); defaults to the current sys.stdout.
    :param flush: whether to forcibly flush the stream.    
    """
    console.cprint(*values, sep=sep, end=end, file=file, flush=flush)

  @staticmethod
  def format(*values: List[Any], sep: Optional[str] = "", itemized: Optional[bool] = False) -> Union[str, List[str]]:
    """
    Parses a given text(s) while replacing specific key codes
    and turning them into colorized text inside the console.

    :param args: All the texts or options used, must all be `str` serialiable.
    :param sep: if itemized is false, this concats all the values, adding the `sep` in between every value Default is an empty string.
    :param itemized: turns the return type to a list, containing all formated objects seperated. Defaults to `False`.    
    :return: Hopefully a string that contains text which when printed, is colored!
    :rtype: str
    """

    __colorized: List[str] = []
    
    # Iterate through all the inputed texts
    for textSection in values:
      try:      

        # Find all color formatting
        regularMatch = re.compile(r"\<([^}]*)\}").search(textSection)

        # Iterate through all matches
        if regularMatch:
          for match in regularMatch.groups():
            textSection = textSection.replace(f"<{match}}}", f"\u001B[{match}m")

        __colorized.append(textSection)

      except Exception as e:
        print(f"Oooh boi you fucked up {e}")
        traceback.print_exc()
        return   
    
    __colorized.append("\u001B[0;38;48m")

    if not itemized:
      __colorized: str = sep.join(__colorized)
            
    return __colorized
  
  @classmethod
  def cprint(cls, *values: Any, sep: Optional[str] = " ", end: Union[str, None] = "\n", file: Union[None, None] = None, flush: Literal[True, False] = False) -> None:
    """
    An "Inherited" print method, utilizes `python's builtin print method` to immediatly print out a formated string.

    :param values: Just like any `print statement` in python, these are the things that will be printed out.
    :param sep: The `seperator` between all the values.
    :param end: The end of the `print statement`, defaults to `\\n`
    :param file: a file-like object (stream); defaults to the current sys.stdout.
    :param flush: whether to forcibly flush the stream.    
    """    
    print(*cls.format(*values, sep=None, itemized=True), sep=sep, end=end, file=file, flush=flush)

  @classmethod
  def register(cls, func):
    
    def wrapper(*args, **kwargs):
      print(func, args, kwargs)
    
    return wrapper

  def __getattribute__(self, __name: str) -> Any:
    print(f"Getting {__name}")
    
