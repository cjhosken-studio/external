name = "pybind11"

version = "3.0.0"

authors = [
    "Wenzel Jakob"
]

description = \
    """
    pybind11 is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code. Its goals and syntax are similar to the excellent Boost.Python library by David Abrahams: to minimize boilerplate code in traditional extension modules by inferring type information using compile-time introspection.
    """

tools = [

]

variants = [
    ["vfxbase-2026", "gcc-14.2", "python-3.13"],
]


def commands():    
    env.CMAKE_MODULE_PATH.append("{root}/share/cmake")

    env.pybind11_ROOT.set("{root}")
    env.pybind11_INCLUDE_DIR.set("{root}/include")