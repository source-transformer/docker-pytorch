# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.231.1/containers/debian/.devcontainer/base.Dockerfile

# [Choice] Debian version (use bullseye on local arm64/Apple Silicon): bullseye, buster
ARG VARIANT="buster"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -qq install 

#RUN apt-get update && apt-get install -y \
#    python3 &&\
#    python3-pip &&\

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN pip3 install torch torchvision python3-matplotlib

RUN pip3 install torch torchvision
#RUN pip3 install python3-matplotlib
#python3 -m pip install 

#COPY setupPython.sh /opt/src/scripts/setupPython.sh
#RUN /opt/src/scripts/setupPython.sh

