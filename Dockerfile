# Pull base image
FROM python:3.7-alpine

# Set environment varibles
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /link_checker

# Install dependencies
RUN pip install --upgrade --no-cache-dir pip \
    && pip install requests

# Copy file
COPY link_checker.py /link_checker

RUN addgroup -S checker \
    && adduser -S checker -G checker \
    && chown -R checker:checker /link_checker

USER checker

ENTRYPOINT ["python", "link_checker.py"]
