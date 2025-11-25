install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/

format:
	# (Optional) Falls du Code-Formatierung nutzen möchtest
	# pip install black
	# black src/ tests/
	echo "Formatting step (skipped for now)"

clean:
	rm -rf __pycache__ .pytest_cache
	rm -rf src/*.egg-info
