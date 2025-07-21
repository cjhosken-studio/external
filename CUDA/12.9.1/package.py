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

installer = f"cuda_{version}_575.57.08_linux.run"

build_command = f"""
wget https://developer.download.nvidia.com/compute/cuda/{version}/local_installers/{installer}
sh ./{installer} --silent --toolkit --defaultroot=$REZ_BUILD_INSTALL_PATH --toolkitpath=$REZ_BUILD_INSTALL_PATH
"""

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.CUDA_ROOT.set("{root}")
    env.CUDA_INCLUDE_DIR.set("{root}/include")
    env.CUDA_LIBRARY_DIR.set("{root}/lib64")
    