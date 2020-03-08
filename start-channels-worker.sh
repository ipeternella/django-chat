#!/bin/bash

echo "Starting worker for channel ${WORKER_CHANNEL}..."
python manage.py runworker ${WORKER_CHANNEL}
