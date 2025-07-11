name = "imath"

version = "3.1.12"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    Imath is a basic, light-weight, and efficient C++ representation of 2D and 3D vectors and matrices and other simple but useful mathematical objects, functions, and data types common in computer graphics applications, including the “half” 16-bit floating-point type.
    Imath also includes optional python bindings for all types and functions, including optimized implementations of vector and matrix arrays.
    """

tools = [

]

requires = [
    "cmake-4.0.3",
    "boost-1.88.0"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.Imath_ROOT.set("{root}")
    env.Imath_INCLUDE_DIR.set("{root}/include")
    env.Imath_LIBRARY_DIR.set("{root}/lib64")
    
