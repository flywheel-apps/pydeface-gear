#!/usr/bin/env python3
import os
import logging
from nipype.interfaces.base import File, traits, CommandLineInputSpec, CommandLine

from gear_toolkit import gear_toolkit_context


log = logging.getLogger(__name__)


class PyDefaceInputSpec(CommandLineInputSpec):
    infile = File(exists=True,
                  argstr='%s',
                  position=-1,
                  mandatory=True,
                  desc='Path to input nifti.')
    template = File(exists=True,
                    argstr='--template %s',
                    mandatory=False,
                    desc='Optional template image that will be used as the registration ""target instead of the '
                         'default.')
    facemask = File(exists=True,
                    argstr='--facemask %s',
                    mandatory=False,
                    desc='Optional face mask image that will be used instead of the default.')
    cost = traits.Enum('mutualinfo', 'corratio', 'normcorr', 'normmi', 'leastsq', 'labeldiff', 'bbr',
                       argstr='--cost %s', desc='FSL-FLIRT cost function. Default is <mutualinfo>',
                       usedefault=True)
    nocleanup = traits.Bool(argstr='--nocleanup',
                            desc='Do not cleanup temporary files. Off by default.')
    verbose = traits.Bool(argstr='--verbose',
                          desc='Do not catch exceptions and show exception traceback (Drop into pdb debugger).')


class PyDeface(CommandLine):
    _cmd = 'pydeface'
    input_spec = PyDefaceInputSpec


def main(context):
    try:
        # Instantiate node
        pydef = PyDeface()

        # Connect input node to config
        pydef.inputs.infile = context.get_input_path('infile')
        if context.get_input_path('template'):
            pydef.inputs.template = context.get_input_path('template')
        if context.get_input_path('facemask'):
            pydef.inputs.facemask = context.get_input_path('facemask')
        pydef.inputs.cost = context.config.get('cost')
        pydef.inputs.nocleanup = context.config.get('nocleanup')
        pydef.inputs.verbose = context.config.get('verbose')

        # Run
        log.info(pydef.cmdline)
        pydef.run()

    except Exception as e:
        context.log.exception(e)
        context.log.fatal('Error executing pydeface-gear.')
        return 1

    context.log.info("pydeface-gear completed Successfully!")
    return 0


if __name__ == '__main__':
    with gear_toolkit_context.GearToolkitContext() as gear_context:
        gear_context.init_logging()
        gear_context.log_config()
        exit_status = main(gear_context)

    log.info('exit_status is %s', exit_status)
    os.sys.exit(exit_status)
