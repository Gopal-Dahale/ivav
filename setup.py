from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="ivav",
      version="0.0.1",
      description="A quantum computer simulator",
      py_modules=["index_view"],
      package_dir={"": "ivav"},
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      extras_require={
          "dev": ["pytest>=7.0.1", "check-manisfest>=0.47", "yapf>=0.32.0"]
      },
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/Gopal-Dahale/ivav",
      author="Gopal Ramesh Dahale",
      author_email="dahalegopal27@gmail.com")
