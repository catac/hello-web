# hello-web
Play with fastapi and react, running on pythonanywhere

## Prepare dev env
- Install `uv` tool
- Clone this repo
- Sync python virtual environment
  ```
  uv sync
  ```
- follow doc on [uv fastapi](https://docs.astral.sh/uv/guides/integration/fastapi/).
  ```
  uv run fastapi dev
  ```

## Prepare deployment to pythonanywhere
- open [pythonanywhere](https://www.pythonanywhere.com/) -> Consoles -> New Bash console
- check that `uv` is installed
- clone repo from github
  ```
  git clone https://github.com/catac/hello-web.git
  ```
- prepare app environment
  ```
  cd hello-web
  uv sync
  ```
  This should produce the `.venv` folder in project's app
- create an environment file `.env`:
  ```
  REPO_DIR = "/home/catac/hello-web"
  ```

### Check howto setup pythonanywhere with FastAPI
- check [this guide](https://help.pythonanywhere.com/pages/ASGICommandLine/).
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

### Check how to deploy automatically from GitHub
- automatically deploy [from github](https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664)
