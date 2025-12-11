# Project settings
APP_NAME = antigravity_demo
VENV = .antigravity_demo
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

DOCKER_IMAGE = antigravity-demo
DOCKER_CONTAINER = antigravity-demo-container
PORT = 8000


# Local Python virtualenv targets

.PHONY: venv
venv:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: run-dev
run-dev:
	$(PYTHON) app.py

.PHONY: run
run: venv
	$(PYTHON) app.py

.PHONY: freeze
freeze:
	$(PIP) freeze > requirements.txt

# Docker targets

.PHONY: docker-build
docker-build:
	docker build -t $(DOCKER_IMAGE) .

.PHONY: docker-run
docker-run:
	docker run --rm -d \
		--name $(DOCKER_CONTAINER) \
		-p $(PORT):8000 \
		$(DOCKER_IMAGE)

.PHONY: docker-stop
docker-stop:
	-docker stop $(DOCKER_CONTAINER)

.PHONY: docker-shell
docker-shell:
	docker exec -it $(DOCKER_CONTAINER) /bin/bash

# Utility

.PHONY: clean
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	rm -f data.db
	rm -rf $(VENV)

.PHONY: zip
zip:
	$(PYTHON) make_zip.py

