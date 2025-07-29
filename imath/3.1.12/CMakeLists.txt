cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Imath
    URL https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX imath
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND python3 -m pip install numpy==1.26.4
    BUILD_IN_SOURCE 1
    BUILD_COMMAND
        mkdir -p build &&
        cd build &&
        cmake
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON
        -DPYTHON=ON
        -DBUILD_TESTING=OFF
        ..

    INSTALL_COMMAND 
        cd build &&
        make install -j
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Imath-${VERSION} Install finished!\n\"
    )"
)