"""Debug function for the hwnd stuff without loading in any of the p loppoer code"""

import sys
from pathlib import Path

# Inserts the hwnd folder so we can load it directly without extra stuff
MODFOLDER: Path = Path(__file__).parent.parent
hwnd_folder = MODFOLDER / "plopper" / "embed"
if str(hwnd_folder) not in sys.path:
    sys.path.insert(0, str(hwnd_folder))

def test_hwnd():
    from hwnd_functions import hwnd_from_exe
    exe_names = [
        "arma3.exe",
        "arma3_x64.exe",
    
        "arma3diag_x64.exe",
    ]

    hwnd = hwnd_from_exe(exe_names)
    if hwnd is None:
        return "hwnd not found. Can't identify the Arma3.exe, did you rename it?"
    else:
        return 0

def test_hwnd_alt():
    from hwnd_functions import hwnd_from_name
    hwnd = hwnd_from_name("Arma3_x64.exe")
    if hwnd is None:
        return "hwnd not found. Can't identify the Arma3.exe, did you rename it?"
    else:
        return 0
