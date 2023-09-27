# PyUCC

### An Unoptimezed Console Colorization tool written in python.

## How to Install

This python project was converted to a pypi package, to install this package you can just use [pip](https://pypi.org/project/pip/).

```python
pip install pyucc
```

## Usage

After installing the package with pip, all you need to do is import it like you would any other package and work on colorizing your precious console. This package relies on ANSI Unicode Escape Sequences to allow for coloring in the rgb space inside your console.

```python
from pyucc import console, colors

# Use cprint or colored print just like you would pythons print method.
console.cprint(colors.vibrant_red, "This text is in red")

# You can also use formatting
console.cprint(f"{colors.vibrant_red}This text is also in red")

# Use .switch for background switch
console.cprint(f"{colors.vibrant_red.switch}This text has a red background")
```

> Basic Red Text

There are some more advanced use cases like registering your own console class:

```python
from pyucc import console, colors, symbols

@console.register(identifier="test")
def test(*values, **optional):
  # Optional can be used to access "optional" values like time.
  time = optional.get("time")
  console.cprint(f"{colors.vibrant_purple.switch} Debug {symbols.reset} {colors.chex('#aaaaaa')}{time}{symbols.reset}", *values)

console.test("This is the test method")
```

> Advanced customized console

Also, cprint can be used as print if you need to.

```python
from pyucc import console
console.cprint("This is just a print")
```
