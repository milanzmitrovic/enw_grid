FROM python:3.10

ENV DASH_DEBUG_MODE False
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8050
CMD ["python", "main.py"]

