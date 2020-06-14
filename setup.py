import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-networkdays",
    version="0.0.1",
    author="Carlos Leite",
    author_email="caduado@gmail.com",
    description="Networkday function like spreadsheet, plus job schedule",
    keywords='networkdays calendar schedule project',
    description_content_type="text/x-rst",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/cadu-leite/networkdays",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Scheduling",
    ],
    python_requires='>=3.6',
)