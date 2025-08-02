name = "rust"

version = "1.88.0"

authors = [
    "Forge"
]

description = \
    """
    The gcc package contains the GNU Compiler Collection version 4.8.
    You'll need this package in order to compile C code.
    """

tools = [
    "cargo",
    "cargo-clippy",
    "cargo-fmt",
    "clippy-driver",
    "rust-analyzer",
    "rustc",
    "rustdoc",
    "rustfmt",
    "rust-gdb",
    "rust-gdbgui",
    "rust-lldb"
]

requires = [    
]

variants = [

]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.RUST_ROOT.set("{root}")

build_command = "{root}/build.sh"