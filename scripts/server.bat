@ECHO OFF


POWERSHELL -NoExit -Command ../.venv/Scripts/activate ; idasen-controller --server --config ../cli/config.yaml
