name = "qt"

version = "6.5.3"

authors = [
    "Qt Group"
]

description = \
    """
    Qt is a cross-platform application development framework, primarily used for creating graphical user interfaces (GUIs) and applications that can run on various operating systems with little to no code changes.
    """

tools = [
    "androiddeployqt",
    "androiddeployqt6",
    "androidtestrunner",
    "assistant",
    "balsam",
    "balsamui",
    "canbusutil",
    "cooker",
    "designer",
    "instancer",
    "lconvert",
    "linguist",
    "lrelease",
    "lupdate",
    "materialeditor",
    "meshdebug",
    "pixeltool",
    "qdbus",
    "qdbuscpp2xml",
    "qdbusviewer",
    "qdbusxml2cpp",
    "qdistancefieldgenerator",
    "qmake",
    "qmake6",
    "qml",
    "qmldom",
    "qmleasing",
    "qmlformat",
    "qmllint",
    "qmlls",
    "qmlplugindump",
    "qmlpreview",
    "qmlprofiler",
    "qmlscene",
    "qmltc",
    "qmltestrunner",
    "qmltime",
    "qopcuaxmldatatypes2cpp",
    "qqem",
    "qsb",
    "qt-cmake",
    "qt-cmake-create",
    "qt-configure-module",
    "qtdiag",
    "qtdiag6",
    "qtpaths",
    "qtpaths6",
    "qtplugininfo",
    "shadergen",
    "shapegen",
    "svgtoqml"
]

variants = [
    ["studio_core-2025"]
]

requires = [
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")


    env.Qt_ROOT.set("{root}")
    env.Qt6_DIR.set("{root}")
    env.Qt6_ROOT.set("{root}")