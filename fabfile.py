# -*- coding:utf-8 -*-
from datetime import datetime
from fabric import utils
from fabric.api import *
from fabric.colors import cyan, green, red
from fabric.contrib import files, console
from fabric.contrib.files import exists
import os
import sys
import time


def dh():
    """
    Configura informações de acesso ao servidor do Dreamhost para operações de bootstrap e deploy.
    """
    user     = os.environ.get('DH_USER')
    password = os.environ.get('DH_PASSWORD')
    host     = os.environ.get('DH_HOST')

    env.forward_agent = True
    env.hosts         = [host]
    env.user          = user
    env.password      = password


def bootstrap():
    """
    Instala as bibliotecas básicas para uma aplicação Django.
    """

    ### CRIA OS DIRETÓRIOS NECESSÁRIOS ###
    run('mkdir -p ~/downloads')

    ### INSTALAR PYTHON 2.7.6 ###
    with cd('~/downloads'):
        run('wget http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz')
        run('tar -xzvf Python-2.7.6.tgz')
        with cd('Python-2.7.6'):
            run('./configure --prefix=$HOME/opt')
            run('make')
            run('make install')
            run("echo 'export PATH=$HOME/opt/bin:$PATH' >> ~/.bash_profile")

    ### SETUP TOOLS ###
    with cd('~/downloads'):
        run('wget http://peak.telecommunity.com/dist/ez_setup.py')
        run('python ez_setup.py')

    ### PIP ###
    with cd('~/downloads'):
        run('wget http://pypi.python.org/packages/source/p/pip/pip-1.5.2.tar.gz --no-check-certificate')
        run('tar -xzvf pip-1.5.2.tar.gz')
        with cd('pip-1.5.2'):
            run('python setup.py install')

    ### PYTHON MYSQL ###
    with cd('~/downloads'):
        run('wget http://downloads.sourceforge.net/project/mysql-python/mysql-python/1.2.3/MySQL-python-1.2.3.tar.gz')
        run('tar -xzvf MySQL-python-1.2.3.tar.gz')
        with cd('MySQL-python-1.2.3'):
            run('python setup.py install')

    ### PYTHON PIL ###
    with cd('~/downloads'):
        run('wget http://effbot.org/downloads/Imaging-1.1.7.tar.gz')
        run('tar -xzvf Imaging-1.1.7.tar.gz')
        with cd('Imaging-1.1.7'):
            run('python setup.py install')

    ### VIRTUALENV ###
    with cd('~/downloads'):
        run('wget http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.2.tar.gz --no-check-certificate')
        run('tar -xzvf virtualenv-1.11.2.tar.gz')
        with cd('virtualenv-1.11.2'):
            run('python setup.py install')

