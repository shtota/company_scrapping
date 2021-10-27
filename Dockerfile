FROM python:3.8

WORKDIR /code

ARG CHUNK=14

COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

ADD scrapy.cfg .

ADD gospider.py .

ADD /companies/ ./companies/

ADD /targets/${CHUNK}.csv ./targets/

CMD python gospider.py ${CHUNK}

COPY ./${CHUNK}.json .