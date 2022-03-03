FROM python:latest
COPY requirements.txt /tmp/
RUN apt-get -y update && apt-get install -y git && apt-get install -y pip && apt-get install -y vim
RUN pip install --no-cache-dir -r tmp/requirements.txt
RUN git clone --single-branch --branch master https://github.com/luizgdias/maestro.git 
RUN cd maestro/dfa-lib-python && python setup.py install
CMD ["python", "maestro/main.py"]
RUN python maestro/sources/wf.py
