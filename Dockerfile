FROM danielgran/debian-base
RUN wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-py3_8.0.29-1debian10_amd64.deb && \
    apt install -y default-libmysqlclient-dev python3.9 python3-pip python3-protobuf python3-distutils && \
    dpkg -i mysql-connector-python-py3_8.0.29-1debian10_amd64.deb

WORKDIR /backend

COPY . .
RUN pip install -r requirements.txt
ENV FLASK_ENV=production
ENV PYTHONPATH "${PYTHONPATH}:/backend/src"

EXPOSE 5555
CMD ["python3", "/backend/src/yearsinpixels_api/Main/Main.py"]