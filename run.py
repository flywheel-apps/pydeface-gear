#!/usr/bin/env python3
import os
import os.path as op
import json
import logging

from gear_toolkit import gear_toolkit_context
from utils import args


log = logging.getLogger(__name__)


def main(context):
    context.log_config()
    with open('/tmp/gear_environ.json','r') as f:
        environ = json.load(f)

    # Build, Validate, and execute Parameters Hello World 
    try:
        # build the command string
        params = args.build(context)
        # validate parameters (Not currently used.)
        # args.validate(params)
        # Execute on those parameters.
        args.execute(context, params, environ=environ)

    except Exception as e:
        context.log.fatal(e,)
        context.log.fatal('Error executing pydeface-gear.')
        return 1

    context.log.info("pydeface-gear completed Successfully!")
    return 0


if __name__ == '__main__':
    with gear_toolkit_context.GearToolkitContext() as gear_context:
        gear_context.init_logging()
        exit_status = main(gear_context)

    log.info('exit_status is %s', exit_status)
    os.sys.exit(exit_status)        
