USERNAME:=$(shell git config user.name)
REPO:=$(shell dirname $(CURDIR))/$(USERNAME).github.com
TMP:=/tmp/github-pages
DIST:=static/dist

all:
	make migrate
	make import
	make dist
	make build
	make push

migrate:
	python -u manage.py migrate

import:
	bash -l -c "python -u manage.py import-repos"
	bash -l -c "python -u manage.py import-starred-repos"
	bash -l -c "python -u manage.py import-gists"
	bash -l -c "python -u manage.py import-starred-gists"

build:
	find $(REPO) -name "*.html" -type f -exec rm {} \;
	find $(REPO) -depth -type d -exec rmdir {} \; 2>/dev/null
	python -u manage.py build --skip-static --build-dir=$(TMP)
	cp -R $(TMP)/ $(REPO)

webpack:
	webpack --config webpack.production.config.js

dist:
	rm -fr $(DIST)
	make webpack
	test -d $(REPO)/static || mkdir -p $(REPO)/static
	rsync --delete -a static/ $(REPO)/static

push:
	cd $(REPO) && make
