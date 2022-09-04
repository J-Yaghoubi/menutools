from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='menutools',
    version='1.0.3',
    description='Create command line menu',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/J-Yaghoubi/menutools',
    python_requires='>=3.8',
    author='Seyed Jafar Yaghoubi',
    author_email='algo3xp3rt@gmail.com',
    license='MIT',
    packages=['menutools'],
    zip_safe=False
    )