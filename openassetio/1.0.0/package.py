name = "openassetio"
version = "1.0.0"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    An open-source interoperability standard for tools and content management systems used in media production.
    It aims to reduce the integration effort and maintenance overhead of modern CGI pipelines, and pioneer new, standardized asset-centric workflows in content creation tooling.
    """

tools = [

]

variants = [
    ["studio_core-2025"],
    ["studio_core-2026"],
]

requires = [
    "pybind11"
]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.OpenAssetIO_ROOT.set("{root}")
    env.OpenAssetIO_INCLUDE_DIR.set("{root}/include")
    env.OpenAssetIO_LIBRARY_DIR.set("{root}/lib")