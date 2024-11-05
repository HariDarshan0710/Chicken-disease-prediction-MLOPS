FROM python:3.8-slim-buster

# Install Azure CLI (optional, if you need Azure CLI tools)
RUN apt update -y && apt install -y curl \
    && curl -sL https://aka.ms/InstallAzureCLIDeb | bash

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
