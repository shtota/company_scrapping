FROM python:3.8

WORKDIR /code

ARG CHUNK=0

COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

ADD /companies/ .

ADD /targets/${CHUNK}.csv ./targets/

CMD ['scrapy', 'crawl', 'company', '-o ${CHUNK}.json -L INFO -a chunk=${CHUNK}']