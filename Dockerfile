FROM python:3.8-slim

WORKDIR /app

COPY . /app

# installs prd dependencies with pipfile.lock and to the system's python
RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile
