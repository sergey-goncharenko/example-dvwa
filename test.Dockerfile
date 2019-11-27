FROM python:3

RUN pip install selenium

ADD tests.py /

CMD [ "python", "./tests.py" ]
