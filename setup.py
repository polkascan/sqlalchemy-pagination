import re

# try:  # for pip >= 10
#     from pip._internal.req import parse_requirements
# except ImportError:  # for pip <= 9.0.3
#     from pip.req import parse_requirements

try:
    # newest versions.
    # pip>=21.x.x
    from pip._internal.req.constructors import (
        install_req_from_parsed_requirement,
    )
except ImportError:
    # pip<=20.x.x
    def install_req_from_parsed_requirement(x):
        return x


from setuptools import setup, find_packages


def requirements(filename):
    # reqs = parse_requirements(filename, session=False)
    # return [str(r.req) for r in reqs]
    # read your requirements.
    install_reqs = parse_requirements(requirements_path, session=False)
    # for pip==21.x.x convert ParsedRequirement into InstallRequirement.
    return [install_req_from_parsed_requirement(req) for req in install_reqs]


def get_version():
    with open('sqlalchemy_pagination/__init__.py', 'r') as f:
        version_regex = r'^__version__\s*=\s*[\'"](.+)[\'"]'
        return re.search(version_regex, f.read(), re.MULTILINE).group(1)

setup(
    name='sqlalchemy-pagination',
    version=get_version(),
    url='https://github.com/wizeline/sqlalchemy-pagination',
    author='Wizeline',
    author_email='engineering@wizeline.com',
    description='A small utility to paginate SqlAlchemy queries.',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    keywords=['sqlalchemy', 'pagination', 'paginate'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    tests_require=requirements('requirements-dev.txt'),
    install_requires=requirements('requirements.txt'),
    extras_require={
        'dev': requirements('requirements-dev.txt')
    }
)
