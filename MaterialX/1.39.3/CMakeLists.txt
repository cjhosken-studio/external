cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    MaterialX
    GIT_REPOSITORY https://github.com/AcademySoftwareFoundation/MaterialX.git
    GIT_TAG v${VERSION}
    GIT_SHALLOW FALSE
    GIT_SUBMODULES_RECURSIVE TRUE
    PREFIX materialx
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_CXX_STANDARD=$ENV{VFX_CXX_STANDARD}
        -DBUILD_SHARED_LIBS=ON



        -DMATERIALX_BUILD_PYTHON=ON
        -DMATERIALX_BUILD_VIEWER=ON

        -DMATERIALX_BUILD_OIIO=ON
        -DMATERIALX_OIIO_DIR=$ENV{OpenImageIO_ROOT}

        -DMATERIALX_PYTHON_VERSION=3
        -DMATERIALX_PYTHON_EXECUTABLE=$ENV{Python_EXECUTABLE}

        -DMATERIALX_PYTHON_OCIO_DIR=$ENV{OpenColorIO_ROOT}
        -DMATERIALX_PYBIND11_DIR=$ENV{pybind11_ROOT}
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] MaterialX-${VERSION} Install finished!\n\"
    )"
)