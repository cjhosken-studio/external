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
    "ocioacrhive",
    "ociobakelut",
    "ociocheck",
    "ociochecklut",
    "ocioconvert",
    "ociopuinfo",
    "ociodisplay",
    "ociolutimage",
    "ociomakeclf",
    "ocioperf",
    "ociowrite"
]

variants = [
    ["studio_core-2026"], # OpenEXR should be 3.4
]

requires = [
    "openexr-3+",
    
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.PYTHONPATH.append("{root}/lib64/python3.13/site-packages")

    env.OpenColorIO_ROOT.set("{root}")
    env.OpenColorIO_INCLUDE_DIR.set("{root}/include")
    env.OpenColorIO_LIBRARY_DIR.set("{root}/lib64")