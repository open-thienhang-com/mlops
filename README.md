<div align="center">
  <a href="https://thienhang.com">
    <img src="images/a.png" alt="Logo">
  </a>

  <h1 align="center">MLOps</h1>

  <p align="center">
    <a href="thienhang.com">View Demo</a>
    ·
    <a href="https://hub.docker.com/r/thienhang/open.thienhang.com">Docker Hub</a>
    ·
    <a href="https://thienhang.com">Request Feature</a>
  </p>
</div>


Update your package index:


```
sudo apt update
sudo apt install python3 python3-pip

python3 --version

nano ~/.bashrc


```
Add the following line to the end of the file:

```
alias python='python3'

```

Save and close the file.

To apply the changes immediately, source your .bashrc file:

```

source ~/.bashrc

```


python3 -m venv .venv

source .venv/bin/activate

deactivate


``` shell
pip install poetry

poetry env list

poetry env use python3

poetry install

poetry add requests

poetry run python services/examples/http/__init__.py

poetry export --output requirements.txt

poetry shell

poetry show

```

## Local development
To allow ease of development, a `pyproject.toml` is placed at the root of the project, referencing all sub-modules as dependencies. This allows your editor to use one virtual environment for all the modules. 

Install locally with
```shell
poetry install
```
and run e.g.
```
poetry run python src/service1/service1/main.py
```

## Docker
Each service has its own Dockerfile (`service1.Dockerfile` & `service2.Dockerfile`) that can be used for easy deployment. 

Additionally, `docker-compose.yaml` is defining how to build and run both services. This allows easy testing of the Docker deployment, locally. 
Run both with `docker compose up`.