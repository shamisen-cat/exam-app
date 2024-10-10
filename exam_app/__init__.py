"""初期化"""

import sys

from exam_app.config import load_settings

# 設定の読み込み
if load_settings():
    print("Successfully loaded settings.")
else:
    print("Failed to load settings.")
    sys.exit()
