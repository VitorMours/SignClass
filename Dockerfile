FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt



COPY /backend .

ENV PORT=8000
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
