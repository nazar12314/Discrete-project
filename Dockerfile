# Dockerfile for the discrete project
# syntax=docker/dockerfile:1
FROM node:latest
RUN mkdir /app
WORKDIR /app
ENV PATH ./frontend/node_modules/.bin:$PATH
EXPOSE 3000
EXPOSE 8080

RUN apt-get update && apt-get install -y python3 \
    python3-pip
RUN pip install flask jsonify requests
COPY ./ .
