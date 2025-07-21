cmake_minimum_required(VERSION 3.31.8)
include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

# Clone and install properly
ExternalProject_Add(
    OpenTimelineIO
    GIT_REPOSITORY https://github.com/AcademySoftwareFoundation/OpenTimelineIO.git
    GIT_TAG v${VERSION}
    PREFIX otio
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS 
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DOTIO_PYTHON_INSTALL=ON
        -DOTIO_DEPENDENCIES_INSTALL=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenTimelineIO-${VERSION} Install finished!\n\"
    )"
)