# -*- mode: python ; coding: utf-8 -*-

# One-file spec for MGWRApp (Windows)
# 產出：dist/MGWRApp.exe 只有一顆執行檔

import sys
from PyInstaller.utils.hooks import collect_submodules

main_script = 'main.py'

# 將常見的動態匯入一次蒐集起來，避免漏模組
hidden_imports = (
    collect_submodules('mgwrlib')
    + collect_submodules('spglm')
    + collect_submodules('numpy')
    + collect_submodules('scipy')
)

# 靜態資源
datas = [
    ('img/*', 'img'),
    ('fonts/*', 'fonts'),
    ('src/*', 'src'),
]

block_cipher = None

a = Analysis(
    [main_script],
    pathex=['.'],
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
    noarchive=False,     # 保持預設，通常較穩
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# === 關鍵：one-file 寫法 ===
# 1) 不要 COLLECT
# 2) EXE 內直接帶入 a.binaries / a.zipfiles / a.datas
# 3) 不要 exclude_binaries=True
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MGWRApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,                 # 若一切正常可改 True；發生 DLL 問題先維持 False
    upx_exclude=[],
    console=False,             # 若需主控台輸出改 True
    icon='resources/img/MGWR-pc.ico',
    runtime_tmpdir=None,       # 解壓到系統暫存目錄（one-file 必要行為）
)
