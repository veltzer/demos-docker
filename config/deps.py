"""
os level dependencies for this project
"""
packages_remove = [
    # because of conflict with containerd which is needed by "docker.io" below
    "containerd.io",
]

packages = [
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
