name = "onetbb"

version = "2022.2.0"

authors = [
    "UXL Foundation"
]

description = \
    """
    oneTBB is a flexible C++ library that simplifies the work of adding parallelism to complex applications, even if you are not a threading expert.
    """

tools = [

]

requires = [
    "cmake-4.0.3"
]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.oneTBB_ROOT.set("{root}")
    env.oneTBB_INCLUDE_DIR.set("{root}/include")
    env.oneTBB_LIBRARY_DIR.set("{root}/lib64")