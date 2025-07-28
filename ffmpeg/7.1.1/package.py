name = "ffmpeg"

version = "4.4.6"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.
    """

variants = [

]

tools = [
    "ffmpeg"
    "ffprobe"
]

requires = []

def commands():
    import platform

    if platform.system() == "Windows":
        env.PATH.prepend("{root}/bin")
    else:
        env.PATH.append("{root}/bin")
        env.LD_LIBRARY_PATH.append("{root}/lib")

        env.FFmpeg_ROOT.set("{root}")
        env.FFmpeg_INCLUDE_DIR.set("{root}/include")
        env.FFmpeg_LIBRARY_DIR.set("{root}/lib")

import platform

if platform.system() == "Windows":
    build_command = "{root}\\build.bat"
else:
    build_command = ""