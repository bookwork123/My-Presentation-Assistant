import os
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, collect_submodules


project_root = Path(os.getcwd()).resolve()

datas = [
    (str(project_root / "backend" / "model" / "gesture_recognizer.task"), "backend/model"),
]
datas += collect_data_files("mediapipe")
datas += collect_data_files("cv2")

binaries = []
binaries += collect_dynamic_libs("mediapipe")
binaries += collect_dynamic_libs("cv2")

hiddenimports = []
hiddenimports += collect_submodules("mediapipe")
hiddenimports += collect_submodules("pycaw")
hiddenimports += collect_submodules("comtypes")
hiddenimports += collect_submodules("pyautogui")


a = Analysis(
    ["frontend/main.py"],
    pathex=[str(project_root)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="MyPresentationAssistant",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="MyPresentationAssistant",
)
