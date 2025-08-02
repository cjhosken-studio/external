cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)
string(REPLACE "." "_" VERSION ${VERSION})

ExternalProject_Add(
    OpenSubdiv
    URL https://github.com/PixarAnimationStudios/OpenSubdiv/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX opensubdiv
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release

        -DNO_PTEX=ON
        -DPTEX_LOCATION=$ENV{Ptex_ROOT}

        -DNO_TBB=ON
        -DNO_OMP=ON

        -DNO_CUDA=ON
        -DCUDA_TOOLKIT_ROOT_DIR=$ENV{CUDA_ROOT}

        -DNO_OPENCL=ON
        -DNO_CLEW=ON
        -DNO_OPENGL=OFF
        -DNO_METAL=ON
    
        -DNO_DOC=ON
        -DNO_EXAMPLES=ON
        -DNO_TUTORIALS=ON
        -DNO_REGRESSION=ON
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenSubdiv-${VERSION} Install finished!\n\"
    )"
)