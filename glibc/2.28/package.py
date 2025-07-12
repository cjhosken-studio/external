name = "glibc"

version = "2.28"

authors = [
    "GNU"
]

description = \
    """
    The GNU C Library - The project provides the core libraries for the GNU system and GNU/Linux systems, as well as many other systems that use Linux as the kernel. 
    These libraries provide critical APIs including ISO C11, POSIX.1-2008, BSD, OS-specific APIs and more. 
    These APIs include such foundational facilities as open, read, write, malloc, printf, getaddrinfo, dlopen, pthread_create, crypt, login, exit and more.
    """

tools = [

]

requires = [
    "cmake-3.31.7+",
    "gcc-11.2.0+"
]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.LIBRARY_PATH.prepend("{root}/lib")

