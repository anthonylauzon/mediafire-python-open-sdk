from setuptools import setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

import uuid

requirements = parse_requirements('requirements.txt', session=uuid.uuid1())
install_requires = [str(r.req) for r in requirements]

setup(
    name='mediafire',
    version='0.6.0',
    author='Roman Yepishev',
    author_email='rye@keypressure.com',
    packages=['mediafire', 'mediafire.media'],
    url='https://github.com/MediaFire/mediafire-python-open-sdk',
    license='BSD',
    description='Python MediaFire client library',
    long_description=open('README.rst').read(),
    install_requires=install_requires,
    keywords="mediafire cloud files sdk storage api upload",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: BSD License'
    ]
)
