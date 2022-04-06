

def resetSettings():
    """
        ["plopper_install.reset.resetSettings"] call PY3_fnc_callExtension
    """

    try:
        from PyQt5.QtCore import QSettings
    except ImportError:
        return "PyQt5 not installed?"
    
    settings = QSettings("Adanteh", "Plopper")
    settings.clear()

def forceReinstall():
    """
        ["plopper_install.reset.forceReinstall"] call PY3_fnc_callExtension
    """
    from plopper_install import install
    install(force=True)
