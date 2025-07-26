cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenCL
    GIT_REPOSITORY https://github.com/KhronosGroup/OpenCL-SDK.git
    GIT_TAG v${VERSION}
    PREFIX opencl
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON

        -DBUILD_TESTING=OFF
        -DBUILD_DOCS=OFF
        -DBUILD_EXAMPLEs=OFF
        -DBUILD_TEST=OFF
        -DOPENCL_SDK_BUILD_SAMPLES=OFF
        -DOPENCL_SDK_TEST_SAMPLES=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenCL-${VERSION} Install finished!\n\"
    )"
)