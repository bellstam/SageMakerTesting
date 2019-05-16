FROM python:3.6

# set the working directory
RUN ["mkdir", "app"]
WORKDIR "app"

ADD . /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

# install code dependencies
COPY "requirements.txt" .

RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt --no-cache-dir --no-binary :all:

RUN pip install -e .

# provision environment
ENV FLASK_APP app.py

EXPOSE 8080

CMD ["python", "app.py"]
