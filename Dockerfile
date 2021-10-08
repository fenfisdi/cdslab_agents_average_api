FROM python:3.8-slim-buster
EXPOSE 8080

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app
ENV VIRTUAL_ENV /app/.venv
RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt

WORKDIR ${APP_HOME}

COPY main.py .
COPY docker-entrypoint.sh .
COPY src src
COPY api.json /tmp/api_key.json

ENTRYPOINT ["/bin/bash"]
CMD ["./docker-entrypoint.sh"]
