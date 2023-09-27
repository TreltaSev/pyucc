from pyucc import console, colors, symbols

def main():
  console.cprint(f"Hi there, this is {colors.vibrant_orange}pyucc{symbols.reset}", 
                 f"a real {colors.vibrant_green}beginner friendly{symbols.reset}", 
                 f"to create and register differnet cutomized print methods.\n"
                 f"You can keep things simple or you can add some advanced sludge to it.",
                 f"Heres an example:")
  console.example("This is an example I displayed by running console.example('Text')")
  console.example("I hate documenting things so this may not be very in depth but take a look at the docs and experiment :)")
  