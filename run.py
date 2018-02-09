"""The sector model wrapper for smif to run the energy demand model
"""
import os
import logging
import configparser
import numpy as np
from datetime import date
from collections import defaultdict
from smif.model.sector_model import SectorModel
from pkg_resources import Requirement, resource_filename
from pyproj import Proj, transform
from sweep import main

class sweepWrapper(SectorModel):
    """Energy Demand Wrapper
    """
    def __init__(self, name):
        super().__init__(name)

        self.user_data = {}

    def before_model_run(self, data=None):
        """Implement this method to conduct pre-model run tasks

        Arguments
        ---------
        data_handle: smif.data_layer.DataHandle
            Access parameter values (before any model is run, no dependency
            input data or state is guaranteed to be available)

        Info
        -----
        `self.user_data` allows to pass data from before_model_run to main model
        """
        pass

    def initialise(self, initial_conditions):
        """
        """
        pass

    def simulate(self, data_handle):
        """Runs the Energy Demand model for one `timestep`

        Arguments
        ---------
        data_handle : dict
            A dictionary containing all parameters and model inputs defined in
            the smif configuration by name

        Returns
        =======
        out_dict : dict
            Outputs of et_module
        """
        print("... start sweep")
        out_dict = {}

        print("... Finished running sweep")
        return out_dict

    def extract_obj(self, results):
        return 0
