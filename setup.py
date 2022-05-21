import os

from setuptools import Extension, find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    long_description = f.read()

setup(
    name="geprofiler",
    packages=find_packages(include=["geprofiler", "geprofiler.*"]),
    version="1.0.8",
    ext_modules=[
        Extension(
            "geprofiler.low_level.stat_profile",
            sources=["geprofiler/low_level/stat_profile.c"],
        )
    ],
    description="Geprofiler is a Python HTTP Server profiler that makes it easy to find slow code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ben Pham",
    author_email="benalpha1105@gmail.com",
    url="https://github.com/phamtrongngh/geprofiler",
    keywords=["profiling", "profile", "profiler", "cpu", "time", "sampling"],
    install_requires=["pyyaml"],
    extras_require={"jupyter": ["ipython"]},
    include_package_data=True,
    python_requires=">=3.7",
    entry_points={"console_scripts": ["geprofiler = geprofiler.__main__:main"]},
    zip_safe=False,
    classifiers=[
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Testing",
    ],
)
