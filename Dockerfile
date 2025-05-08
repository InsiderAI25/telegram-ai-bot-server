FROM python:3.9-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip==22.3.1
RUN pip install -r requirements.txt

# Copy bot server code
COPY main_bot_server.py .

# Expose port and run app
EXPOSE 5000
CMD ["python", "main_bot_server.py"]
