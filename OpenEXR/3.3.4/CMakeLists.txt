cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenEXR
    URL https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX openexr
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON

        -DOPENEXR_CXX_STANDARD=17
        
        -DOPENEXR_USE_TBB=OFF
        -DBUILD_TESTING=OFF
        -DOPENEXR_BUILD_TOOLS=ON
        -DOPENEXR_INSTALL_TOOLS=ON
        -DOPENEXR_BUILD_EXAMPLES=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenEXR-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)