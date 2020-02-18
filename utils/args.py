import os.path as op
from collections import OrderedDict

from gear_toolkit.command_line import build_command_list, exec_command


def build(context):
    # use Ordered Dictionary to keep the order created.
    # Default in Python 3.6 onward
    params = OrderedDict()
    config = context.config
    for key in config.keys():
        params[key] = config[key]

    infile = context.get_input_path('infile')

    params['outfile'] = context.output_dir / \
        op.basename(infile).replace('.nii.gz', '_defaced.nii.gz')
    return params


def validate(params):
    """
    validate the given parameters against potential conflicts

    Args:
        params (dict): dictionary of pydeface parameters
    """
    pass


def execute(context, params, dry_run=False, environ=None):
    # Get Params
    command = ['pydeface']

    # Build command-line parameters
    command = build_command_list(command, params)

    # Extend with positional arguments
    command.append(context.get_input_path('infile'))

    exec_command(command, environ=environ)
