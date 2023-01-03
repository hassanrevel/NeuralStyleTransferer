from setuptools import find_packages, setup

setup(
    include_package_data=True,
    name='Neural style transfer',
    version='0.0.1',
    description='Neural style Transfer',
    author = 'A.H Revel',
    packages=find_packages(),

    long_description='A.H Revel\'s Neural Style Transfer',
    long_description_content_type = "The src module allows you to apply the neural style transfer on your image",
    classifier=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)