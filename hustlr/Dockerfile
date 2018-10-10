FROM tiangolo/uwsgi-nginx-flask:python3.6


# Install updates
RUN apt-get update


#Install project reqs
RUN pip install --upgrade pip
RUN pip3 install pipenv
RUN pip3 install flask
RUN pip3 install pymongo
RUN pip3 install  hackernews
RUN pip3 install pyphen
RUN pip3 install haxor
RUN pip3 install pytest
RUN pip3 install pylint
RUN pip3 install gunicorn

# Activate directory
ADD . /usr/src/hustlr
WORKDIR /usr/src/hustlr
