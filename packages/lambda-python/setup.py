import os
import setuptools
from remotion_lambda_sdk.version import VERSION

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="remotion_lambda_sdk",
    version=VERSION,
    author="Johny Burger",
    author_email="jonny@remotion.dev",
    description="Remotion Lambda client",
    long_description_content_type="text/markdown",
    url="https://github.com/remotion-dev/remotion/tree/main/packages/lambda-python",
    classifiers=[

    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    # Name of the python package
    py_modules=["remotion_lambda_sdk"],

)
