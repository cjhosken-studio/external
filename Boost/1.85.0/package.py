name = "boost"

version = "1.85.0"

authors = [
    "Boost"
]

description = \
    """
    Boost is a collection of high-quality and peer-reviewed libraries that aims to make C++ development highly productive.
    """

tools = [

]

variants = [
    ["python-3.11+"]
]

requires = [
    "cmake-3.31.7+",
    "gcc-11.2.0+"
]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.BOOST_ROOT.set("{root}")
    env.Boost_ROOT.set("{root}")