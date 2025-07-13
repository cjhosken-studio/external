cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

# Set up build and install directories
set(BUILD_DIR ${CMAKE_CURRENT_BINARY_DIR}/imath-build)
set(INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH})

ExternalProject_Add(
    Imath
    URL https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX imath
    # Use separate build directory
    BINARY_DIR ${BUILD_DIR}
    INSTALL_DIR ${INSTALL_DIR}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=$ENV{VFX_CXX_STANDARD}
        -DCMAKE_BUILD_TYPE=Release

    # These steps replicate the standard CMake process
    CONFIGURE_COMMAND ${CMAKE_COMMAND} <SOURCE_DIR> 
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=$ENV{VFX_CXX_STANDARD}
        -DCMAKE_BUILD_TYPE=Release
        -DPYTHON=ON

        -DCMAKE_POSITION_INDEPENDENT_CODE=ON  # Proper way to enable PIC
        -DBoost_ROOT=$ENV{Boost_ROOT}
        -B <BINARY_DIR>
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR> --config Release
    INSTALL_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR> --target install --config Release
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Imath-${VERSION} Install finished!\n\"
    )"
)