import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="apple-music-api",  # Replace with your own username
    version="0.0.1",
    author="Juhyun Lee",
    author_email="xog2000@gamil.com",
    description="Easy Apple Music API Helper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hobbyworker/apple-music-api-for-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
    python_requires='>=3.6',
)
