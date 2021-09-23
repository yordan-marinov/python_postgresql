import os
from pathlib import Path
from configparser import ConfigParser


def get_db_config(section) -> dict:
    """Return params as dict from initializing file"""

    # Path.glob returns gen.
    file_name = next(Path.cwd().glob('*.ini'))

    config_parser = ConfigParser()
    config_parser.read(file_name)

    config_params_dict = {}
    # Raises exception with wrong section.
    if config_parser.has_section(section):
        params = config_parser.options(section)
        for param in params:
            # Password is environment var.
            if param == "password":
                value = config_parser.get(section, param, vars=os.environ)
            else:
                value = config_parser.get(section, param)

            config_params_dict[param] = value
    else:
        raise Exception(f"Section '{section}' is not found in the {file_name} file.")

    return config_params_dict
