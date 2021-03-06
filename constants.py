DEBUG = True  # Use DEBUG=False in production environment.

CRED_OR_ENVIRON = "cred"  # Read tokens and passwords from environments variables or cred.json file (cred/environ)
CRED_FILE_NAME = "cred.json"

API_CURRENT_VERSION = "1"
API_ENTRYPOINT = f"/api/v{API_CURRENT_VERSION}"
