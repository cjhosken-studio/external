cmake_minimum_required(VERSION 3.31.7)

include(ExternalProject)

# Versions
get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(glibc
  URL https://ftp.gnu.org/gnu/glibc/glibc-${VERSION}.tar.gz
  PREFIX glibc
  INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
  CONFIGURE_COMMAND
    <SOURCE_DIR>/configure
    CC=$ENV{CC} 
    --prefix=<INSTALL_DIR>
  BUILD_COMMAND make -j ${nproc}
  BUILD_IN_SOURCE 0
  INSTALL_COMMAND make install
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] glibc-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)