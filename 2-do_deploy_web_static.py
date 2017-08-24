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

    arch_list = archive_path.split("/")
    arch_name = arch_list[1]
    arch_name_sans = arch_name.split('.')[0]

    if not os.path.exists("{}".format(archive_path)):
        print("Path doesn't exist!")
        return False
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(arch_name_sans))
        run('tar xzf /tmp/{} -C\
            /data/web_static/releases/{}'.format(arch_name, arch_name_sans))
        run('rm /tmp/{}'.format(arch_name))
        run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}'.
            format(arch_name_sans, arch_name_sans))
        run('rm -rf /data/web_static/releases/{}/web_static'.
            format(arch_name_sans))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}\
            /data/web_static/current'.format(arch_name_sans))
        return True
    except Exception as x:
        print(x)
        return False
