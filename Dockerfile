FROM python:3.9.12-bullseye

WORKDIR /backend

COPY . .
RUN pip install -r requirements.txt
ENV FLASK_ENV=production
ENV PYTHONPATH "${PYTHONPATH}:/backend/src"

ENV MYSQL_HOST=localhost
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root
ENV MYSQL_DATABASE=yearsinpixels

EXPOSE 5555
CMD ["python3", "/backend/src/yearsinpixels_api/Main/Main.py"]