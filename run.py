#!/usr/bin/env python3
import os
import os.path as op
import json
import logging

import flywheel
from gear_toolkit import gear_toolkit_context
from gear_toolkit import command_line
from utils import args

log = logging.getLogger(__name__)

if __name__ == '__main__':
    with gear_toolkit_context.GearToolkitContext() as context:
        # Activate custom logger
        context.init_logging()

        context.log_config()
        with open('/tmp/gear_environ.json','r') as f:
            environ = json.load(f)

        # Build, Validate, and execute Parameters Hello World 
        try:
            # build the command string
            params = args.build(context)
            args.validate(params)
            args.execute(context, params, environ=environ)

        except Exception as e:
            context.log.fatal(e,)
            context.log.fatal('Error executing pydeface-gear.')
            os.sys.exit(1)

        context.log.info("pydeface-gear completed Successfully!")
        os.sys.exit(0)