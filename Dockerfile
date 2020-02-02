FROM ubuntu:18.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3.6 python3-pip

RUN pip3 install flask
RUN pip3 install flask-wtf
RUN pip3 install pymongo dnspython
RUN pip3 install requests


WORKDIR "/dinner-party"
ENTRYPOINT ["python3.6"]
CMD ["main.py"]