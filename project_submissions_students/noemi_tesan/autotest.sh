#!/bin/bash

# Fehler sofort melden, wenn ein Befehl fehlschlägt
set -e

echo "🔧 Installing dependencies..."
pip install -r requirements.txt
pip install -e .

echo "🧪 Running tests..."
pytest tests/

echo "✅ All tests passed!"
