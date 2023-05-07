import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="languagemodels",
    version="0.0.1",
    author="Jon Craton",
    author_email="jon@joncraton.com",
    description="Simple inference interface for large language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jncraton/languagemodels",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
    ],
)