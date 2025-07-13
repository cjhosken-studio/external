name = "alembic"

version = "1.8.8"

authors = [
    "Sont Pictures Imageworks",
    "Lucasfilm"
]

description = \
    """
    Alembic is an open computer graphics interchange framework. Alembic distills complex, animated scenes into a non-procedural, application-independent set of baked geometric results. 
    This distillation of scenes into baked geometry is exactly analogous to the distillation of lighting and rendering scenes into rendered image data.
    """

tools = [

]

variants = [
    ["vfxbase-2026", "gcc-14.2", "python-3.13", "boost-1.88"],
]

requires = [

]

def commands():
    env.PATH.append("{root}/bin")
    
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    env.Alembic_ROOT.set("{root}")
    env.Alembic_INCLUDE_DIR.set("{root}/include")
    env.Alembic_LIBRARY_DIR.set("{root}/lib64")