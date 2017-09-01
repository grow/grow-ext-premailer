from setuptools import setup


setup(
    name='grow-ext-premailer',
    version='1.0.0',
    license='MIT',
    author='Grow Authors',
    author_email='hello@grow.io',
    include_package_data=False,
    packages=[
        'premailer_ext',
    ],
    install_requires=[
        'premailer',
    ],
)
