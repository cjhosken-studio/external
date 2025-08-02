name = "materialx"
version = "1.39.3"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    """

tools = [

]

variants = [
    ["studio_core-2025", "boost-1.85"],
    ["studio_core-2026", "boost-1.88"],
]

requires = [
    "imath-3+"
]

def commands():
    env.PATH.append("{root}/bin")
    
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.PYTHONPATH.append("{root}/python/site-packages")

    env.MaterialX_ROOT.set("{root}")
    env.MaterialX_INCLUDE_DIR.set("{root}/include")
    env.MaterialX_LIBRARY_DIR.set("{root}/lib")