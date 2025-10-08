param ($population, $gap, $limit, $file)


# create python venv if not exist and activate it
python -m venv world_sims
./world_sims/Scripts/activate


python ./world_simulation.py --population $population --gap $gap --limit $limit --file $file