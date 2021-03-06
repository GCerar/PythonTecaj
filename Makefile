.PHONY: all

venv:
	if [ ! -d "./env" ]; then \
		python3 -m venv env; \
	fi; \
	source ./env/bin/activate


all: venv
	pip install -Ur requirements.txt
