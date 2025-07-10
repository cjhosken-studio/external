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
    "cmake-4.0.3",
    "openexr-3.3.4",
    "openimageio-2.4.17.0",
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.OpenColorIO_ROOT.append("{root}")