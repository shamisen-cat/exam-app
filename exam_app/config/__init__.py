"""設定の定義"""

from typing import Final

from exam_app.config.setting import JsonFile

# デフォルト設定
# TODO: GUI作成時に適宜修正
DEFAULT_SETTINGS: dict[str, int | str] = {
    "file_name": "question.csv",
    "font": "",
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

    Notes
    -----
    default_settings : dict[str, int | str] | None
        設定ファイルがない、または設定項目が不足している場合の設定値, by default None
    dir_layer : int
        設定ファイルのディレクトリ, 0: config, 1: exam_app, by default 0

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
    FONT: Final = SETTINGS["font"]
    FONT_SIZE: Final = SETTINGS["font_size"]
    WIDTH: Final = SETTINGS["width"]
    HEIGHT: Final = SETTINGS["height"]
    PADDING: Final = SETTINGS["padding"]


def load_settings() -> bool:
    """設定の読み込み"""
    # TODO: バリデーションの実装
    return SETTINGS != {}
