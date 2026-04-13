# My-Presentation-Assistant

Control presentation slides and system audio using hand gestures detected from your webcam.

## Platform Support

- Windows only (uses COM APIs through `pycaw`/`comtypes`).
- Python source run and packaged executable run are both supported.

## Build an Executable (PyInstaller)

The repository includes a ready-to-use spec file and PowerShell scripts.

1. Open PowerShell in the repository root.
2. Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build.ps1 -Clean
```

Build output is created at:

- `dist/PresentationAssistant/PresentationAssistant.exe`

## Clean Build Artifacts

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\clean.ps1
```

This removes `build/` and `dist/`.

## Runtime Prerequisites

- Webcam access enabled for desktop apps.
- Microphone permission is not required; camera permission is.
- Presentation target app should have keyboard focus for slide controls (`left`/`right` arrow simulation).
- Windows audio endpoint available (for volume and mute gestures).
- If executable fails on another machine due to missing runtime DLLs, install the Microsoft Visual C++ Redistributable (x64).

## Packaging Notes

- The gesture model is bundled with the executable:
  - `backend/model/gesture_recognizer.task`
- In packaged mode, model resolution uses PyInstaller runtime paths (`sys._MEIPASS`).
- Primary PyInstaller config is in:
  - `PresentationAssistant.spec`

## Packaged App Test Checklist

After building, launch `dist/PresentationAssistant/PresentationAssistant.exe` and validate:

- App window appears.
- Camera initializes and gesture indicator updates.
- `Open_Palm` and `Closed_Fist` move slides forward/back.
- `Thumb_Up` and `Thumb_Down` adjust system volume.
- `Pointing_Up` toggles mute.
