# This dockerfile generates a container with the needed dependencies to build the theme

FROM python:alpine

RUN apk add sassc inkscape optipng

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

# The reason for this is to allow the GH Actions Workflow execute commands within the container
CMD ["sleep", "infinity"]
