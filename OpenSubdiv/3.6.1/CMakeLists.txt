cmake_minimum_required(VERSION 4.0.3)

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
        -DCMAKE_CXX_STANDARD=17
        -DCMAKE_BUILD_TYPE=Release

        -DNO_PTEX=ON
        -DNO_TBB=ON
        -DNO_OMP=ON

        -DNO_CUDA=OFF
        -DNO_OPENCL=OFF
        -DNO_CLEW=OFF
        -DNO_OPENGL=OFF
        -DNO_METAL=OFF
    
        -DNO_DOC=ON
        -DNO_EXAMPLES=ON
        -DNO_TUTORIALS=ON
        -DNO_REGRESSION=ON
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenSubdiv-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)