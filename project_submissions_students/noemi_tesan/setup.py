from setuptools import setup, find_packages

setup(
    name="gravity_listener",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "matplotlib",
    ],
)
