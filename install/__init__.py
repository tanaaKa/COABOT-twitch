"""
    Some ways onf installing the python requirements in background threads, so we don't freeze and crash the game
    Everything in this install module should be 100% free of any install requirements
"""

from pathlib import Path
from shutil import copy
import subprocess
import sys
import threading
import winreg
import os


INSTALL_PROGRESS = [0, ""]
MODFOLDER = Path(__file__).parents[1]


def install(*args, **kwargs):
    """PIP requiremnts install call to handle in background"""
    t = threading.Thread(target=install_bg, args=args, kwargs=kwargs)
    t.start()
    return True


def test(*args, **kwargs):
    """
        ["plopper_install.test"] call py3_fnc_callExtension; 
    """
    from .hwnd import test_hwnd, test_hwnd_alt
    return test_hwnd()


def install_bg(force=False, path=None, **kwargs):
    """Installs the requirements in current pythia version"""
    global INSTALL_PROGRESS

    print("Installing requirements")
    requirementspath = MODFOLDER / "requirements.txt"

    if path is None:
        path = Path(sys.executable)

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    cmd = [str(path), "-m", "pip", "install", "--isolated", "-q", "-q", "-r", str(requirementspath)]
    if force:
        cmd.insert(len(cmd) - 2, "--force")

    try:
        subprocess.check_output(cmd, startupinfo=startupinfo, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        msg = e.output.decode("UTF-8").strip()
        print(e.returncode, msg)
        INSTALL_PROGRESS = [-1, msg]
    else:
        INSTALL_PROGRESS = [0.5, ""]
        INSTALL_PROGRESS = install_pywin32(path)
        print("Finished installing")


def install_pywin32(python_exe: Path):
    """Finishes postinstall for pywin32"""

    print("Installing Pywin32")
    folder = python_exe.parent
    files = ("pythoncom37.dll", "pywintypes37.dll")

    
    for file in files:
        target = folder / file  # type: Path
        if not target.exists():
            src = folder / "Lib" / "site-packages" / "pywin32_system32" / file
            copy(str(src), str(target), follow_symlinks=True)

    os.environ["PATH"] += ";{}".format(folder)
    return [1, ""]


def installed():
    """Poll this to check if we properly called the requirements install"""
    return INSTALL_PROGRESS


def find_arma():
    """Gets arma installation folder from registry"""
    flags = winreg.KEY_READ
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Wow6432Node\\bohemia interactive\\arma 3", 0, flags)
        (value, valuetype) = winreg.QueryValueEx(key, "main")
        key.Close()
        return value
    except Exception:
        return None


def install_cmd():
    """Install from simple CMD"""
    arma = find_arma()

    force = len(sys.argv) > 1 and "--force" in sys.argv[1:]
    if arma:
        pythia = Path(arma) / "!Workshop" / "@Pythia"
        if pythia.is_dir():
            actual_folder = pythia.resolve()  # The other one is a symlink
            install(path=(actual_folder / "python-37-embed-amd64" / "python.exe"), force=force)
        else:
            print("Can't find @Pythia in arma workshop folder")
    else:
        print("Can't find Arma path in registry")


if __name__ == "__main__":
    install_cmd()
