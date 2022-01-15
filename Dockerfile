FROM python:3.8.10

RUN mkdir -p /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]