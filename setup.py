import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gtl2via",
    version="0.0.1",
    author="Shi Jin",
    author_email="jinzishuai@gmail.com",
    description="Converter from AWS SageMaker tto VIA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jinzishuai/gtl2via",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["gtl2via = gtl2via.__main__:main"]},
)
