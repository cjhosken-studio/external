name = "oneapi"

version = "2025.2.0"

authors = [
    "Intel"
]

description = \
    """
    Intel oneAPI is an open, standards-based programming model designed to simplify development for a variety of data-centric workloads across different hardware architectures like CPUs, GPUs, and FPGAs.
    """

def commands():
    maj, mnr = f"{version}".split('.')[0:2]
    major_minor = f"{maj}.{mnr}"

    env.PATH.prepend(f"{{root}}/{major_minor}/bin")
    env.LD_LIBRARY_PATH.append(f"{{root}}/{major_minor}/lib")

    if building:
        env.oneAPI_ROOT.set(f"{{root}}/{major_minor}")
        env.oneAPI_INCLUDE_DIR.set(f"{{root}}/{major_minor}/include")
        env.oneAPI_LIBRARY_DIR.set(f"{{root}}/{major_minor}/lib")


build_command = "{root}/build.sh"