.PHONY: build install dist sources srpm clean

PYTHON  := python
PROGRAM := httmock
PACKAGE := python-$(PROGRAM)
VERSION := $(shell sed -n s/[[:space:]]*Version:[[:space:]]*//p $(PACKAGE).spec)


build:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install --skip-build

dist: clean
	$(PYTHON) setup.py sdist

sources: clean
	@git archive --format=tar --prefix="$(PROGRAM)-$(VERSION)/" \
		$(shell git rev-parse --verify HEAD) | gzip > "$(PROGRAM)-$(VERSION).tar.gz"

srpm: sources
	rpmbuild -bs --define "_sourcedir $(CURDIR)" \
		--define "_srcrpmdir $(CURDIR)" $(PACKAGE).spec

clean:
	@rm -rf build dist $(PROGRAM).egg-info $(PROGRAM)-*.tar.gz *.egg *.src.rpm
