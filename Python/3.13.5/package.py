name = "python"

version = "3.13.5"

authors = [
    "Python"
]

description = \
    """
    Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
    Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. 
    Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. 
    The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.
    """

tools = [
    "f2py",
    "idle3",
    "idle3.13",
    "pip3",
    "pip3.13",
    "pydoc3",
    "pydoc3.13",
    "python3",
    "python3.13",
    "python3.13-config",
    "python3.13d",
    "python3.13d-config",
    "python3-config",
]

variants = [
    ["vfxbase-2026", "gcc-14.2"]
]


requires = [
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.Python_ROOT.set("{root}")
    env.Python_EXECUTABLE.set("{root}/bin/python3")

    alias("python", "{root}/bin/python3")