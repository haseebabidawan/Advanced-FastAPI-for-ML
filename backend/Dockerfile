#backend/Dockercfile

FROM python:3.10-slim

WORKDIR /app

#Copy Backend Files
COPY ./app /app/


# Install Requirments 
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose FastAPI port
EXPOSE 8000


# Run startup script
CMD ["bash", "start.sh"]