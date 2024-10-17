"""Read the setting file.

Attributes
----------
SettingDict : TypedDict
    Define value types for the settings.
DEFAULT_SETTINGS : Final[SettingDict]
    If no JSON file for the settings, the following settings will be used.
JsonSchemaError : Exception
    Base class for all schema errors when read the JSON file.
RequiredKeysError : JsonSchemaError
    If no required keys in the JSON file.
UnwantedKeysError : JsonSchemaError
    If unwanted keys in the JSON file.
InvalidValueTypeError : JsonSchemaError
    If there is an invalid value type in the JSON file.

"""

import json
from pathlib import Path
from typing import Any, Final, TypedDict


class SettingDict(TypedDict):
    """Define value types for the settings."""

    file_name: str
    font_name: str
    font_size: int
    width: int
    height: int
    padding: int


# If there is no JSON file for the settings, the following settings will be used.
DEFAULT_SETTINGS: Final[SettingDict] = {
    "file_name": "question.csv",
    "font_name": "",
    "font_size": 18,
    "width": 640,
    "height": 480,
    "padding": 8,
}


class JsonSchemaError(Exception):
    """Base class for all schema errors when read the JSON file."""


class RequiredKeysError(JsonSchemaError):  # noqa: D101
    def __init__(self, keys: set[str]) -> None:
        """If no required keys in the JSON file.

        Parameters
        ----------
        keys : set[str]
            Required keys

        """
        super().__init__(f"No required keys in the JSON file: {keys}")


class UnwantedKeysError(JsonSchemaError):  # noqa: D101
    def __init__(self, keys: set[str]) -> None:
        """If unwanted keys in the JSON file.

        Parameters
        ----------
        keys : set[str]
            Unwanted keys

        """
        super().__init__(f"Unwanted keys in the JSON file: {keys}")


class InvalidValueTypeError(JsonSchemaError):  # noqa: D101
    def __init__(self, key: str, value_type: type, default_type: type) -> None:
        """If there is an invalid value type in the JSON file.

        Parameters
        ----------
        key : str
            Setting key
        value_type : type
            Invalid value type
        default_type : type
            Value type in the 'DEFAULT_SETTINGS'

        """
        super().__init__(f"'{key}' {default_type} is an invalid value in the JSON file: {value_type}")


def read_json_file(file_name: str, dir_layer: int = 1) -> SettingDict | None:
    """Load settings from the JSON file and return the settings.

    Parameters
    ----------
    file_name : str
        JSON file name
    dir_layer : int, optional
        JSON file directory hierarchy, 0: Current, 1: Parent, by default 1

    Returns
    -------
    SettingDict | None
        If the load fails, returns None.

    """
    settings: SettingDict | None = None

    parent: Path = Path(__file__).resolve().parents[dir_layer]
    file: Path = parent.joinpath(file_name)

    try:
        with Path.open(file, encoding="UTF-8") as f:
            json_settings: dict[str, Any] = json.load(f)

        # Compare with the schema of the 'DEFAULT_SETTINGS'.
        # If an error occurs, go to the exception 'JsonSchemaError'.
        json_keys: set[str] = set(json_settings.keys())
        default_keys: set[str] = set(DEFAULT_SETTINGS.keys())

        if json_keys == default_keys:
            for key, value in json_settings.items():
                value_type: type = type(value)
                default_type: type = type(DEFAULT_SETTINGS.get(key))

                if value_type is not default_type:
                    raise InvalidValueTypeError(key=key, value_type=value_type, default_type=default_type)
        else:
            required_keys: set[str] = default_keys.difference(json_keys)
            unwanted_keys: set[str] = json_keys.difference(default_keys)

            if required_keys:
                raise RequiredKeysError(keys=required_keys)

            if unwanted_keys:
                raise UnwantedKeysError(keys=unwanted_keys)

        settings = json_settings  # type: ignore  # noqa: PGH003
    except FileNotFoundError:
        with Path.open(file, "w", encoding="UTF-8") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)

        settings = DEFAULT_SETTINGS
    except json.decoder.JSONDecodeError as e:
        print(type(e), "Failed to load settings from the JSON file.", sep="\n")
    except JsonSchemaError as e:
        print(type(e), e, sep="\n")

    return settings


if __name__ == "__main__":
    settings: SettingDict | None = read_json_file("setting.json")

    if settings:
        print(settings)
