"""
設定ファイルの読み込み

Attributes
----------
JsonFile : class
    JSONファイルから設定値を読み込み、設定値を定義する。

"""

from __future__ import annotations

import functools
import json
from collections.abc import Callable
from pathlib import Path
from typing import Final, TypeVar

C = TypeVar("C", bound=Callable)

# JSONファイルのファイル名
FILE_NAME: Final[str] = "setting.json"


def singleton(cls: C) -> C:  # noqa: D103
    __instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):  # noqa: ANN202
        nonlocal __instance
        if __instance is None:
            __instance = cls(*args, **kwargs)
        return __instance

    return inner  # type: ignore  # noqa: PGH003


@singleton
class JsonFile:
    """
    JSONファイルから設定値を読み込み、設定値を定義する。

    Attributes
    ----------
    __settings : dict[str, int | str]
        設定値

    """

    def __init__(self, default_settings: dict[str, int | str] | None = None, dir_layer: int = 0) -> None:
        """
        JSONファイルがない、または設定項目が不足している場合、default_settingsの値を読み込む。

        Parameters
        ----------
        default_settings : dict[str, int | str] | None, default None
            デフォルトの設定値
        dir_layer : int, default 0
            JSONファイルのディレクトリ階層, 0: カレントディレクトリ, 1: 親ディレクトリ

        """
        if default_settings is None:
            default_settings = {}

        parent: Path = Path(__file__).resolve().parents[dir_layer]
        file: Path = parent.joinpath(FILE_NAME)

        settings: dict[str, int | str]
        try:
            # JSONファイルの読み込み
            with Path.open(file, encoding="UTF-8") as f:
                settings = json.load(f)

            # 設定項目が不足している場合、設定値を追加する。
            for key, val in default_settings.items():
                settings.setdefault(key, val)
        except FileNotFoundError:
            settings = default_settings

            # JSONファイルの出力
            with Path.open(file, "w", encoding="UTF-8") as f:
                json.dump(default_settings, f, indent=4)
        except json.decoder.JSONDecodeError:
            print("Failed to read settings from JSON file.")
            settings = {}

        self.__settings: dict[str, int | str] = settings

    @property
    def settings(self) -> dict[str, int | str]:  # noqa: D102
        return self.__settings


if __name__ == "__main__":
    settings_1: dict[str, int | str] = {"font_name": "", "font_size": 18}
    settings_2: dict[str, int | str] = {"font_name": "HackGen", "font_size": 12, "width": 640}

    print("Generating an instance.")
    instance_1: JsonFile = JsonFile(settings_1)
    instance_2: JsonFile = JsonFile(settings_2)
    instance_3: JsonFile = JsonFile()

    print("settings_1:", instance_1.settings)
    print("settings_2:", instance_2.settings)
    print("settings_3:", instance_3.settings)

    print("instance_1 is instance_2:", instance_1 is instance_2)
    print("instance_1 is instance_3:", instance_1 is instance_3)

    print("Modifying and Adding settings.")
    instance_1.settings["font_name"] = "HackGen"
    instance_2.settings["font_size"] = 12
    instance_3.settings["width"] = 640

    print("settings_1:", instance_1.settings)

    print("instance_1 is instance_2:", instance_1 is instance_2)
    print("instance_1 is instance_3:", instance_1 is instance_3)
