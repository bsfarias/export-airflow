from setuptools import setup, find_packages

import version

setup(
    name='export-airflow',
    version=version.VERSION,

    description='Export Airflow',

    author='...',
    author_email='...',

    packages=find_packages(exclude=['venv', 'dist', 'docs', 'tests']),
    py_modules=['export_airflow', 'export_version'],

    install_requires=[
        'apache-airflow==1.10.14'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Monitoring'
    ]
)
