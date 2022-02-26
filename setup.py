from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ivav",
    version="0.0.1",
    description="A quantum computer simulator",
    py_modules=["index_view"],
    package_dir={"": "ivav"},
    classifiers=[
        "Programming Language :: Python :: 3.9.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
