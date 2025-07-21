# @studio/platform-2026/package.py

name = "studio_vfxplatform"
version = "2026.0"

description = \
    """
    studio_vfxplatform is a wrapper for all packages that meet the current VFX Reference Platform specifications.
    """

variants = [
    ["platform-linux", "arch-x86_64"]
]

requires = [
    "studio_core-2026", # GCC setup is done in here.
    "python-3.13",
    "qt-6.8",
    "openexr-3.3+",
    "ptex-2.4",
    "opensubdiv-3.6",
    "openvdb-12+",
    "alembic-1.8",
    "fbx-2020.2+",
    "opencolorio-2.4", # ACES 2.0.0
    "boost-1.88",
    "oneapi-2025"
]

build_command = ""

def commands():
    env.VFXPLATFORM_VERSION = "2026"