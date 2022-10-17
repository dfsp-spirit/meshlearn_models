# -*- coding: utf-8 -*-

"""
Model persistence functions.
"""

import pickle
import json
import os


def load_model(model_file, model_settings_file, verbose=True):
    """
    Load a pickled model and, if available, JSON metadata from files.

    Parameters
    ----------
    model_fil     e     : str, the filename from which to load the model (Pickle file), must end with '.pkl' or a warning will be printed.
    model_settings_file : str or None, the filename from which to load the model metadata (JSON), must end with '.json' or a warning will be printed. If it contains a path, that path must exist. Set to `None` if you do not have a metadata file or do not want to load it.
    verbose             : bool, whether to print status info to stdout. Does not affect warnings, which will be printed even if `verbose=False`.

    Returns
    -------
    model               : the loaded model, some sklearn or lightgbm model typically.
    model_and_data_info : dict or None. Contains the model metadata loaded from the JSON file.
    """
    if not model_file.endswith('.pkl'):
        print(f"WARNING: Given model filename '{model_file}' does not have '.pkl' file extension.")
    pickle_file_size_mb = int(os.path.getsize(model_file) / 1024. / 1024.)
    if verbose:
        print(f"Loading model from {pickle_file_size_mb} MB file '{model_file}'.")
    model = pickle.load(open(model_file, 'rb'))
    model_and_data_info = None
    if model_settings_file is not None:
        if not model_settings_file.endswith('.json'):
            print(f"WARNING: Given model metadata JSON file filename '{model_settings_file}' does not have '.json' file extension.")
        try:
            with open(model_settings_file, 'r') as fp:
                model_and_data_info = json.load(fp)
                if verbose:
                    print(f"INFO: Loaded settings used to create dataset from file '{model_settings_file}'.")
        except Exception as ex:
            model_and_data_info = None
            print(f"NOTICE: Could not load settings used to create dataset from file '{model_settings_file}': {str(ex)}.")
    else:
        if verbose:
            print(f"INFO: Not loading metadata for model, no filename given.")
    return model, model_and_data_info
