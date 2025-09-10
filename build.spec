# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_submodules

main_script = 'main.py'

hidden_imports = collect_submodules('mgwrlib') + collect_submodules('spglm') + collect_submodules('numpy') + collect_submodules('scipy')


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
    name='MGWRApp',        
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,           
    icon='resources/img/MGWR-pc.ico'   
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
