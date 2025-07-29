name = "usd"

version = "25.05"

authors = [
    "Pixar Animation Studios"
]

description = \
    """
    USD is a high-performance extensible software platform for collaboratively constructing animated 3D scenes, designed to meet the needs of large-scale film and visual effects production.
    """

tools = [
 
]

variants = [
    ["studio_core-2026"]
]

requires = [
    "opensubdiv-3.6",
    "boost-1.88",
    "oneapi-2025",
    "materialx-1.39",
    "openimageio-3",
    "opencolorio-2.4",
    "ptex-2.4",
    "alembic-1.8"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")

    env.USD_DIR.set("{root}")
    env.pxr_DIR.set("{root}")