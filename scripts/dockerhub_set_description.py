#!/usr/bin/env python

"""
This is a script that sets the description of an image repository in docker hub
"""

import json
import requests


def main():
    """ This function does all the work """
    # Your Docker Hub username and password
    username = "your_docker_hub_username"
    password = "your_docker_hub_password"

    # The repository you want to update
    repo_name = "your_repo_name"

    # Docker Hub API endpoint for updating repository description
    api_endpoint = \
        f"https://hub.docker.com/v2/repositories/{username}/{repo_name}/"

    # New repository description
    new_description = \
        "This is an updated description for my Docker repository."

    # Authenticate with Docker Hub
    auth_url = "https://hub.docker.com/v2/users/login/"
    auth_data = {"username": username, "password": password}
    auth_response = requests.post(
            auth_url,
            data=json.dumps(auth_data),
            timeout=5,
    )
    access_token = auth_response.json()["token"]

    # Update the repository description
    update_data = {
        "description": new_description
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"JWT {access_token}"
    }
    response = requests.patch(
            api_endpoint.format(username=username, repo_name=repo_name),
            data=json.dumps(update_data),
            headers=headers,
            timeout=5,
    )

    if response.status_code == 200:
        print("Repository description updated successfully!")
    else:
        print("Failed to update repository description")
        print(f"{response.status_code} - {response.text}")


if __name__ == "__main__":
    main()
