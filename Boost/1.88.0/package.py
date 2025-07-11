name = "boost"

version = "1.88.0"

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
    ["python-3.13.5"]
]

requires = [
    "cmake-4.0.3",
]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.BOOST_ROOT.set("{root}")
    env.Boost_ROOT.set("{root}")