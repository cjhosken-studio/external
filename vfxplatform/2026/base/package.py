name = "vfxbase"

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

]

build_command = ""

def commands():
    env.VFX_CXX_STANDARD.set(20)