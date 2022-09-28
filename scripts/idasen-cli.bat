@ECHO OFF


WT -d %CD% -p "PowerShell 5" --title "Server" server.bat ; nt -d %CD% -p "PowerShell 5" --title "Idasen CLI" client.bat
