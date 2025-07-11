cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Imath
    URL https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX imath
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON

        -DBoost_ROOT=$ENV{Boost_ROOT}
        -DPYTHON=ON
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Imath-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)