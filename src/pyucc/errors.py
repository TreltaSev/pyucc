from typing import Optional, Any, Literal

class HighException(Exception):
  """
  Low Level Base Exception which will be used as a building 
  block for future exceptions.

  :paramm message: The error message defaults to None
  :param name: Name of the error, or cause
  :type message: str
  :type name: str
  """

  def __init__(self, message: Optional[str] = None, *args: Any, name: str) -> None:
    self.name: str = name
    self.message = message or f'Error: {name!r}'
    super().__init__(self.message, *args)

  def display(self):
    """
    Displays the selected error with bcolors.fail
    """

    # bcolors.console.fail(f'{bcolors.colors.brRed}{self.message}')

class OverwriteTrigger(HighException):
  def __init__(self, identifier: str, __type: Literal["overwrite", "unsafe_overwrite"]) -> None:
    super().__init__(f"Overwrite error has been triggered, the console registration with the identifier: \"{identifier}\" needs {__type} to be registered as true.", name="OverwriteTrigger")

class InvalidInput(HighException):
  def __init__(self, value: Any, __while: str = None, looking_for: str = None, valid_value: Any = None):
    super().__init__(f"Got {value}, while: {__while} Looking for: {looking_for}, Valid Value: {valid_value}", name="Invalid Input")