# External Packages

This repository contains a collection of **external packages** for the VFX / Animation pipeline.  
It is designed to stay aligned with the **VFX Reference Platform**, with additional useful packages included.

---

## 🚀 Building & Installing

These packages are setup to build with **Rez**. A Rez install script is included to help you get started.

To build a package:

1. Navigate to the folder containing `package.py`.
2. Run:

```bash
rez build -i
```

## 🎬 The Studio Package

There is a special package called studio, which aggregates all compatible and required versions into a single package.
Use this for:

- Software development
- Full VFX ecosystem testing
- Any workflow that requires a complete VFX environment

## 📦 Packages
| Package        | Latest Version     |
| -------------- | ------------------ |
| Alembic        | 1.8.8              |
| Boost          | 1.88.0             |
| CMake          | 3.31.8             |
| CUDA           | 12.9.1             |
| Emscripten     | 4.0.8              |
| FBX            | 2020.3.7           |
| FFmpeg         | 4.4.6              |
| GCC            | 14.2               |
| Git            | 2.50.1             |
| Imath          | 3.1.12             |
| LLVM           | 20.1.0             |
| MaterialX      | 1.39.3             |
| NodeJS         | 22.17.1            |
| oneAPI         | 2025.2.0           |
| OpenAssetIO    | 1.0.0 (failing)    |
| OpenCL         | 2025.07.24         |
| OpenColorIO    | 2.4.2              |
| OpenEXR        | 3.3.4              |
| OpenImageIO    | 3.0.8.1            |
| OpenSubdiv     | 3.6.1              |
| OpenTimelineIO | 0.17.0             |
| OpenUSD        | 25.05              |
| OpenVDB        | 12.0.1             |
| Optix          | 9.0.0              |
| OSL            | 1.14.6.0 (failing) |
| Ptex           | 2.4.3              |
| pybind11       | 3.0.0              |
| Python         | 3.13.5             |
| Qt             | 6.8.1              |
| Rez            | 3.2.1              |
| Studio         | 2026               |
| Vulkan         | 1.4.321.1          |


## 🔧 Build Order

Some packages depend on others, so a recommended build order is:

0. rez

1. CMake / Python

2. GCC / CUDA

3. studio_core

4. oneAPI / FBX / Boost / Qt / Pybind11 / Imath

5. Ptex / OpenVDB / OpenEXR / Alembic / OpenCL

6. OpenSubdiv / OpenColorIO

7. OpenImageIO

8. studio_vfxplatform

9. OpenUSD / OpenTimelineIO / OptiX

10. All other packages

    This order is mainly aligned with the VFX Reference Platform.


## 🐍 Pip Packages

Rez can also be used to install Python pip packages:
```bash
rez pip --python-version VERSION -i PACKAGE
```

| Package  | Latest Version |
| -------- | ------- |
| PySide6  | 6.8.1   |
| PyQt6    | 6.8.1   |
| numpy    | 1.26.4  |
| PyOpenGL | 3.1.9   |
| Jinja2   | 3.1.6   |

## 🛠 Maintenance
This repository is maintained by [Christopher Hosken](https://cjhosken.github.io)