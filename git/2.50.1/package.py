name = "git"

version = "2.50.1"

authors = [
    "Linus Torvalds",
    "Junio Hamano"
]

description = \
    """
    Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
    """

tools = [
    "git",
    "git-cvsserver",
    "git-recieve-pack",
    "git-upload-pack",
    "git-shell",
    "git-upload-archive"
]

requires = []

def commands():
    import platform

    if platform.system() == "Windows":
        env.PATH.prepend("{root}")
        env.PATH.prepend("{root}/bin")
    else:
        env.PATH.prepend("{root}/bin")
        env.GIT_EXEC_PATH = "{root}/libexec/git-core"
        env.GIT_TEMPLATE_DIR = "{root}/share/git-core/templates"
        
        env.LD_LIBRARY_PATH.append("{root}/lib")

        
        # Set man pages path
        env.MANPATH.prepend("{root}/share/man")

import platform

if platform.system() == "Windows":
    build_command="{root}\\build.bat"
else:
    build_command="{root}"