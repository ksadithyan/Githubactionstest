FROM python:3.9-slim

WORKDIR /app

# Copy everything from your folder into the container
COPY . .

# Install everything listed in our shopping list
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]