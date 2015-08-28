from cx_Freeze import setup, Executable
import requests.certs

setup(
    name = "YaP",
    version = "0.1",
    description = "YaP",
    executables = [Executable("yapco.py")],
    data_files=[('',[requests.certs.where()])]
)
