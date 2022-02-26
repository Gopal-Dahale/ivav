from setuptools import setup

setup(name="ivav",
      version="0.0.1",
      description="A quantum computer simulator",
      py_modules=["index_view"],
      package_dir={"": "ivav"}
      classifiers=[
            "Programming Language :: Python :: 3.9.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ]
      )
