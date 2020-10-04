FROM python:3

WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install wget
RUN pip install python-magic


CMD ["python","./cmd_application.py"]

