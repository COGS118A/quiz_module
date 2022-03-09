import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='quiz',
    version='0.0.1',
    author='Scott',
    author_email='yuy004@ucsd.edu',
    description='Display the quiz content',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ScottY177/quiz_module',
    project_urls = {
        "Bug Tracker": "https://github.com/ScottY177/quiz_module/issues"
    },
    license='MIT',
    packages=['quiz'],
    package_data = {"": ["*.js", "*.css"]},
    include_package_data = True,
    install_requires=[''],
)