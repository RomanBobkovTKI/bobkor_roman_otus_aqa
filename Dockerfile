#FROM python:3.13-alpine
FROM python:3.13-slim-bookworm
ENV IS_DOCKER=True

RUN mkdir -p /root/my_tests
WORKDIR /root/my_tests

COPY . /root/my_tests

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/root/my_tests/entrypoint.sh"]