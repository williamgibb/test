import setuptools.command.test
from setuptools import setup


version = __import__('module').__version__
print('Executing setup.py for {}'.format(version))

setup(
    name="module",
    version=version,
    url='http://www.github.com/williamgibb/test/',
    author='William Gibb',
    author_email='williamgibb@gmail.com',
    description=('CI Integration test'),
    license='MIT',
    packages=['module',
              ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=True
)