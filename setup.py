# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

# Add the plugin dependencies here
requirements = []

# Add the packages needed to build the package.
setup_requirements = ['pytest-runner']

test_requirements = ['pytest>=3']

# Custom command to run tests using pytest
def run_tests():
    import pytest
    errno = pytest.main(["tests"])
    raise SystemExit(errno)

entry_label = 'pysteps.plugins.' + 'importer'

# It woudld be even better to read the functions from the plugin module.
# We could add multiple functions in the entry_points.
# Is that possible?
# e.g. like plugin_functions = [attr for attr in dir(importlib.import_module(cookiecutter.project_slug.cookiecutter.plugin_type.cookiecutter.plugin_name)) if attr.startswith("import_" if "importer" in cookiecutter.plugin_type else cookiecutter.plugin_type+"_")]
# Then loop over the functions to set all entry_points.
entry = {
    entry_label: [
        'import_msg_roa=pysteps_importer_msg_roa.importer.importer_msg_roa:import_msg_roa'
    ]
}

setup(
    author="Alexander Roberts",
    author_email='earajr@leeds.ac.uk',
    python_requires='>=3.10',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12'
    ],
    description="Pysteps plugin to import Leeds generated rain over Africa files based on MSG data",
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords=['pysteps_importer_msg_roa', 'pysteps' , 'plugin', 'importer'],
    name='pysteps-importer-msg-roa',
    packages=find_packages(),
    setup_requires=setup_requirements,
    # Entry points
    # ~~~~~~~~~~~~
    #
    # This is the most important part of the plugin setup script.
    # Entry points are a mechanism for an installed python distribution to advertise
    # some of the components installed (packages, modules, and scripts) to other
    # applications (in our case, pysteps).
    # https://packaging.python.org/specifications/entry-points/
    #
    # An entry point is defined by three properties:
    # - The group that an entry point belongs indicate the kind of functionality that
    #   provides. For the pysteps importers use the "pysteps.plugins.importers" group.
    #   For the pysteps diagnostics use the "pysteps.plugins.diagnostics" group.
    # - The unique name that is used to identify this entry point in the
    #   "pysteps.plugins.importers" group.
    # - A reference to a Python object. For the pysteps importers, the object should
    #   point to a importer function, and should have the following form:
    #   package_name.module:function.
    # The setup script uses a dictionary mapping the entry point group names to a list
    # of strings defining the importers provided by this package (our plugin).
    # The general form of the entry points dictionary is:
    # entry_points={
    #     "group_name": [
    #         "entry_point_name=package_name.module:function",
    #         "entry_point_name=package_name.module:function2",
    #     ]
    # },
    entry_points = entry,
    version='0.1.0',
    zip_safe=False,
    cmdclass = {
        'test': run_tests,
    },
)
