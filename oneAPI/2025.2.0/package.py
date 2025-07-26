name = "oneapi"

version = "2025.2.0"

authors = [
    "Intel"
]

description = \
    """
    Intel oneAPI is an open, standards-based programming model designed to simplify development for a variety of data-centric workloads across different hardware architectures like CPUs, GPUs, and FPGAs.
    """

tools = [

]

variants = [
    ["studio_core-2026"],
]

requires = [

]

build_command = \
    f"""
    wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/2d607ce3-9aa8-492d-a97d-e473dc37be66/intel-cpp-essentials-{version}.532_offline.sh
    sh ./intel-cpp-essentials-{version}.532_offline.sh -a -s --eula accept --action install --install-dir $REZ_BUILD_INSTALL_PATH
    rm -rf $HOME/intel
    """

def commands():
    major_minor_version = "2025.2"

    env.PATH.prepend(f"{{root}}/{major_minor_version}/bin")
    env.LD_LIBRARY_PATH.append(f"{{root}}/{major_minor_version}/lib")

    env.oneAPI_ROOT.set(f"{{root}}/{major_minor_version}")
    env.oneAPI_INCLUDE_DIR.set(f"{{root}}/{major_minor_version}/include")
    env.oneAPI_LIBRARY_DIR.set(f"{{root}}/{major_minor_version}/lib")

