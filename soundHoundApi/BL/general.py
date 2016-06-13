"""


"""
import os


def get_git_branch(path=None):
    """
    Read the git branch from git config file and return it.
    :return: project branch name.-
    """

    api_name = 'soundHound'

    if path is None:
        path = os.path.abspath(__file__)

    with open(path[:path.rfind(api_name)] + '.git\\config', 'r') as file:
        for line in file:
            if 'branch' in line:
                branch = line[line.find('branch "') + 8:-3]
                return branch

    raise Exception('Could not discover git branch name..')
