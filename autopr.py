#!/usr/bin/env python3

import argparse
from github import Github
from git import Git
import os
import sys
import semantic_version

GH_TOKEN = os.environ.get('GITHUB_TOKEN', None)

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        "-g",
        "--github-repo",
        default="nashif/github_scripts",
        help="Github repository (owner/repo)")


    args = parser.parse_args()
    print(GH_TOKEN)
    if GH_TOKEN:
        g = Github(GH_TOKEN)
    else:
        sys.exit("GITHUB_TOKEN not found in environment. export GITHUB_TOKEN and retry")

    repo = g.get_repo(args.github_repo)

    body = """This is a PR created using a script"""
    pr = repo.create_pull(title="test PR", body=body, head="autopr", base="master")

if __name__ == '__main__':
    main()