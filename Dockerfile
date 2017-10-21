FROM python:3.6

RUN pip3 install virtualenv

RUN mkdir environments && cd environments
run virtualenv env && . env/bin/activate

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

COPY . /usr/src/app

CMD ["python", "app.py"]

