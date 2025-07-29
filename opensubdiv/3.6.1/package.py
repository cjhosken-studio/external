name = "opensubdiv"

version = "3.6.1"

authors = [
    "Pixar Animation Studios"
]

description = \
    """
    OpenSubdiv is a set of open source libraries that implement high performance subdivision surface (subdiv) evaluation on massively parallel CPU and GPU architectures. 
    This codepath is optimized for drawing deforming subdivs with static topology at interactive framerates. 
    The resulting limit surface matches Pixar's Renderman to numerical precision.
    """

tools = [

]

variants = [
    ["studio_core-2026"],
]

requires = [
    "ptex-2.4",
    "cuda-12.9",
    "opencl-2025",
    "oneapi-2025"
]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.OpenSubdiv_ROOT.set("{root}")
    env.OpenSubdiv_INCLUDE_DIR.set("{root}/include")
    env.OpenSubdiv_LIBRARY_DIR.set("{root}/lib")