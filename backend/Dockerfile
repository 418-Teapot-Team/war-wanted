FROM python:3.11-bullseye

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

EXPOSE 8001

CMD ["flask", "--app=backend/app.py", "run", "--host=0.0.0.0", "--port=8001"]
