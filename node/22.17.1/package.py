name = "node"

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

def commands():
    env.NVM_DIR.set("{root}")

def post_commands():
    command("source $NVM_DIR/nvm.sh")

build_command = "{root}/build.sh"
