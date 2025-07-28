name = "windows"

version = "latest"

tools = [
    "nmake"
]

def commands():
    env.PATH.prepend("C:/Program Files (x86)/Windows Kits/10/bin/10.0.22621.0/x64")
    env.PATH.prepend("C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.44.35207/bin/Hostx64/x64")

build_command = "{root}/build.bat"