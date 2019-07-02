import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chapterprojects",
    version="0.0.1",
    author="PatchworkCookie",
    description="A collection of programming projects from the book 'Automate the Boring Stuff with Python' by Al Sweigart",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PatchworkCookie/Sweigart-Book-Projects.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)