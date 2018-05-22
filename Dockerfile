FROM python:3.5-slim

WORKDIR /code
RUN mkdir -p /code/modules
RUN apt-get -y update
RUN apt-get -y install git
RUN cd /code && git clone https://github.com/inveniosoftware/invenio.git invenio
RUN cd invenio && pip install .

EXPOSE 5000
CMD ["/bin/bash", "-c", "invenio run -h 0.0.0.0"]
