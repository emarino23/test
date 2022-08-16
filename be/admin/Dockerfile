FROM python:3.9-buster

# Install dependencies:
COPY requirements.txt .
COPY manage.py .
COPY models.py .
COPY src ./src
RUN apt -y update
RUN apt -y install build-essential libpq-dev python3-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
# Run the application:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



