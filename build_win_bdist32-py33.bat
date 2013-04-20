setlocal EnableDelayedExpansion
CALL "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd" /x86 /release
set DISTUTILS_USE_SDK=1
C:\Python33_32bit\python.exe %STATSMODELSDIR%\setup.py bdist_wininst
