"""Define the configuration.

Attributes
----------
SETTING_FILE_NAME : Final[str]
    Setting file name
settings : SettingDict | None
    If the setting file could not be read, None.
FILE_NAME: str
    Question data file name
FONT_NAME : str
    Font name
FONT_SIZE : int
    Font size / pt
WIDTH : int
    Window width / px
HEIGHT : int
    Window height / px
PADDING : int
    Margin / px

"""

from typing import Final

from .setting import SettingDict, load_settings

JSON_FILE_NAME: Final[str] = "setting.json"

SETTINGS: SettingDict | None = load_settings(JSON_FILE_NAME)

if SETTINGS:
    FILE_NAME: str = SETTINGS["file_name"]
    FONT_NAME: str = SETTINGS["font_name"]
    FONT_SIZE: int = SETTINGS["font_size"]
    WIDTH: int = SETTINGS["width"]
    HEIGHT: int = SETTINGS["height"]
    PADDING: int = SETTINGS["padding"]
