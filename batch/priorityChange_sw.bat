@echo off
::ChangePriorityForSWClient
wmic process where name="SoulWorker100.exe" call setpriority 128
pause
