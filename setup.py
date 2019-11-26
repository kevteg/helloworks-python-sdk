from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='helloworks-python-sdk',
    version='0.3',
    description="A Python wrapper for the HelloWorks API  (https://portal.helloworks.com/)",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    keywords='Helloworks python api sdk',
    url='https://github.com/kevteg/helloworks-python-sdk',
    author='kevteg',
    author_email='kevteg05@gmail.com',
    license='MIT',
    packages=[
        'helloworks',
        'helloworks.utils',
    ],
    install_requires=[
        'requests'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False
)
