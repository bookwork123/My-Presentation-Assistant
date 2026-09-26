# My-Presentation-Assistant

Control presentation slides and system audio using hand gestures detected from your webcam.

## Download

**[Download the latest release](https://github.com/bookwork123/My-Presentation-Assistant/releases/latest)**

1. Download `MyPresentationAssistant-windows.zip` from the link above.
2. Extract the zip to a folder of your choice.
3. Run `MyPresentationAssistant.exe`.

## Platform Support

- Windows only (uses COM APIs through `pycaw`/`comtypes`).

## Note on Windows SmartScreen

When you first run the executable, Windows Defender SmartScreen may show a warning ("Windows protected your PC"). This happens because the executable is not code-signed. Click **More info** then **Run anyway** to proceed.

## Runtime Prerequisites

- Webcam access enabled for desktop apps.
- Presentation target app should have keyboard focus for slide controls (`left`/`right` arrow simulation).
- Windows audio endpoint available (for volume and mute gestures).
- If the executable fails due to missing runtime DLLs, install the [Microsoft Visual C++ Redistributable (x64)](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).

## Gestures

- **Open Palm** / **Closed Fist** — move slides forward / back.
- **Thumb Up** / **Thumb Down** — adjust system volume.
- **Pointing Up** — toggle mute.

## Building from Source

If you prefer to build the executable yourself:

1. Open PowerShell in the repository root.
2. Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build.ps1 -Clean
```

Output: `dist/MyPresentationAssistant/MyPresentationAssistant.exe`
