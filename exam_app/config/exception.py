"""Exceptions that occur during configuration.

Attributes
----------
JsonSchemaError : Exception
    Base class for all schema errors when read the JSON file.
SettingValueError : Exception
    Base class for all errors when validate the settings.

RequiredKeysError : JsonSchemaError
    If no required keys in the JSON file.
UnwantedKeysError : JsonSchemaError
    If unwanted keys in the JSON file.
InvalidTypeError : JsonSchemaError
    If there is an invalid value type in the JSON file.

EmptyFileNameError : SettingValueError
    If the file name value is empty.
InvalidFontSizeError : SettingValueError
    If the font size value is out of range.
InvalidWidthError : SettingValueError
    If the width value is out of range.
InvalidHeightError : SettingValueError
    If the height value is out of range.
InvalidPaddingError : SettingValueError
    If the padding value is out of range.

"""


class JsonSchemaError(Exception):
    """Base class for all schema errors when read the JSON file."""


class SettingValueError(Exception):
    """Base class for all errors when validate the settings."""


class RequiredKeysError(JsonSchemaError):  # noqa: D101
    def __init__(self, required_keys: set[str]) -> None:
        """If no required keys in the JSON file.

        Parameters
        ----------
        required_keys : set[str]
            Required keys in the JSON file

        """
        msg: str = f"No required keys in the JSON file: {required_keys}"
        super().__init__(msg)


class UnwantedKeysError(JsonSchemaError):  # noqa: D101
    def __init__(self, unwanted_keys: set[str]) -> None:
        """If unwanted keys in the JSON file.

        Parameters
        ----------
        unwanted_keys : set[str]
            Unwanted keys in the JSON file

        """
        msg: str = f"Unwanted keys in the JSON file: {unwanted_keys}"
        super().__init__(msg)


class InvalidTypeError(JsonSchemaError):  # noqa: D101
    def __init__(self, key: str, value_type: type, required_type: type) -> None:
        """If there is an invalid value type in the JSON file.

        Parameters
        ----------
        key : str
            Setting key
        value_type : type
            Setting value type
        required_type : type
            Value type in 'DEFAULT_SETTINGS'

        """
        msg: str = f"'{key}' {required_type} is an invalid value in the JSON file: {value_type}"
        super().__init__(msg)


class EmptyFileNameError(SettingValueError):  # noqa: D101
    def __init__(self) -> None:
        """If the file name value is empty."""
        msg: str = "File name is empty in the settings."
        super().__init__(msg)


class InvalidFontSizeError(SettingValueError):  # noqa: D101
    def __init__(self, font_size: int) -> None:
        """If the font size value is out of range.

        Parameters
        ----------
        font_size : int
            Font size

        """
        msg: str = f"Font size value out of range: {font_size}"
        super().__init__(msg)


class InvalidWidthError(SettingValueError):  # noqa: D101
    def __init__(self, width: int) -> None:
        """If the width value is out of range.

        Parameters
        ----------
        width : int
            Window width

        """
        msg: str = f"Width value out of range: {width}"
        super().__init__(msg)


class InvalidHeightError(SettingValueError):  # noqa: D101
    def __init__(self, height: int) -> None:
        """If the height value is out of range.

        Parameters
        ----------
        height : int
            Window height

        """
        msg: str = f"Height value out of range: {height}"
        super().__init__(msg)


class InvalidPaddingError(SettingValueError):  # noqa: D101
    def __init__(self, padding: int) -> None:
        """If the padding value is out of range.

        Parameters
        ----------
        padding : int
            Padding

        """
        msg: str = f"Padding value out of range: {padding}"
        super().__init__(msg)
