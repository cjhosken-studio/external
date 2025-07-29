name = "cmake"
version = "3.31.8"
maj, mnr = version.split('.')[0:2]

variants = [
    ['platform-linux', 'arch-x86_64']
]

tools = [
    "cmake", 
    "cpack", 
    "ctest"
]

#requires = ["gcc"] ld causes issues

def commands():
    maj, mnr = f"{version}".split('.')[0:2]
    major_minor = f"{maj}.{mnr}"

    env.PATH.prepend("{root}/bin")

    if building:
        env.CMAKE_PREFIX_PATH.append(f"{{root}}/share/cmake-{major_minor}")


build_command = "{root}/build.sh"