import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY = os.path.join(os.path.dirname(__file__), "config", "service-account.json")
PROJECT = os.environ.get("GCP_PROJECT", "sinthec-api-prod")


def _credentials():
    return service_account.Credentials.from_service_account_file(KEY)


def check_target():
    svc = build("cloudresourcemanager", "v1", credentials=_credentials())
    project = svc.projects().get(projectId=PROJECT).execute()
    print(f"deploy target: {project['name']} ({project['projectId']})")


if __name__ == "__main__":
    check_target()
