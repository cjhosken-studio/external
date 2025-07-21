
Current Issues:

- OpenEXR 3.4 has not been released yet. This means OCOIO and OIIO cannot be built as well. For the time being OpenEXR is 3.3.4

- OpenVDB 13 has not been released yet. For the time being OpenVDB is 12.0.1


Build Order:

1. Cmake / python
2. GCC / cuda
3. studio_core
3. oneAPI / FBX / Boost / Qt / Pybind11 / Imath
4. Ptex / OpenVDB / OpenEXR / Alembic
5. OpenSubdiv / OpenColorIO
8. OpenImageIO
9. studio_vfxplatform
9. OpenUSD / OpenTimelineIO / OptiX




Extra thingies:

CUDA needs properly linking to OpenSubdiv

- LLVM?
- OSL

- Vulkan?
- OpenCL?
- OpenGL?
- Emscripten?


PYTHON MODULES:
- TensorFlow/PyTorch
- OpenCV