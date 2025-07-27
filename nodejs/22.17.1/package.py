name = "nodejs"

version = "22.17.1"

authors = [
    "nodejs"
]

description = \
    """
    """

tools = [
    "nvm",
    "node",
    "npm"
]

requires = []

build_command = f"""
NVM_DIR=$REZ_BUILD_INSTALL_PATH
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source $NVM_DIR/nvm.sh && nvm install {version}
node -v
nvm current
npm -v
"""

def commands():
    env.NVM_DIR.set("{root}")
    command("source $NVM_DIR/nvm.sh")
    
    env.PATH.append(f"{{root}}/versions/node/v{version}/bin")

import platform

if platform.system() == "Windows":
    build_command = "{root}\\build.bat"
