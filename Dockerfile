FROM python:3.9
COPY * .
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python", "bot.py"]
