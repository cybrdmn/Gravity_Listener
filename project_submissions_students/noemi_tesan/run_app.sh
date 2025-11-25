#!/bin/bash

# 1. Start the API in the background (&)
# We use --host 0.0.0.0 so it is accessible from outside the container
uvicorn gravity_listener.main:app --host 0.0.0.0 --port 8000 &

# 2. Start Streamlit in the foreground
streamlit run src/gravity_listener/frontend.py --server.port 8501 --server.address 0.0.0.0
