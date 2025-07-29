name = "cuda"

version = "12.9.1"

authors = [
    "NVIDIA"
]

description = \
    """
    CUDA is a parallel computing platform and programming model created by NVIDIA. With more than 20 million downloads to date, CUDA helps developers speed up their applications by harnessing the power of GPU accelerators. 
    """

tools = [
    "bin2c",
    "computeprof",
    "compute-sanitizer",
    "cudafe++",
    "cuda-gdb",
    "cuda-gdb-minimal",
    "cuda-gdbserver",
    "cu++filt",
    "cuobjdump",
    "fatbinary",
    "ncu",
    "ncu-ui",
    "nsight-sys",
    "nsys",
    "nsys-ui",
    "nvcc",
    "nvdisasm",
    "nvlink",
    "nvprof",
    "nvprune",
    "nvvp",
    "ptxas"
]

requires = []

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.set("{root}/lib64")

    if building:      
        env.CUDA_ROOT.set("{root}")
        env.CUDA_INCLUDE_DIR.set("{root}/include")
        env.CUDA_LIBRARY_DIR.set("{root}/lib64/")
        env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
        env.PKG_CONFIG_PATH.prepend("{root}/pkgconfig")

build_command = "{root}/build.sh"