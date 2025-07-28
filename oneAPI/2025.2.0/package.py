name = "oneapi"

version = "2025.2.0"

authors = [
    "Intel"
]

description = \
    """
    Intel oneAPI is an open, standards-based programming model designed to simplify development for a variety of data-centric workloads across different hardware architectures like CPUs, GPUs, and FPGAs.
    """

build_command = \
    f"""
    wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/2d607ce3-9aa8-492d-a97d-e473dc37be66/intel-cpp-essentials-{version}.532_offline.sh
    sh ./intel-cpp-essentials-{version}.532_offline.sh -a -s --eula accept --action install --install-dir $REZ_BUILD_INSTALL_PATH
    rm -rf $HOME/intel
    """

def commands():
    import platform
    import os
    major_minor_version = "2025.2"

    if platform.system() == "Windows":
        env.PATH.prepend(f"{{root}}/{major_minor_version}/bin")

        env.oneAPI_ROOT.set(f"{{root}}/{major_minor_version}")
        env.oneAPI_INCLUDE_DIR.set(f"{{root}}/{major_minor_version}/include")
        env.oneAPI_LIBRARY_DIR.set(f"{{root}}/{major_minor_version}/lib")

    else:
        os.environ["PATH"] = f"{{root}}/{major_minor_version}/bin:" + os.environ.get("PATH")
        os.environ["LD_LIBRARY_PATH"] + f":{{root}}/{major_minor_version}/lib"


        os.environ["oneAPI_ROOT"] = f"{{root}}/{major_minor_version}"
        os.environ["oneAPI_INCLUDE_DIR"] = f"{{root}}/{major_minor_version}/include"
        os.environ["oneAPI_LIBRARY_DIR"] = f"{{root}}/{major_minor_version}/lib"

import platform

if platform.system() == "Windows":
    build_command = "{root}\\build.bat"
else:
    build_command = ""