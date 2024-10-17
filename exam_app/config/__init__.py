"""Define the config.

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
    Window Height / px
PADDING : int
    Margin / px

"""

from typing import Final

from exam_app.config.setting import SettingDict, read_json_file

SETTING_FILE_NAME: Final[str] = "setting.json"

settings: SettingDict | None = read_json_file(SETTING_FILE_NAME)

if settings:
    FILE_NAME: str = settings["file_name"]
    FONT_NAME: str = settings["font_name"]
    FONT_SIZE: int = settings["font_size"]
    WIDTH: int = settings["width"]
    HEIGHT: int = settings["height"]
    PADDING: int = settings["padding"]


def load_config() -> bool:
    """Load the config."""
    # TODO: Add validation
    return settings is not None
