# Ollama Market-Classifier Benchmark
 
Runs the benchmark script against a local Ollama server, fully in Docker.
 
## Run
 
    docker compose up --build
 
This starts three services in order:
 
1. `ollama`: the Ollama server (port 11434, models stored in the `ollama_data` volume).
2. `model-pull`: downloads the model, then exits.
3. `benchmark`: runs `benchmark.py` and prints the results.
The first run downloads the model; later runs reuse the volume.
 
## Use a different model
 
    MODEL=some-model:tag docker compose up --build
 
If you change the model, also change the `model=` argument in `benchmark.py`.
 
## Re-run only the benchmark
 
    docker compose run --rm benchmark
 
## Clean up (also deletes downloaded models)
 
    docker compose down -v