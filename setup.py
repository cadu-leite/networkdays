import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-networkdays",
    version="1.2",

    author="Carlos Leite",
    author_email="caduado@gmail.com",

    description="Business days (workdays) between two date, like `NetworkDays` function used on spreadsheets and more.",

    long_description=long_description,
    long_description_content_type="text/x-rst",

    keywords=["workdays", "business day", "networkdays", "diasuteis", "calendar", "days", "schedule", "excel", "feriados", "holidays"],

    url="https://github.com/cadu-leite/networkdays",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Environment :: Console",
        "Environment :: Web Environment",

        "Intended Audience :: Developers",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Customer Service",

        "License :: OSI Approved :: BSD License",

        "Operating System :: OS Independent",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",

        "Topic :: Office/Business ",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    python_requires=">=3.",
)
