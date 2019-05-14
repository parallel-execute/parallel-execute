import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parallel-execute",
    version="0.0.1",
    author="Sahil Pardeshi",
    author_email="sahilrp7@gmail.com",
    description="Python wrappers for easy multiprocessing and threading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parallel-execute/parallel-execute",
    packages=setuptools.find_packages(),
    license='MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)