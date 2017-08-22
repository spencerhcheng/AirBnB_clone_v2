#!/usr/bin/python3
"""
Generates a tgz archive file from web_static
"""
import os
from datetime import datetime
import tarfile
from fabric.api import *
env.use_ssh_config = True


def do_pack():
    local("sudo mkdir -p ./versions", capture=False)
    file_name = "web_static_" + datetime.now().\
        strftime("%Y%m%d%H%M%S") + ".tgz"
    local("sudo tar zcvf './versions/{}' web_static"
          .format(file_name), capture=False)
    if not os.path.exists("./versions/{}".format(file_name)):
        return None
    else:
        return "./versions/{}".format(file_name)
