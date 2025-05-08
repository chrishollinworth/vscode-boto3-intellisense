FROM python:latest

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY create_stubs.sh create_stubs.sh
COPY get_aws_services.py get_aws_services.py

RUN apt-get update
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

RUN pip3 install  --upgrade boto3 botocore jinja2 pyparsing black mdformat isort setuptools loguru prompt-toolkit questionary requests ruff uv

RUN python3 get_aws_services.py

RUN git clone https://github.com/chrishollinworth/mypy_boto3_builder.git

RUN ./mypy_boto3_builder/scripts/build.sh
RUN ./mypy_boto3_builder/scripts/install.sh
RUN chmod +x create_stubs.sh
RUN ./create_stubs.sh


CMD ["python3", "-m", "http.server", "8000"]