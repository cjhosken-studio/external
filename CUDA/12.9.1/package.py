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
    import platform
    import os

    if platform.system() == "Windows":
        cuda_root = "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v12.9"
        os.environ["PATH"] = f"{cuda_root}\\bin;" + os.environ.get("PATH")
        os.environ["LD_LIBRARY_PATH"] += f";{cuda_root}\\lib\\x64"

        
        os.environ["CUDA_ROOT"] = cuda_root
        os.environ["CUDA_INCLUDE_DIR"] = f"{cuda_root}\\include"
        os.environ["CUDA_LIBRARY_DIR"] = f"{cuda_root}\\lib\\x64"
        os.environ["CMAKE_MODULE_PATH"] += f";{cuda_root}\\lib\\cmake"

    else:
        os.environ["PATH"] = "{root}/bin:" + os.environ.get("PATH")
        os.environ["LD_LIBRARY_PATH"] += ":{root}/lib64"
        os.environ["CMAKE_MODULE_PATH"] += ":{root}/lib64/cmake"

        os.environ["CUDA_ROOT"] = "{root}"
        os.environ["CUDA_INCLUDE_DIR"] = "{root}/include"
        os.environ["CUDA_LIBRARY_DIR"] = "{root}/lib64"
    
import platform

if platform.system() == "Windows":
    build_command = "{root}\\build.bat"
else:
    installer = f"cuda_{version}_575.57.08_linux.run"

    build_command = f"""
    wget https://developer.download.nvidia.com/compute/cuda/{version}/local_installers/{installer}
    sh ./{installer} --silent --toolkit --defaultroot=$REZ_BUILD_INSTALL_PATH --toolkitpath=$REZ_BUILD_INSTALL_PATH
    """