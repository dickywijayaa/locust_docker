FROM python:3.8
 
RUN mkdir -p /locust /build
RUN chmod -R 777 locust/ /build
 
RUN git clone -b 1.4.1 https://github.com/locustio/locust.git /build
RUN cd /build && pip install . && rm -rf /build
 
WORKDIR /locust
 
EXPOSE 8089 5557
 
ENV PYTHONUNBUFFERED=1