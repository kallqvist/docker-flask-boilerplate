import os
from setuptools import setup
try: # pip >= 10.0
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError: # pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

req_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
reqs = [str(r.req) for r in parse_requirements(req_file, session=PipSession())]

setup(
    name='docker-flask-boilerplate',
    version='0.0.1',
    install_requires=reqs,
    packages=[],
)
