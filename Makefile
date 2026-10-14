.PHONY: install test run lint
ifeq ($(OS),Windows_NT)
PYTHON ?= python
VENV_PYTHON = .venv/Scripts/python.exe
else
PYTHON ?= python3
VENV_PYTHON = .venv/bin/python
endif

install:
	"$(PYTHON)" -m venv .venv
	"$(VENV_PYTHON)" -m pip install -r requirements.txt

test:
	"$(VENV_PYTHON)" -m pytest

run:
	"$(VENV_PYTHON)" main.py

lint:
	"$(VENV_PYTHON)" -m ruff check .
	"$(VENV_PYTHON)" -m ruff format --check .
