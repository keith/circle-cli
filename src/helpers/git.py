import subprocess


def current_branch():
    try:
        devnull = open('/dev/null', 'w')
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref",
                                          "HEAD"], stderr=devnull).strip()
    except subprocess.CalledProcessError:
        return None

    if branch == "HEAD":
        return None

    return branch


def current_repo_path():
    try:
        devnull = open('/dev/null', 'w')
        remotes = subprocess.check_output(["git", "remote"],
                                          stderr=devnull).split()
    except subprocess.CalledProcessError:
        return None

    if len(remotes) == 0:
        return None

    remote = remotes[0]
    if "origin" in remotes:
        remote = "origin"

    return _get_url_for_remote(remote)


def _get_url_for_remote(remote):
    url = subprocess.check_output(["git", "remote", "get-url", remote]).strip()
    path = "/".join(url.split("/")[-2:])
    path = path.split(".")[0]
    return path
