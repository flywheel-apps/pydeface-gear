#!/usr/bin/env python3
import os
import os.path as op
import json
import logging

from gear_toolkit import gear_toolkit_context
from utils import args


log = logging.getLogger(__name__)


def main(context):
    # Build and Execute Parameters
    try:
        # build the command string
        params = args.build(context)

        # Execute on those parameters.
        args.execute(context, params)

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
