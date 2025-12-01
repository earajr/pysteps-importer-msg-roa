#!/usr/bin/env python

"""Tests for `pysteps_importer_msg_roa` package."""


def test_plugins_discovery():
    """It is recommended to at least test that the plugin modules provided by the plugin are
    correctly detected by pysteps. For this, the tests should be ran on the installed
    version of the plugin (and not against the plugin sources).
    """

    from pysteps.io import interface as io_interface
    from pysteps.postprocessing import interface as pp_interface

    plugin_type = "importer"
    if plugin_type == "importer":
        new_importers = ["importer_msg_roa"]
        for importer in new_importers:
            assert importer.replace("importer_", "") in io_interface._importer_methods

    elif plugin_type == "diagnostic":
        new_diagnostics = ["importer_msg_roa"]
        for diagnostic in new_diagnostics:
            assert diagnostic in pp_interface._diagnostics_methods

def test_importers_with_files():
    """Additionally, you can test that your plugin correctly reads the corresponding
    some example data.
    """

    # Write the test here.
    pass
