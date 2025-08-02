# @studio/platform-2025/package.py

name = "studio_vfxplatform"
version = "2025.0"

description = \
    """
    studio_vfxplatform is a wrapper for all packages that meet the current VFX Reference Platform specifications.
    """

variants = [

]

requires = [
    "studio_core-2025", # GCC setup and python is done in here.
    "qt-6.5",
    "openexr-3.3",
    "ptex-2.4",
    "opensubdiv-3.6",
    #"openvdb-12", gcc version too low :(
    "alembic-1.8",
    "fbx-2020.2+",
    "opencolorio-2.4", # ACES 2.0.0
    "boost-1.85",
    "oneapi-2025"
]

build_command = ""

def commands():
    env.VFXPLATFORM_VERSION = "2026"