FROM python:3.9.12-bullseye

WORKDIR /backend

COPY . .
RUN pip install -r requirements.txt
ENV FLASK_ENV=production
ENV PYTHONPATH "${PYTHONPATH}:/backend/src"
EXPOSE 9090
CMD ["python3", "/backend/src/yearsinpixels_api/Main/Main.py"]