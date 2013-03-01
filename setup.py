import setuptools


setuptools.setup(
    name='git-clone-canonical',
    version='0.0.1',
    url='https://github.com/rconradharris/git-clone-canonical',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    description='git clone popular repos by name not location',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[''],
    scripts=['bin/git-clone-canonical'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
