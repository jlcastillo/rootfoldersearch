import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jlcastillo", # Replace with your own username
    version="0.0.1",
    author="jlcastillo",
    author_email="jlcastillolorenzo@gm**l.com",
    description="This package finds the root directory of a project by traversing the ancestors directories starting at a given path.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jlcastillo/rootfoldersearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
