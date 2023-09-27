from pyucc import errors
from typing import Literal

class pyucc_useable:  

  def __init__(self, type: Literal["foreground", "background"] = "foreground") -> None:
    self.type = type

  @property
  def switch(self) -> str:
    """
    Switches the current type and this method also returns the formated value
    :return: A Formated string of the other type
    :rtype: str
    """
    self.type = "foreground" if self.type == "background" else "background"
    return self.__repr__()

  def __repr__(self) -> str:
    return f"<{'38' if self.type == 'foreground' else '48'};2;{self.r};{self.g};{self.b}}}"

class crgb(pyucc_useable):
  def __init__(self, r: int, g: int, b: int, type: Literal["foreground", "background"]="foreground"):
    """
    Returns an object containing a rgb notation in a string
    that can be used with pyucc

    :param r: Red Intensity
    :param g: Red Intensity
    :param b: Red Intensity
    """

    super().__init__(type=type)

    def valid(num: int) -> bool:
      if num < 0 or num > 255:
        return False
      return True
    
    self.r = r
    self.g = g
    self.b = b

    if False in [valid(self.r), valid(self.g), valid(self.b)]:
      raise errors.InvalidInput([valid(self.r), valid(self.g), valid(self.b)], "Checking RGB Values", "A Valid RGB Integer", "0-255")
    
    

class chex(pyucc_useable):
  def __init__(self, __hex: str, type: Literal["foreground", "background"]="foreground"):
    """
    Returns an object containing a rgb notation in a string
    that can be used with pyucc

    :param __hex: The hex color like #fff or #ffffff
    :param type: The type being 'foreground' or 'background'
    :return: an object containing r, g, and b as values and when printed is formatted.
    :rtype: self
    """

    super().__init__(type=type)

    self.hex: str = __hex
    
    __hex = __hex.lstrip("#")

    try:
      match len(__hex):
        case 3:
          self.r: int = self.convert(__hex[0]) * 17
          self.g: int = self.convert(__hex[1]) * 17
          self.b: int = self.convert(__hex[2]) * 17
        case 6:
          self.r: int = self.convert(__hex[0:2])
          self.g: int = self.convert(__hex[2:4])
          self.b: int = self.convert(__hex[4:6])
    except errors.InvalidInput as error:
      print("Failed invalid input", error)      

  @staticmethod
  def convert(content: str) -> int:
    """
    Converts pairs or singles such as "f" or "ff" to their int decimal
    counterpart.

    :param content: Hex character(s)
    :type content: str
    :return: A decimal notation
    :rtype: int
    """

    try:
      __decimal = int(content, 16)
    except ValueError:
      raise errors.InvalidInput(content, "Converting Hex to Int", "A Valid Hex Color Code", "f or ff")
    return __decimal

white = chex("#ffffff", "foreground")
vibrant_green = chex("#71ff71", "foreground")
vibrant_yellow = chex("#FFCE00", "foreground")
vibrant_orange = chex("#FF7300", "foreground")
vibrant_red = chex("#FF3F30", "foreground")
vibrant_blue = chex("#305EFF", "foreground")
vibrant_violet = chex("#8942BE", "foreground")