# Inheriting from established docker image:
FROM poldracklab/pydeface:37-2e0c2d

# Inheriting from established docker image:
LABEL maintainer="Flywheel <support@flywheel.io>"

# Flywheel gears are run as root
# poldracklab/pydeface:37-2e0c2d leaves it in the "neuro" user
USER root

# For interactive docker... Not needed in gear execution
RUN head -n 7 /neurodocker/startup.sh >> ~/.bashrc

ENV FLYWHEEL /flywheel/v0
WORKDIR ${FLYWHEEL}

ENV PATH=/opt/conda/envs/neuro/bin/:$PATH
COPY requirements.txt $FLYWHEEL/
RUN pip install -r requirements.txt

# Copy executable, manifest, and tools to Gear
COPY run.py manifest.json ${FLYWHEEL}/
COPY utils ${FLYWHEEL}/utils
RUN chmod a+x ${FLYWHEEL}/run.py

RUN python -c "import os, json; f = open('/tmp/gear_environ.json', 'w');json.dump(dict(os.environ), f)"

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run.py"]
