CMAKE_MINIMUM_REQUIRED(VERSION 3.31.7)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] VFX-Platform-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)