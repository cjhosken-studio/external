name = "cmake"

version = "4.0.3"

authors = [
    "Kitware"
]

description = \
    """
    CMake cross-platform build system package.
    """

tools = [

]

requires = [

]

installer = f"cmake-{version}-linux-x86_64.sh"
url = f"https://github.com/Kitware/CMake/releases/download/v{version}/{installer}" 

build_command = f"""
wget {url}
chmod +x ./{installer}
./{installer} --skip-license --prefix=$REZ_BUILD_INSTALL_PATH
rm -rf ./{installer}
"""

def commands():
    env.PATH.append("{root}/bin")