FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN mkdir -p /usr/src/emp_dep
WORKDIR /usr/src/emp_dep

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/emp_dep/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./emp_dep /usr/src/app
