name = "imath"

version = "3.1.12"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    """

tools = [

]

variants = [
    ["studio_core-2026"],
]

requires = [
    "boost-1.88"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.PYTHONPATH.append("{root}/lib/python3.13/site-packages")

    env.Imath_ROOT.set("{root}")
    env.Imath_INCLUDE_DIR.set("{root}/include:{root}/include/Imath")
    env.Imath_LIBRARY_DIR.set("{root}/lib64")
    
