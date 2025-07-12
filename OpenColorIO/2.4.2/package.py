name = "opencolorio"

version = "2.4.2"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    OpenColorIO (OCIO) is a complete color management solution geared towards motion picture production with an emphasis on visual effects and computer animation. 
    OCIO provides a straightforward and consistent user experience across all supporting applications while allowing for sophisticated back-end configuration options suitable for high-end production usage. 
    OCIO is compatible with the Academy Color Encoding Specification (ACES) and is LUT-format agnostic, supporting many popular formats.    
    """



tools = [

]

requires = [
    "openexr-3.3.4",
    "python-3.11.5"
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.OpenColorIO_ROOT.set("{root}")
    env.OpenColorIO_INCLUDE_DIR.set("{root}/include")
    env.OpenColorIO_LIBRARY_DIR.set("{root}/lib64")