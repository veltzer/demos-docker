"""
os level dependencies for this project
"""

import platform


desktop = platform.freedesktop_os_release()
VERSION_ID = desktop["VERSION_ID"]


packages_remove = []

if VERSION_ID == "22.04":
    # because of conflict with containerd which is needed by "docker.io" below
    packages_remove.append("containerd.io")


packages = [
    # for compiling .net
    "dotnet-sdk-8.0",
    # spell check md files
    "aspell",
    # lint .sh and .bash files
    "shellcheck",
    # ruby stuff
    "ruby-bundler",
    "rbenv",
    # for scratch exercises
    "bash-static",
    # for docker
    "docker.io",
    # "docker-compose",
    # "docker-doc",
    # "docker-buildx",
    # "docker-clean",
    # "docker-registry",
]
