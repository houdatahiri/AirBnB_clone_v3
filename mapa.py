
#!/usr/bin/python3
"""A Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""

from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.144.140.209', '34.202.233.3']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web files to server
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive to the /tmp/dir of web_server
        put(archive_path, '/tmp/')

        # create target dir
        time = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
                releases/web_static_{}/'.format(time))

        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
                /data/web_static/releases/web_static_{}/'
                .format(time, time))

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(time))

        # move contents into host web_static
        run('sudo mv -r /data/web_static/releases/web_static_{}/webs_static/* \
                /data/web_static/releases/web_static_{}/'.format(time, time))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
                .format(time))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run('sudo ln -s /data/web_static/releases/web_static_{}/ \
                /data/web_static/current'.format(time))
    except:
        return False

    # return True on success
    return True

