name = "python"

version = "3.13.5"
maj, mnr = version.split('.')[0:2]

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

requires = []

tools = [
    "2to3",
    f"2to3-{maj}.{mnr}",
    f"idle{maj}",
    f"idle{maj}.{mnr}",
    f"pip{maj}",
    f"pip{maj}.{mnr}",
    f"pydoc{maj}",
    f"pydoc{maj}.{mnr}",
    f"python{maj}",
    f"python{maj}.{mnr}",
    f"python{maj}-config",
    f"python{maj}.{mnr}-config",
]

def pre_commands():
    env.PYTHONHOME.unset()

def commands():
    import platform
    maj, mnr = f"{version}".split('.')[0:2]

    major_minor = f"{maj}.{mnr}"


    if platform.system() == "Windows":
        pass
    else:
        env.PATH.prepend("{root}/bin")
        env.LD_LIBRARY_PATH.set("{root}/lib")
            
        alias("python", "{root}/bin/python{maj}")

        if building:
            env.PYTHON_ROOT.set("{root}")
            env.PYTHON_INCLUDE_DIR.set("{root}/include")
            env.PYTHON_LIBRARY_DIR.set("{root}/lib")
            env.PYTHON_LIBRARIES.set(f"{{root}}/lib/python/libpython{maj}.so")
            env.PYTHON_EXECUTABLE.set(f"{{root}}/bin/python{maj}")

            env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")
            env.LDFLAGS.prepend("-L{root}/lib -Wl, -rpath, {root}/lib ")
            env.CFLAGS.prepend(f"-I{{root}}/include/python{major_minor} -fPIC -Wall ")
            env.CXXFLAGS.prepend(f"-I{{root}}/include/python{major_minor}")
            env.CPPFLAGS.prepend(f"-I{{root}}/include/python{major_minor}")


import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"