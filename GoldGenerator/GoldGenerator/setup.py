from cx_Freeze import setup, Executable

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "GoldGenerator",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]GoldGenerator.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),

    ("StartupShortcut",        # Shortcut
     "StartMenuFolder",          # Directory_
     "GoldGenerator",          # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]GoldGenerator.exe",   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )

    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

build_exe_options = {"excludes": ["tkinter", "PyQt5.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt5.QtNetwork",
                                  "PyQt5.QtScript",
                                  "numpy.core._dotblas"],
                     "include_files" : ['GoldGenerator.ico'],
                     "optimize": 2}


setup(
    name = "GoldGenerator",
    version = "2.0",
    description = "GoldGenerator",
    options = {"build_exe": build_exe_options,
               "bdist_msi": bdist_msi_options},
    executables = [Executable("GoldGenerator.py", base = "Win32GUI", icon="GoldGenerator.ico")])
