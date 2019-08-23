FROM python:3.7.3
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]