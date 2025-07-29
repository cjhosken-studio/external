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
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.FFmpeg_ROOT.set("{root}")
        env.FFmpeg_INCLUDE_DIR.set("{root}/include")
        env.FFmpeg_LIBRARY_DIR.set("{root}/lib")

        env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")


build_command = "{root}/build.sh"