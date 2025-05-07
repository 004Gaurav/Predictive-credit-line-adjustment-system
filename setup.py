from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    Returns a list of required packages from the given requirements.txt file.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
    return requirements

setup(
    name='predictive_credit_line_adjustment',
    version='0.0.1',
    description='A machine learning system to predict and adjust credit lines based on user behavior.',
    long_description=open('README.md').read() if 'README.md' else '',
    long_description_content_type='text/markdown',
    author='Gaurav Kumar',
    author_email='gauravkumar19994@gmail.com',
    url='https://github.com/yourusername/credit-line-adjustment',  # <-- Change to your actual GitHub repo URL
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
    include_package_data=True
)
