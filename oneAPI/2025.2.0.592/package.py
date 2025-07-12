name= "oneapi"

version = "2025.2.0.592"

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
    
]

requires = [
    "glibc-2.28+"
]

build_command = """
chmod +x {root}/intel-oneapi-base-toolkit-2025.2.0.592.sh
{root}/intel-oneapi-base-toolkit-2025.2.0.592.sh -a --silent --eula accept --install-dir $REZ_BUILD_INSTALL_PATH
"""

def commands():
    env.PATH.prepend("{root}/bin")