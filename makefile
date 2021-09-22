.PHONY: clean
clean:
	$(RM) dist

.PHONY: build
run: clean
	python3 src/Main/Main.py