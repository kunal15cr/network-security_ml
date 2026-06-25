import yaml
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os, sys
import numpy as np
# import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    
    try:
        with open(file_path, "rb") as file:
            return yaml.safe_load(file) 
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    
def write_yaml_file(file_path: str, content: object = None, replace: bool = False) -> None:
    try:
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        if replace and os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, "w") as file:
            yaml.safe_dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e