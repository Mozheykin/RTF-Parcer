FROM python:3.8.10 AS builder

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --user -r requirements.txt

# FROM python:3.8.10-slim

RUN mkdir -p /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5432

#docker run -p 127.0.0.1:80:80
# CMD [ "python", "./main.py", "-f" ]
# docker run -it --rm -e 'ENV1=Save_CSV_in_DataBase' -v /home/legal/github/RTF-Parcer/resources:/usr/src/app/resources --name rtf rtf-parcer
CMD python3 main.py -f $ENV1 -arg $ENV2