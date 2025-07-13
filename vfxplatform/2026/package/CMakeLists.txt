CMAKE_MINIMUM_REQUIRED(VERSION 3.31.7)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] VFX-Platform-2026 PACKAGE SETUP FINISHED!\n\"
    )"
)