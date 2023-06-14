#!/bin/bash
alembic upgrade head
cd src || exit
gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:"$BACK_APP_PORT" --timeout 600