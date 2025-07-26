name = "opentimelineio"

version = "3.6.1"

authors = [
    ""
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
    "git",
    "imath-3",
    "pybind11-3",
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64:{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.PYTHONPATH.append("{root}/python")



    env.OpenTimelineIO_ROOT.set("{root}")
    env.OpenTimelineIO_INCLUDE_DIR.set("{root}/include")
    env.OpenTimelineIO_LIBRARY_DIR.set("{root}/lib:{root}/lib64")