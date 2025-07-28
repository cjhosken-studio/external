import platform

name = "cmake"
version = "3.31.8"

variants = []

build_requires = []

tools = ["cmake", "cmake-gui", "cmcldeps", "cpack", "ctest"]

def commands():
    import platform
    import os

    if platform.system() == "Windows":
        env.PATH.prepend("{root}/bin")
        env.CMAKE_PREFIX_PATH.append("{root}/share/cmake-3.31")
    else:
        os.environ["PATH"] = "{root}/bin;" + os.environ.get("PATH")
        os.environ["CMAKE_PREFIX_PATH"] += ";{root}/share/cmake-3.31"

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"