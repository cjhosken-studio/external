name = "qt"

version = "6.8.3"

authors = [
    "Qt Group"
]

description = \
    """
    Qt is a cross-platform application development framework, primarily used for creating graphical user interfaces (GUIs) and applications that can run on various operating systems with little to no code changes.
    """

tools = [

]

requires = [
    "gcc-11.2+"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.set("{root}/lib")