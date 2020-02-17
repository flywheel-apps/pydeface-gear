
# Inheriting from established docker image:
FROM poldracklab/pydeface:37-2e0c2d

# Inheriting from established docker image:
LABEL maintainer="Flywheel <support@flywheel.io>"

# Flywheel gears are run as root
# poldracklab/pydeface:37-2e0c2d leaves it in the "neuro" user
USER root

# Install APT dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \ 
    zip  && \ 
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# For interactive docker... Not needed in gear execution
RUN head -n 7 /neurodocker/startup.sh >> ~/.bashrc

# All the neuro-conda environment commands must be executed
# within bash. conda does not have a sh-shell configuration
RUN /bin/bash -c "\
    source activate neuro && \
    pip install \
    flywheel-sdk==11.0.1 \
    flywheel-gear-toolkit==0.0.1.dev1 \
    "

# Make directory for flywheel spec (v0):
ENV FLYWHEEL /flywheel/v0
WORKDIR ${FLYWHEEL}
# Copy executable/manifest to Gear
COPY run.py ${FLYWHEEL}/run.py
RUN chmod a+x run.py
COPY utils utils
COPY manifest.json ${FLYWHEEL}/manifest.json

# ENV preservation for Flywheel Engine
# Again, these env are preserved in the bash shell
RUN /bin/bash -c "\
    source activate neuro && \
    source /neurodocker/startup.sh && \
    python -c \
    \"import os, json; f = open('/tmp/gear_environ.json', 'w');\
    json.dump(dict(os.environ), f)\"\
    "

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run.py"]
