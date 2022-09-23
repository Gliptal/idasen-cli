@ECHO OFF


POWERSHELL -NoExit -Command .venv/Scripts/activate ; idasen-controller --server --config ./config.yaml
