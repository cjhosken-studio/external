name = "windows"

version = "2025.27.07"

tools = [
    "nmake",
    ""
]

build_command = ""

def commands():
    import os
    os.environ["PATH"] = "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.43.33807\\bin\\Hostx64\\x64;" + os.environ.get("PATH")
    os.environ["PATH"] = "C:\\Program Files (x86)\Windows Kits\\10\\bin\\10.0.22621.0\\x64;" + os.environ.get("PATH")

build_command = "{root}\\build.bat"