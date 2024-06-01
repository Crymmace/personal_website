FROM python:3.9-slim

WORKDIR /Users/crystal/source/docker/personal_website/personal_website

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir .streamlit
RUN bash -c 'echo -e "\
[ui]\n\
hideTopBar = true\n\
" > .streamlit/config.toml'

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 10000

HEALTHCHECK CMD curl --fail http://localhost:10000/_stcore/health

ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=10000", "--server.address=0.0.0.0"]

