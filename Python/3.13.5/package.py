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

variants = []

requires = []

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

def commands():
    import platform
    import os
    
    # Platform-specific environment setup
    if platform.system() == "Windows":
        env.PATH.prepend("{root}")
        env.PATH.prepend("{root}/Scripts")

        env.Python_ROOT.set("{root}")
        env.PYTHON_ROOT.set("{root}")

        env.Python_INCLUDE_DIR.set("{root}/include")
        env.PYTHON_INCLUDE_DIR.set("{root}/include")
        
        env.Python_LIBRARY_DIR.set("{root}/lib")
        env.PYTHON_LIBRARY_DIR.set("{root}/lib")

        env.Python_EXECUTABLE.set("{root}/python.exe")
        env.PYTHON_EXECUTABLE.set("{root}/python.exe")
        
        alias("python3", "{root}/python.exe")
        alias("python3.13", "{root}/python.exe")

    else:
        os.environ["PATH"] = "{root}/bin:" + os.environ.get("PATH")
        os.environ["LD_LIBRARY_PATH"] += "{root}/lib"
        os.environ["PYTHON_EXECUTABLE"] = "{root}/bin/python3"
        
        alias("python", "{root}/bin/python3")

        os.environ["PYTHON_ROOT"] = "{root}"
        os.environ["PYTHON_INCLUDE_DIR"] = "{root}/include"
        os.environ["PYTHON_LIBRARY_DIR"] = "{root}/lib"

import platform

if platform.system() == "Windows":
    build_command = "{root}\\build.bat"
else:
    build_command = """
        # Unix-like build commands (Linux/macOS)
        wget https://www.python.org/ftp/python/{version}/Python-{version}.tar.xz
        tar -xf Python-{version}.tar.xz
        cd Python-{version}
        ./configure --prefix=$REZ_BUILD_INSTALL_PATH
        --enable-optimizations
        --with-lto
        --with-ensurepip=install
        --enable-shared
        LDFLAGS='-Wl,-rpath={root}/lib'
        make -j$NPROC
        make install
        {root}/bin/python3 -m pip install numpy==1.26.4
    """
