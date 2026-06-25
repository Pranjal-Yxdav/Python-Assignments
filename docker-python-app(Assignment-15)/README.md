# Dockerized Python Application

This project uses the **python:3.12-slim** Docker image to run a Python application that displays the current Python version, date, and time.

## Build the Docker Image

```bash
docker build -t python-version-app .
```

## Run the Docker Container

```bash
docker run --rm python-version-app
```

## Sample Output

```
Python Version : 3.14.5
Current Date   : DD-MM-YYYY
Current Time   : HH:MM:SS
```


