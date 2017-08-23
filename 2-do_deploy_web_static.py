#!/usr/bin/python3
"""
Distributes an archive to web servers
"""

import tarfile
from fabric.api import *
import os
import sys

# Server username and hostname
env.hosts = ['34.207.108.29', '34.229.54.8']

def do_deploy(archive_path):
    if archive_path is None:
        return False

    args = sys.argv[3]
    arg = args.split('/')[1]
    no_tgz = arg.split('.')[0]

    put('./versions/{}'.format(arg), '/tmp/{}'.format(arg))
    run("sudo tar zxcf '/tmp/{} /data/web_static/releases/{}'.format(arg, no_tgz)")
    local('sudo rm *.tgz ./versions', capture=False)
    local('sudo unlink ./data/web_static/current')
    local("sudo ln -s './data/web_static/releases/{}'.format(no_tgz) /data/web_static/current")

    if not os.path.exists("./data/web_static/releases/{}".format(no_tgz)):
        return False
    else:
        return True
