name = "materialx"

version = "1.39.3"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    MaterialX is an open standard for representing rich material and look-development content in computer graphics, enabling its platform-independent description and exchange across applications and renderers.
    """

tools = [

]

requires = [
    "python-3.11.11+",
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")

    env.MaterialX_ROOT.set("{root}")
    env.MaterialX_INCLUDE_DIR.set("{root}/include")
    env.MaterialX_LIBRARY_DIR.set("{root}/lib")
    
