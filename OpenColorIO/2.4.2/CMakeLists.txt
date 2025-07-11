cmake_minimum_required(VERSION 4.0.3)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenColorIO
    URL https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/refs/tags/v${VERSION}.tar.gz
    PREFIX opencolorio
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_CXX_STANDARD=17
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON
        


        -DPython_EXECUTABLE=$ENV{Python_EXECUTABLE}

        -DOCIO_INSTALL_EXT_PACKAGES=MISSING

        -DOCIO_BUILD_APPS=ON
        -DOCIO_USE_OIIO_FOR_APPS=OFF # More file formats than with OpenEXR, but we'd rather have OCIO with OIIO than OIIO with OCIO
        -DOCIO_BUILD_PYTHON=ON

        -DOCIO_BUILD_TESTS=OFF
        -DOCIO_BUILD_GPU_TESTS=OFF
        -DOCIO_BUILD_DOCS=OFF
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenColorIO-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)