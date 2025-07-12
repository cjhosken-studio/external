cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Boost
    URL https://github.com/boostorg/boost/releases/download/boost-${VERSION}/boost-${VERSION}-cmake.tar.gz
    PREFIX boost
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=17
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON

        -DBOOST_ENABLE_PYTHON=ON
        -DBOOST_ENABLE_MPI=OFF

)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Boost-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)