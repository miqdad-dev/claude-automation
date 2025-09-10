# File Organizer Makefile

.PHONY: test run clean install help

help:
	@echo "Available commands:"
	@echo "  install  - Install dependencies (if any)"
	@echo "  test     - Run unit tests"
	@echo "  run      - Run the file organizer with preview"
	@echo "  clean    - Remove temporary files"

install:
	@echo "No external dependencies required for this project"

test:
	@echo "Running tests..."
	python -m pytest tests/ -v || python -m unittest discover tests/ -v

run:
	@echo "Running file organizer with preview..."
	python src/file_organizer.py --preview

clean:
	@echo "Cleaning temporary files..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name ".organizer_history.json" -delete

# Development commands
dev-run:
	python src/file_organizer.py --directory ./sample_files --dry-run

sample-files:
	@mkdir -p sample_files
	@touch sample_files/photo.jpg sample_files/document.pdf sample_files/video.mp4
	@touch sample_files/song.mp3 sample_files/script.py sample_files/archive.zip
	@echo "Created sample files in ./sample_files/"
