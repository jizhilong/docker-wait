FROM python:2.7.13
MAINTAINER jizhilong <zhilongji@gmail.com>


ADD dresponse/requirements.txt /usr/local/src/dresponse/requirements.txt

RUN pip install -r /usr/local/src/dresponse/requirements.txt

CMD ["uwsgi", "--http-socket", "/var/run/dresponse/dresponse.sock", "-w", "dresponse.wsgi"]

ADD dresponse /usr/local/src/dresponse
ADD dwait/bin.tar /usr/lib/dwait
RUN pip install /usr/local/src/dresponse &&\
    mkdir -p /var/lib/dresponse/ &&\
    cp -R /usr/local/src/dresponse/bin/default-dresponse-scripts /var/lib/dresponse/pre_start
ENTRYPOINT ["/usr/local/src/dresponse/bin/entrypoint"]
