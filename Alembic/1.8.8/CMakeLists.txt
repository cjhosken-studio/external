cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    Alembic
    URL https://github.com/alembic/alembic/archive/refs/tags/${VERSION}.tar.gz
    PREFIX alembic
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=17
        -DCMAKE_BUILD_TYPE=Release
        -DALEMBIC_SHARED_LIBS=ON

        -DImath_ROOT=$ENV{Imath_ROOT}
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Alembic-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)