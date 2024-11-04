"""Read the setting file.

Attributes
----------
SettingDict : TypedDict
    Define value types for the settings.
DEFAULT_SETTINGS : Final[SettingDict]
    If no JSON file for the settings, the following settings will be used.

"""

import json
from collections.abc import Callable
from functools import wraps
from pathlib import Path
from typing import Any, Final, TypedDict, TypeVar

if __name__ == "__main__":
    import exception as ex
else:
    from . import exception as ex

F = TypeVar("F", bound=Callable)


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


def validate_settings(func: F) -> F:  # noqa: D103
    @wraps(func)
    def inner(*args, **kwargs) -> SettingDict | None:
        """Validate the setting values."""
        settings: SettingDict | None = func(*args, **kwargs)
        if settings:
            try:
                file_name: str = settings["file_name"]
                if not file_name:
                    raise ex.EmptyFileNameError

                font_size: int = settings["font_size"]
                if font_size < 0:
                    raise ex.InvalidFontSizeError(font_size)

                width: int = settings["width"]
                if width < 0:
                    raise ex.InvalidWidthError(width)

                height: int = settings["height"]
                if height < 0:
                    raise ex.InvalidHeightError(height)

                padding: int = settings["padding"]
                if padding < 0:
                    raise ex.InvalidPaddingError(padding)
            except ex.SettingValueError as e:
                print(type(e), e, sep="\n")
                settings = None

        return settings

    return inner  # type: ignore  # noqa: PGH003


@validate_settings
def load_settings(file_name: str, dir_layer: int = 1) -> SettingDict | None:
    """Load settings from the JSON file and return the settings.

    Parameters
    ----------
    file_name : str
        JSON file name
    dir_layer : int, default 1
        JSON file directory hierarchy, 0: Current, 1: Parent

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

        # Compare with the schema in 'DEFAULT_SETTINGS'.
        # If an error occurs, go to the exception labeled 'JsonSchemaError'.
        json_keys: set[str] = set(json_settings.keys())
        default_keys: set[str] = set(DEFAULT_SETTINGS.keys())

        required_keys: set[str] = default_keys.difference(json_keys)
        if required_keys:
            raise ex.RequiredKeysError(required_keys)

        unwanted_keys: set[str] = json_keys.difference(default_keys)
        if unwanted_keys:
            raise ex.UnwantedKeysError(unwanted_keys)

        for key, value in json_settings.items():
            value_type: type = type(value)
            required_type: type = type(DEFAULT_SETTINGS.get(key))
            if value_type is not required_type:
                raise ex.InvalidTypeError(key, value_type, required_type)

        settings = json_settings  # type: ignore  # noqa: PGH003
    except FileNotFoundError:
        with Path.open(file, "w", encoding="UTF-8") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
        settings = DEFAULT_SETTINGS
    except json.decoder.JSONDecodeError as e:
        print(type(e), "Failed to load settings from the JSON file.", sep="\n")
    except ex.JsonSchemaError as e:
        print(type(e), e, sep="\n")

    return settings


if __name__ == "__main__":
    settings: SettingDict | None = load_settings("setting.json")
    if settings:
        print(settings)
