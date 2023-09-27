from pyucc import console, colors

console("Poggers <38;2;0;100;100}}Possible Text", "Other Test")

@console.register(identifier="debug")
def debug(*values, **optional):
  print(values, optional, "|||||||||||")

console.debug("Test")
print(colors.chex("#ffffff", type="background"))


def main():
  pass