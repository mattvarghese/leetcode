from setuptools import Extension, setup

setup(
    name="custom_math",
    version="1.0",
    description="Python wrapper for C factorial function",
    ext_modules=[Extension("custom_math", sources=["mathmodule.c"])],
)
