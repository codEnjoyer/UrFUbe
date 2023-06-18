#!/bin/bash
alembic upgrade 93ab834200bf
cd src || exit
gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:"$BACK_APP_PORT" --timeout 600