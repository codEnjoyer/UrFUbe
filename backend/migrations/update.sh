#!/bin/bash

cd ../

alembic revision --autogenerate

alembic upgrade head
