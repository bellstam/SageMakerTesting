FROM python:3.6

# set the working directory
RUN ["mkdir", "app"]
WORKDIR "app"

ADD . /app

# install code dependencies
COPY "requirements.txt" .

RUN pip install --upgrade setuptools
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install -e .

# provision environment
ENV FLASK_APP app.py

EXPOSE 8080

#ENTRYPOINT ["/bin/bash"]
CMD ["python", "app.py"]
