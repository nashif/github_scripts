#!/usr/bin/env python3

import argparse
from github import Github
from git import Git
import os
import sys
import semantic_version

GH_TOKEN = os.environ.get('GITHHUB_TOKEN', None)

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        "-p",
        "--pull-request",
        required=True,
        type=int,
        help="Pull request number")
    parser.add_argument(
        "-d",
        "--git-repo",
        default=".",
        help="Local directory of the git repository (default=local directory)")

    parser.add_argument(
        "-g",
        "--github-repo",
        default="zephyrproject-rtos/zephyr",
        help="Github repository (owner/repo) default=zephyrproject-rtos/zephyr")


    args = parser.parse_args()
    if GH_TOKEN:
        g = Github(GH_TOKEN)
    else:
        sys.exit("GITHUB_TOKEN not found in environment. export GITHUB_TOKEN and retry")

    repo = g.get_repo(args.github_repo)


    git_tree = args.git_repo
    g = Git(git_tree)

    pr = repo.get_pull(args.pull_request)
    for commit in pr.get_commits():
        print(commit.sha)
        describe = g.describe(["--contains", commit.sha])
        print(describe)
        #v = semantic_version.Version(describe)

if __name__ == '__main__':
    main()