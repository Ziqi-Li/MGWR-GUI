# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/Ziqi/Desktop/developer/GWR-UI-ZIQI'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['matplotlib','PySide','PyQt4','requests','urllib3'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
app = BUNDLE(coll,
             name='MGWR.app',
             icon='resources/img/MGWR.icns',
             bundle_identifier=None,
             info_plist={
                'NSHighResolutionCapable': 'True'
             }
)
