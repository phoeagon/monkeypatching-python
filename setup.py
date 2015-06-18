from setuptools import setup

setup(
    name="monkeypatch",
    version="0.0.1",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="A monkey patching library for python",
    author='phoeagon',
    author_email='admin@phoeagon.info',
    url='https://github.com/phoeagon/monkeypatch-python',
    package_data={
        'monkeypatch': ['README', 'LICENSE']
    },
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    long_description="""Provide dynamic method name resolution and routing
    simulates monkey patching in Ruby.""",
)
