name= "oneapi"

version = "2025.2"

authors = [
    "Intel"
]

description = \
    """
    oneAPI provides a comprehensive set of libraries, open source repositories, SYCL-based C++ language extensions, and optimized reference implementations to accelerate the following goals:
     - Define a common, unified, and open multiarchitecture and multivendor software platform.
     - Ensure functional code portability and performance portability across hardware vendors and accelerator technologies.
     - Enable an extensive set of specifications and library APIs to cover programming domain needs across industries and compute as well as AI use cases.
     - Meet the needs of modern software applications that merge high-end computational needs and AI.
     - Provide a developer community and open forum to drive a unified API for a unified industry-wide multiarchitecture software development platform.
     - Encourage ecosystem collaboration on the oneAPI specification and compatible oneAPI implementations.
    """

tools = [
    "aocl-ioc64",
    "c2s",
    "codepin-report.py",
    "compiler",
    "cpuinfo",
    "dpcpp",
    "dpcpp-cl",
    "dpct",
    "fi_info",
    "fi_pingpong",
    "gdb-oneapi",
    "gdbserver",
    "gdbserver-32",
    "gdbserver-ze",
    "hydra_bstrap_proxy",
    "hydra_nameserver",
    "hydra_pmi_proxy",
    "icpx",
    "icpx.cfg",
    "icx",
    "icx.cfg",
    "icx-cc",
    "icx-cl",
    "IMB-MPI1",
    "IMB-MPI1-GPU",
    "IMB-MT",
    "IMB-NBC",
    "IMB-P2P",
    "IMB-RMA",
    "IMB-RMA-GPU",
    "impi_cpuinfo",
    "impi_info",
    "install-eclipse-plugins.sh",
    "intercept-build",
    "ioc64",
    "mkl_link_tool",
    "mpicc",
    "mpicxx",
    "mpiexec",
    "mpiexec.hydra",
    "mpif77",
    "mpif90",
    "mpifc",
    "mpigcc",
    "mpigxx",
    "mpiicc",
    "mpiicpc",
    "mpiicpx",
    "mpiicx",
    "mpiifort",
    "mpiifx",
    "mpirun",
    "mpitune_fast",
    "oneapi-cli",
    "opencl-aot",
    "run-clang-tidy",
    "sycl-ls",
    "sycl-trace"
]

variants = [
    ["vfxbase-2026", "gcc-14.2"],
    #["vfxbase-2026"],
]

requires = []

build_command = """
chmod +x {root}/intel-oneapi-base-toolkit-2025.2.0.592.sh
{root}/intel-oneapi-base-toolkit-2025.2.0.592.sh -a --silent --eula accept --install-dir $REZ_BUILD_INSTALL_PATH
"""

def commands():
    env.PATH.prepend("{root}/2025.2/bin")
    env.oneAPI_ROOT.set("{root}")

    env.tbb_ROOT.set("{root}/tbb/latest")
    env.tbb_INCLUDE_DIR.set("{root}/tbb/latest/include")
    env.tbb_LIBRARY_DIR.set("{root}/tbb/latest/lib")

    env.mpi_ROOT.set("{root}/mpi/latest")
    env.mpi_INCLUDE_DIR.set("{root}/mpi/latest/include")
    env.mpi_LIBRARY_DIR.set("{root}/mpi/latest/lib")

    env.mkl_ROOT.set("{root}/mkl/latest")
    env.mkl_INCLUDE_DIR.set("{root}/mkl/latest/include")
    env.mkl_LIBRARY_DIR.set("{root}/mkl/latest/lib")



