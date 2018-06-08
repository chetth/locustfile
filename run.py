import os
import typing
import json
import subprocess
import sys
from argparse import ArgumentParser


def parse(args: list = None) -> dict:
    """ """

    with open('/scripts/locust.config.json') as f:
        configs: dict = json.load(f)

    parser = ArgumentParser()

    parser.add_argument(
        '--master-host',
        dest='master_host',
        default=None,
        help='The hostname/ip of the master instance'
    )

    configs.update(vars(parser.parse_args(args)))
    configs['is_master'] = (configs['master_host'] is None)
    return configs


def get_locust_file(args: list = None) -> typing.Union[str, None]:
    """ """

    for filename in args:
        path = os.path.join('/scripts', filename)
        if os.path.exists(path):
           return path

    return None


def make_command(args: dict) -> str:
    """ """

    cmd = [
        'locust',
        '-f', '"{}"'.format(get_locust_file(args['profile'])),
        '--master' if args['is_master'] else '--slave',
        '--host={}'.format(args['target'])
    ]

    if not args.get('is_master'):
        cmd.append('--master-host={}'.format(args['master_host']))

    try:
        locusts = args['locusts']
        cmd += [locusts] if hasattr(locusts, 'find') else locusts
    except Exception:
        print('[ERROR]: Invalid or missing "locusts" config attribute')
        raise

    return ' '.join(cmd)


def run():
    args = parse()

    process = subprocess.Popen(
        args=make_command(args),
        stdout=sys.stdout,
        shell=True,
        universal_newlines=True
    )

    process.wait()


if __name__ == '__main__':
    run()
