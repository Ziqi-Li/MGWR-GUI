# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_submodules

# 主程式檔名
main_script = 'main.py'

# 把 mgwrlib、spglm 可能用到的子模組都包含進來（防止隱性匯入漏掉）
hidden_imports = collect_submodules('mgwrlib') + collect_submodules('spglm') + collect_submodules('numpy') + collect_submodules('scipy')


# 資料夾打包設定
datas = [
    ('img/*', 'img'),
    ('fonts/*', 'fonts'),
    ('src/*', 'src'),
]

block_cipher = None

a = Analysis(
    [main_script],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MGWRApp',           # 生成的 exe 名稱
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,            # GUI 程式要關閉 console
    icon='resources/img/MGWR-pc.ico'     # 你的應用程式圖示
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MGWRApp'
)
