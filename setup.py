import setuptools

setuptools.setup(
    name="parallel-execute",
    version="0.0.5",
    author="Sahil Pardeshi",
    author_email="sahilrp7@gmail.com",
    description="Python wrappers for easy multiprocessing and threading",
    long_description=open('README.rst').read(),
    url="https://github.com/parallel-execute/parallel-execute",
    packages=setuptools.find_packages(),
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ]
)