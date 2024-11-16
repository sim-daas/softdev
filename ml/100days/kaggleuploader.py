from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate
api = KaggleApi()
api.authenticate()

# Create a new version
dataset_name = "indian-stocks"
api.dataset_version_create(dataset_name, "Your new version description")

# Upload a new file
local_path = "screener.csv"
remote_path = f"{dataset_name}/stocks.csv"
api.dataset_upload_file(dataset_name, remote_path, local_path)

# Commit changes
api.dataset_commit_changes(dataset_name)
