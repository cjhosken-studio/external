name = "qt"

version = "6.5.3"

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
    "cmake-3.31.7+",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")