from setuptools import setup, find_packages

setup(
    name='printannotate',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'printannotate = printannotate.__main__:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
    author='Andrzej Wasowski',
    author_email='me@wasowski.dev',
    description='A package to annotate print statements in provided script.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/saikotek/printannotate',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
