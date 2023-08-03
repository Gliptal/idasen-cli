@ECHO OFF


WT -d %CD% -p "PowerShell 5" --title "Idasen Server" "%CD%/server.bat" ; nt -d %CD% -p "PowerShell 5" --title "Idasen Client" "%CD%/client.bat"
