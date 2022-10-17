from setuptools import setup

setup(
    name='meshlearn_models',
    version='0.0.1',
    description='Predict computationally expensive, local, vertex-wise mesh descriptors like the local gyrification index for a mesh vertex, based on its neighborhood.',
    url='https://github.com/dfsp-spirit/meshlearn_models',
    author='Tim Schaefer',
    author_email='ts+code@rcmd.org',
    license='MIT',
    packages=['meshlearn_models'],
    install_requires=['numpy',
                      'nibabel',
                      'trimesh',
                      'sklearn'
                      ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-console-scripts', 'pytest-runner', 'coverage'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
    package_dir = {'': 'src'},
    entry_points = {
        'console_scripts': [
            'meshpredict_lgi = predict.meshpredict_lgi:main',
        ]
    }
)
