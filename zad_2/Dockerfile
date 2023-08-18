FROM python:3.9.12-slim
WORKDIR /measurement/
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip \
    && python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt
