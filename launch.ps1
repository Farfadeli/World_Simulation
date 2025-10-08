param ($name,$population, $gap, $limit)


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