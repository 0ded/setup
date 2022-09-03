start-process PowerShell -verb runas

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

mkdir c:/temp

Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.0/python-3.10.0.exe" -OutFile "c:/temp/python-3.10.0.exe"

Invoke-WebRequest -Uri "https://github.com/git-for-windows/git/releases/download/v2.37.3.windows.1/Git-2.37.3-64-bit.exe" -OutFile "c:/temp/git.exe"

Invoke-WebRequest -Uri "https://www.mozilla.org/en-US/firefox/download/thanks/" -OutFile "c:/temp/firefox.exe"

echo "installing python"
c:/temp/python-3.10.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

pause

echo "installing git"

c:/temp/git.exe /SP- /VERYSILENT /SUPPRESSMSGBOXES /NOCANCEL /NORESTART /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS

$env:Path += ";c:\Program Files\Git\bin"

pause

echo "installing firefox"
c:/temp/firefox.exe /S

pause


