# Build image with:
# docker build . -f .\.devcontainer\Dockerfile --tag imagename:x.x
#
# Create container with:
# docker create --mount source=C:\path-to-my\systempasswords,target=/run/secrets,type=bind,consistency=cached --name containername --dns-search sjrwmd.com imagename:x.x
# or
# docker run -dit --mount source=C:\path-to-my\systempasswords,target=/run/secrets,type=bind,consistency=cached --name containername --dns-search sjrwmd.com imagename:x.x

# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.234.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY /app/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
#RUN apt-get update \
#    && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
#    && pip install -r requirements.txt 

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1

# copy all the application files
WORKDIR /app
COPY app/* .

# The container's default port
# EXPOSE 5000

# Run the application
ENTRYPOINT [ "python","app/app.py" ]
#ENTRYPOINT ["/bin/bash"]