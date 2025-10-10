#!/bin/bash
set -e

echo "Starting backend services..."

# Optional: Wait for Redis if needed
sleep 3

# Start FastAPI app
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload