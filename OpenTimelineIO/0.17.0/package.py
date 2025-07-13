name = "opentimelineio"

version = "0.17.0"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    OpenTimelineIO is an interchange format and API for editorial cut information. OTIO contains information about the order and length of cuts and references to external media.    
    """

tools = [

]

variants = [
    ["vfxbase-2026", "gcc-14.2", "python-3.13"],
]

requires = [
    "imath",
    "pybind11"
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")

    env.OpenTimelineIO_ROOT.set("{root}")
    env.OpenTimelineIO_INCLUDE_DIR.set("{root}/include")
    env.OpenTimelineIO_LIBRARY_DIR.set("{root}/lib")
    
