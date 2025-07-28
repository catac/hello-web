import dotenv
import logging
import os

dotenv.load_dotenv()

repo_dir = os.environ["REPO_DIR"]
pa_api_token = os.environ["PA_API_TOKEN"]
twelvedata_api_key = os.environ["TWELVEDATA_API_KEY"]
https_proxy = os.environ.get("HTTPS_PROXY")

logger = logging.getLogger("uvicorn.error")
logger.propagate = False  # Prevent duplicate logging from root logger
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s [%(filename)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
