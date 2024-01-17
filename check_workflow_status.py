import requests
import time
import os
import sys

def check_workflow_status(repo_name, workflow_name, github_token):
    url = f"https://api.github.com/repos/{repo_name}/actions/runs"
    headers = {"Authorization": f"token {github_token}"}

    while True:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Failed to fetch workflow data", response.text)
            sys.exit(1)

        runs = response.json()["workflow_runs"]
        workflow = next((run for run in runs if run["name"] == workflow_name), None)

        if not workflow:
            print(f"No workflow named '{workflow_name}' found")
            sys.exit(1)

        if workflow["status"] == "completed":
            if workflow["conclusion"] == "success":
                print("Workflow completed successfully")
                break
            else:
                print(f"Workflow completed with conclusion: {workflow['conclusion']}")
                sys.exit(1)
        print("Workflow is still running... waiting")
        time.sleep(60)  # Poll every 60 seconds

if __name__ == "__main__":
    repo_name = "retrotink-llc/firmware"
    workflow_name = "pages-build-deployment"
    github_token = os.getenv("GITHUB_TOKEN")

    check_workflow_status(repo_name, workflow_name, github_token)