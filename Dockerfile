FROM ubuntu:22.04

# Update system
RUN apt update -y && apt upgrade -y

# Setup of ffmpeg and git
RUN apt install ffmpeg -y && apt install git -y

# Python 3.10 setup
RUN apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa -y

# Install pip and the moviepy module
RUN apt-get -y install python3-pip && pip install --upgrade pip && pip install moviepy

# Setup the git repo
RUN mkdir /var/app && cd /var/app/ && git clone https://github.com/sofackj/ffmpeg-test.git 
