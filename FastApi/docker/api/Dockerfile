
FROM python:3.9
RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until
RUN rm -rf /var/lib/apt/lists/*
RUN apt update
RUN apt clean

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

