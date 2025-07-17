# hello-web
Play with fastapi and react, running on pythonanywhere

## Prepare dev env

Steps:
- Create `app` folder, with `main.py`, using fastapi
- Install `uv` tool
- follow doc on [uv fastapi](https://docs.astral.sh/uv/guides/integration/fastapi/).


Run:
```
uv init --app
uv add fastapi --extra standard
```

## Run in dev mode
```
uv run fastapi dev
```

## Prepare deployment to pythonanywhere
Steps:
- open pythonanywhere console](https://www.pythonanywhere.com/) -> Consoles -> New Bash console
- check that `uv` is installed
- clone repo from github
  ```
  git clone https://github.com/catac/hello-web.git
  ```
- prepare app environment
  ```
  cd hello-web/app
  uv sync
  ```
  This should produce the `.venv` folder in project's app
- check howto setup [pythonaywhere with fastapi](https://help.pythonanywhere.com/pages/ASGICommandLine/).
- install the `pa` tool:
  ```
  pip install --upgrade pythonanywhere
  ```
- Command will be:
  ```
  /home/catac/hello-web/.venv/bin/uvicorn --app-dir /home/catac/hello-web/app --uds ${DOMAIN_SOCKET} main:app
  ```
- Create the website
  ```
  pa website create -d catac.pythonanywhere.com -c '/home/catac/hello-web/.venv/bin/uvicorn --app-dir /home/catac/hello-web/app --uds ${DOMAIN_SOCKET} main:app'
  ```
  It should say that the app is live!
  Note that with free account, you can only have one app; if you already have another, delete it first.

- automatically deploy [from github](https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664)
