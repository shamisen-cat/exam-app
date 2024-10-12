"""
設定の定義

Attributes
----------
DEFAULT_SETTINGS : dict[str, int | str]
    デフォルト設定
REQUIRED_COLUMNS : tuple[str, ...]
    設問データの必須列項目
SETTINGS : dict[str, int | str]
    設定値
FILE_NAME: Final
    設問データのファイル名
FONT_NAME : Final
    フォント名
FONT_SIZE : Final
    フォントサイズ (pt)
WIDTH : Final
    幅 (px)
HEIGHT : Final
    高さ (px)
PADDING : Final
    余白 (px)

"""

from typing import Final

from exam_app.config.setting import JsonFile

# デフォルト設定
# TODO: GUI作成時に適宜修正
DEFAULT_SETTINGS: dict[str, int | str] = {
    "file_name": "question.csv",
    "font_name": "",
    "font_size": 18,
    "width": 640,
    "height": 480,
    "padding": 8,
}

# 設問データの必須列項目
REQUIRED_COLUMNS: tuple[str, ...] = (
    "form",
    "eval_item",
    "question",
    "comment",
    "answer",
)


def read_setting_file() -> dict[str, int | str]:
    """
    設定ファイルの読み込み

    Returns
    -------
    dict[str, int | str]
        設定値

    """
    settings: dict[str, int | str] = JsonFile(default_settings=DEFAULT_SETTINGS, dir_layer=1).settings
    if settings:
        print("Successfully read setting file.")

    return settings


# 設定ファイルの読み込み
SETTINGS: dict[str, int | str] = read_setting_file()

if SETTINGS:
    # 設問データのファイル名
    FILE_NAME: Final = SETTINGS["file_name"]

    # ウィンドウ設定
    FONT_NAME: Final = SETTINGS["font_name"]
    FONT_SIZE: Final = SETTINGS["font_size"]
    WIDTH: Final = SETTINGS["width"]
    HEIGHT: Final = SETTINGS["height"]
    PADDING: Final = SETTINGS["padding"]


def load_settings() -> bool:
    """設定の読み込み"""
    # TODO: バリデーションの実装
    return SETTINGS != {}
