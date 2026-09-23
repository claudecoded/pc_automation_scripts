@echo off
echo Deleting temporary files...

del /q /f /s "%USERPROFILE%\AppData\Local\Temp\*.*"
for /d %%i in ("%USERPROFILE%\AppData\Local\Temp\*") do rmdir /s /q "%%i"

del /q /f /s "C:\Windows\Temp\*.*"
for /d %%i in ("C:\Windows\Temp\*") do rmdir /s /q "%%i"

del /q /f /s "C:\Windows\Prefetch\*.*"
for /d %%i in ("C:\Windows\Prefetch\*") do rmdir /s /q "%%i"

echo Cleanup completed successfully!
pause
