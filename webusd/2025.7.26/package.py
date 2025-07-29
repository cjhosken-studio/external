name = "webusd"

version = "2025.7.26"

authors = [
    "Pixar Animation Studios",
    "Autodesk"
]

description = \
    """
    USD is a high-performance extensible software platform for collaboratively constructing animated 3D scenes, designed to meet the needs of large-scale film and visual effects production.
    WebUSD is an attempt at getting USD working on the web browser.
    """

tools = [
 
]

variants = [
    ["studio_core-2026"]
]

requires = [
    "git",
    "emscripten-4.0.8"
]

build_command = """
git clone --recursive https://github.com/autodesk-forks/USD.git webusd
cd webusd
git checkout 0bda600
git subdmoule update --init --recursive
python3 ./build_scripts/build_usd.py --build-target wasm --onetbb $REZ_BUILD_INSTALL_PATH
"""

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")

    env.WebUSD_DIR.set("{root}")
    env.webpxr_DIR.set("{root}")