from cx_Freeze import setup, Executable
import requests.certs

build_exe_options = {"packages": ["os", "PyQt5.QtNetwork"]}
setup(
    name = "YaP",
    version = "0.1",
    description = "YaP",
    executables = [Executable("yap_main.pyw")],
    data_files=[('',[requests.certs.where()])]
)
