from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

# specify requirements of your package here
REQUIREMENTS = [ 'requests' ]

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

# calling the setup function
setup(name='password-manager',
      version='1.0.0',
      description='A simple python wrapper for creating passwords..',
      long_description=long_description,
      url='https://github.com/TheCodingFreakj/password-manager',
      author='Pallavi Priyadarshini',
      author_email='pallavidapriya75@gmail.com',
      license='MIT',
      packages=[ 'password-manager' ],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='password manager'
      )
