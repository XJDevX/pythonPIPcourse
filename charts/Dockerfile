FROM python:3.9

WORKDIR /charts
COPY requirements.txt /charts/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /charts/requirements.txt

COPY . /charts

CMD bash -c "while true; do sleep 1; done"
