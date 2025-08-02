# External

This repository contains a collection of external packages for the VFX / Animation pipeline. I've aimed to keep it up to date with the VFX Reference Platform (with other usefull packages included)


## Building and Install

These packages have been setup to build with rez. I've included a rez install script that you can use for getting started.


To build a package, dive inside until you're the same level as `package.py`. Then, run `rez build -i`. This will install the package into $HOME/packages


## The Studio
There's a certain package called "studio". This is the studio build and brings all compatible/required versions nicely into one package. Ideally, this would be used for software development and anything else that requires a full VFX eco-system.


## Packages

Alembic:
    - 1.8.8

Boost
    - 1.88.0

cmake
    - 3.31.8

CUDA
    - 12.9.1

Emscripten
    - 4.0.8

FBX
    - 2020.3.7

ffmpeg
    - 4.4.6

gcc
    - 14.2

git 
    - 2.50.1

Imath
    - 3.1.12

LLVM
    - 20.1.0

MaterialX
    - 1.39.3

nodejs
    - 22.17.1

oneAPI
    - 2025.2.0

OpenAssetIO
    - 1.0.0 (failing)

OpenCL
    - 2025.07.24

OpenColorIO
    - 2.4.2

OpenEXR
    - 3.3.4

OpenImageIO
    - 3.0.8.1

OpenSubdiv
    - 3.6.1

OpenTimelineIO
    - 0.17.0

OpenUSD
    - 25.05

OpenVDB
    - 12.0.1

Optix 
    - 9.0.0

OSL
    - 1.14.6.0 (failing)

Ptex
    - 2.4.3

pybind11
    - 3.0.0

Python
    - 3.13.5

Qt
    - 6.8.1

rez
    - 3.2.1

Studio
    - 2026

Vulkan
    - 1.4.321.1





## Build Order

There's quite alot of packages that need building. I've made a simple build order (mainly for the vfx ref platform)

Build Order:
0. rez
1. Cmake / python
2. GCC / cuda
3. studio_core
3. oneAPI / FBX / Boost / Qt / Pybind11 / Imath
4. Ptex / OpenVDB / OpenEXR / Alembic / OpenCL
5. OpenSubdiv / OpenColorIO
8. OpenImageIO
9. studio_vfxplatform
9. OpenUSD / OpenTimelineIO / OptiX
10. Then whatever else you want





## pip packages

rez is also used to install pip python packages

rez pip --python-version VERSION -i PACKAGE

PySide6
    - 6.8.1

PyQt6
    - 6.8.1

numpy
    - 1.26.4

PyOpenGL
    - 3.1.9

Jinja2
    - 3.1.6