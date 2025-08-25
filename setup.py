import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-networkdays",
    version="1.2",

    author="Carlos Leite",
    author_email="",

    description="Calculate Business days (workdays) between two date, like `NetworkDays` function used on spreadsheets. Schedule based on hours and business days",

    long_description=long_description,
    long_description_content_type="text/x-rst",

    keywords=['business days', 'workdays', 'working days', 'networkdays', 'datetime', 'calendar', 'excel', 'schedule', 'calculate', 'holidays' ],

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

        "Topic :: Software Development",
        "Topic :: Utilities",
        "Topic :: Office/Business"
    ],
    python_requires=">=3.6",
)
