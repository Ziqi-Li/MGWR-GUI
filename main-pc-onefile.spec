# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Ziqi\\Desktop\\mgwr-gui-windows'],
             binaries=[],
             datas=[('C:\\Users\\Ziqi\\Desktop\\mgwr-gui-windows\\img','img')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MGWR',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False,
		  icon='resources/img/MGWR-pc.ico')
