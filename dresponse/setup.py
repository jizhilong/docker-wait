from setuptools import find_packages, setup

requirements = [
    'docker',
    'flask',
    'uwsgi'
]

packages = find_packages()
version = '0.0.1'

setup(
    name='dresponse',
    version=version,
    description='a python library for running docker'
                ' container pre-startup hooks',
    packages=packages,
    url='https://github.com/jizhilong/docker-wait',
    install_requires=requirements,
    classifiers=[
        'Developement Status :: 3 - Alpha ',
        'Environment :: Other Environment', 
        'Intended Audience :: Developers',
        'Operating Systems :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License'
    ],
    maintainer='jizhilong',
    maintainer_email='zhilongji@gmail.com',
)
