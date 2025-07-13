name = "embree"

version = "4.4.0"

authors = [
    "Intel",
    "RenderKit"
]

description = \
    """
    Intel® Embree is a high-performance ray tracing library developed at Intel, which is released as open source under the Apache 2.0 license. 
    Intel® Embree supports x86 CPUs under Linux, macOS, and Windows; ARM CPUs on Linux and macOS; as well as Intel® GPUs under Linux and Windows.
    """

tools = [
    "embree_buildbench",
    "embree_bvh_access",
    "embree_bvh_builder",
    "embree_closest_point",
    "embree_collide",
    "embree_convert",
    "embree_curve_geometry",
    "embree_displacement_geometry",
    "embree_dynamic_scene",
    "embree_forest",
    "embree_grid_geometry",
    "embree_hair_geometry",
    "embree_host_device_memory",
    "embree_info",
    "embree_instanced_geometry",
    "embree_interpolation",
    "embree_intersection_filter",
    "embree_lazy_geometry",
    "embree_minimal",
    "embree_motion_blur_geometry",
    "embree_multiscene_geometry",
    "embree_next_hit",
    "embree_pathtracer",
    "embree_point_geometry",
    "embree_quaternion_motion_blur",
    "embree_ray_mask",
    "embree_subdivision_geometry",
    "embree_tests",
    "embree_triangle_geometry",
    "embree_user_geometry",
    "embree_verify",
    "embree_viewer",
    "embree_voronoi",
]

variants = [
    ["vfxbase-2026", "gcc-14.2"],
]

requires = [

]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.Embree_ROOT.set("{root}")
    env.Embree_INCLUDE_DIR.set("{root}/include")
    env.Embree_LIBRARY_DIR.set("{root}/lib64")
    
