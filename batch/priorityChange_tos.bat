@echo off
::PriorityForXignCodeChange
wmic process where name="BlackCipher.aes" call setpriority 64
::PriorityForTosClientChange
wmic process where name="Client_tos.exe" call setpriority 128
pause
