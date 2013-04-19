set STATSMODELSDIR=C:\Users\skipper\statsmodels\statsmodels-skipper
set BUILDDIR=C:\Users\skipper\statsmodels\build_scripts
set BRANCH=fix-build-issues

psftp.exe -i C:\Users\skipper\ssh\sourceforge.ppk jseabold,statsmodels@web.sourceforge.net -b %BUILDIR%\list_remote_directory.scr > %BUILDDIR%\remote_file_list.out

rem Change to statsmodels dir update and checkout branch
chdir /d %STATSMODELSDIR%
git pull --ff-only
git checkout %BRANCH%
git clean -xdf

call python %BUILDDIR%
if errorlevel 1 (
    rem Build the binaries
    call %BUILDDIR%\build_win_bdist64-py26.bat
    call %BUILDDIR%\build_win_bdist32-py26.bat
    call %BUILDDIR%\build_win_bdist64-py27.bat
    call %BUILDDIR%\build_win_bdist32-py27.bat
    call %BUILDDIR%\build_win_bdist32-py32.bat
    call %BUILDDIR%\build_win_bdist64-py32.bat
    call %BUILDDIR%\build_win_bdist32-py33.bat
    call %BUILDDIR%\build_win_bdist64-py33.bat
    call python %STATSMODELSDIR%\setup.py sdist --formats=zip,gztar
    
    rem Rename the built files to contain the git revision
    call python %BUILDDIR%\rename_binaries.py
    
    rem Remove old files
    psftp.exe -i C:\Users\skipper\ssh\sourceforge.ppk jseabold,statsmodels@web.sourceforge.net -b %BUILDDIR%\delete_remote_binaries.scr
    rem Upload new ones
    pscp.exe -i C:\Users\skipper\ssh\sourceforge.ppk %STATSMODELSDIR%\dist\* jseabold,statsmodels@web.sourceforge.net:htdocs/binaries/
    
    rem Email that everything went okay
    call python %BUILDDIR%\email_update.py 
)
