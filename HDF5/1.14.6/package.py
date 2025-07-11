name = "hdf5"

version = "1.14.6"

authors = [
    "The HDF Group"
]

description = \
    """
    HDF5 (Hierarchical Data Format version 5) is a file format, library, and software suite designed for storing and managing large, complex, and heterogeneous datasets, particularly in scientific and engineering fields. 
    It provides a way to organize and access data efficiently, with features like support for n-dimensional datasets, metadata storage, and parallel I/O.
    """

tools = [

]

requires = [
    "cmake-4.0.3",
]

def commands():
    env.PATH.append("{root}/bin")
    
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.HDF5_ROOT.set("{root}")
    env.HDF5_INCLUDE_DIR.set("{root}/include")
    env.HDF5_LIBRARY_DIR.set("{root}/lib")