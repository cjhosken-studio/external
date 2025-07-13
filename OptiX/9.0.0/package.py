name = "optix"

version = "9.0.0"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    An application framework for achieving optimal ray tracing performance on the GPU. It provides a simple, recursive, and flexible pipeline for accelerating ray tracing algorithms. Bring the power of NVIDIA GPUs to your ray tracing applications with programmable intersection, ray generation, and shading.
    """

tools = [

]

variants = [
    ["vfxbase-2025"],
]

requires = [
    "cmake-3.31.7+",
]

def commands():
    env.OptiX_ROOT.set("{root}")
    env.OptiX_INCLUDE_DIR.set("{root}/include")