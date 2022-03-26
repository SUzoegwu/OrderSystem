try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

# python setup.py register
# python setup.py upload

with open("README.md") as f:
    long_description = f.read()

setup(
    name='ordersystem',
    version='1.0',
    description='OrderSystem to take customer orders',
    author='Somtochukwu Uzoegwu',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='',
    packages=find_packages(),
    # packages=['ordersystem'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers"
    ],
    keywords="order system ordersystem order_system",
    python_requires="~=3.9",
    install_requires=[]
)