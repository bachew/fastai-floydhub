# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import click
from ff import sh


@click.group()
def cmd():
    pass


@cmd.command('setup-courses')
def cmd_setup_courses():
    setup_courses()


@cmd.command('floyd-jupyter')
@click.option('--gpu', is_flag=True, help='Use GPU')
def cmd_floyd_jupyter(gpu):
    start_floyd_jupyter(gpu=gpu)


def setup_courses():
    courses_dir = sh.path('courses')

    if courses_dir.check():
        with courses_dir.as_cwd():
            sh.run(['git', 'clean', '-fd'])
            sh.run(['git', 'pull', 'origin', 'master'])
    else:
        url = 'https://github.com/fastai/courses.git'
        sh.run(['git', 'clone', '--depth', '1', url, courses_dir.strpath])

    sh.run(['pip', 'install', '-r', courses_dir.join('requirements.txt').strpath])


def start_floyd_jupyter(gpu=False):
    cmd = [
        'floyd', 'run',
        '--mode', 'jupyter',
        '--open',
        '--env', 'keras:py2'
    ]

    if gpu:
        cmd.append('--gpu')
    else:
        cmd.append('--cpu')

    data_mounts = [
        ('bachew/datasets/dogscats/1', '/data-dogscats')
    ]

    for data_mount in data_mounts:
        cmd.append('--data')
        cmd.append(':'.join(data_mount))

    sh.run(cmd)


if __name__ == '__main__':
    cmd()
