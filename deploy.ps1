mkdir configuration\logs -Force

## Create and activate virtual environment for package management ##
python -m venv venv
python -m pip install venv-run
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

## Stop/Remove old acronyms service ##
$serviceName = 'acronyms'
If (Get-Service $serviceName -ErrorAction SilentlyContinue)
{
    If ((Get-Service $serviceName).Status -eq 'Running') {
        nssm stop $serviceName
        nssm remove $serviceName confirm
    } Else {
        nssm remove $serviceName confirm
    }
}

## Create Slack App Executable ##
pyinstaller --onefile --log-level=ERROR .\app.spec
Move-Item .\dist\acronyms.exe -Force

## Create acronyms service and start Slack App ##
start-sleep -s 20
nssm install acronyms #{acronymsPath}\acronyms.exe
start-sleep -s 20
nssm set acronyms ObjectName DOMAIN\#{serverSvcUsername} "#{serverSvcPassword}"
start-sleep -s 20
nssm start acronyms

## Remove unnecessary stuff ##
Remove-Item .git, acronyms, slackapp, venv, runacronyms.py, app.py, bitbucket-pipelines.yml, requirements.txt, deploy.ps1, RELEASE_VERSION.txt, PACKAGE.txt, .gitignore, app.spec, build, dist, acronyms.ico, __init__.py, acronyms.py, .\__pycache__ -Recurse