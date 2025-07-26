name = "vulkan"

version = "1.4.321.1"

authors = [
    "Khronos Group"
]

description = \
    """
    This is the Khronos OpenCL SDK. It brings together all the components needed to develop OpenCL applications:
    """

tools = [

]

variants = [
    ["studio_core-2026"]
]

requires = [

]

def commands():
    env.PATH.append("{root}/bin")
    
    env.CMAKE_MODULE_PATH.append("{root}/x86_64/lib/cmake")
    env.LD_LIBRARY_PATH.append("{root}/x86_64/lib")

    env.Vulkan_ROOT.set("{root}/x86_x64")
    env.Vulkan_INCLUDE_DIR.set("{root}/x86_64/include")
    env.Vulkan_LIBRARY_DIR.set("{root}/x86_64/lib")