FROM stimela/base:0.2.8
MAINTAINER Jonathan Kenyon "jonosken@gmail.com"

RUN docker-apt-install python-casacore

ADD phd-code /src/phd-code

RUN pip install -r src/phd-code/requirements.txt
RUN pip install src/phd-code
