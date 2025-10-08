param ($name,$population, $gap, $limit)


# Check if python and pip is installed
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "Python est deje installe."
}
else {
    Write-Host "Python n'est pas installer, installation en cours..."
    $pythonInstaller = "$env:TEMP\python-installer.exe"
    $url = "https://www.python.org/ftp/python/3.12.6/python-3.12.amd64.exe"

    Invoke-WebRequest -Uri $url -OutFile $pythonInstaller
    Write-Host "Installation silencieuse de Python..."

    Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_pip=1" -Wait

    Write-Host "Python a été installe avec succes."
    Remove-Item $pythonInstaller

}

if (Get-Command pip -ErrorAction SilentlyContinue) {
    Write-Host "pip est disponible."
} else {
    Write-Host "pip n'est pas détecte. Tentative d'installation..."
    python -m ensurepip --upgrade
    Write-Host "pip installe via ensurepip."
}


# create python venv if not exist and activate it

if(!(Test-path -Path "./world_sims")){
    python -m venv world_sims
    ./world_sims/Scripts/activate
    pip install -r requirements.txt
    Write-Host "---------------------------------------------------------------------------------"
    Write-Host "L'environnement virtuel vient d'etre configurer"
    Write-Host "---------------------------------------------------------------------------------"
} else {
    Write-Host "---------------------------------------------------------------------------------"
    Write-Host "L'environnement virtuel est deja configurer"
    Write-Host "---------------------------------------------------------------------------------"
}


python ./world_simulation.py --name $name --population $population --gap $gap --limit $limit