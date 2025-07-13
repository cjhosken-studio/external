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
    ["vfxbase-2026", "gcc-14.2", "python-3.13"]
]

requires = [

]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.Boost_ROOT.set("{root}")
    env.Boost_INCLUDE_DIR.set("{root}/include")
    env.Boost_LIBRARY_DIR.set("{root}/lib64")