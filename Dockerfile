FROM python:3.6


# Install updates
RUN apt-get update
#RUN apt-get install -y --upgrade python3-pip
# RUN python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pipenv

# Activate directory
ADD . /usr/src/hustlr
WORKDIR /usr/src/hustlr
#CMD pipenv install --system --deploy

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["python","app.py"]