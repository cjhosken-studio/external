name = "vfxplatform"

version = "2026"

authors = [
    "Visual Effects Society (VES) Technology Committee"
]

description = \
    """
    The VFX Reference Platform is a set of tool and library versions to be used as a common target platform for building software for the VFX industry. 
    Its purpose is to minimise incompatibilities between different software packages, ease the support burden for integrated pipelines and encourage further adoption of Linux by both studios and software vendors. 
    The Reference Platform is updated annually by a group of software vendors in collaboration with the Visual Effects Society Technology Committee.
    """

tools = [

]

requires = [
    "cmake-3.31.7+",
    "gcc-14.2+",
    "glibc-2.34+",
    "python-3.13+",
    "qt-6.8+",
    "openexr-3.4+",
    "ptex-2.4+",
    "opensubdiv-3.6+",
    "openvdb-13+"
    "alembic-1.8+",
    "fbx-2020.3+"
    "opencolorio-2.4+",
    "boost-1.88+",
    "openapi-2025+" # move to oneAPI as it includes oneTBB and oneMKL
]

def commands():
    pass