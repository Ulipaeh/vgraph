# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/ulipa/Documents/Python Scripts/vgraph/main.py'],
             pathex=['C:\\Users\\ulipa\\Documents\\Python Scripts\\vgraph'],
             binaries=[],
             datas=[('C:/Users/ulipa/Documents/Python Scripts/vgraph/Icons', 'Icons/')],
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
          [],
          exclude_binaries=True,
          name='Vgraph',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\ulipa\\Documents\\Python Scripts\\vgraph\\icono.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Vgraph')
