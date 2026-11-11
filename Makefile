CC = python3 tools/compiler.py
SRC_DIR = src
BIN_DIR = bin

SRCS = $(wildcard $(SRC_DIR)/*.py)
BINS = $(patsubst $(SRC_DIR)/%.py,$(BIN_DIR)/%.epp,$(SRCS))

all: $(BINS)

$(BIN_DIR)/%.epp: $(SRC_DIR)/%.py
	$(CC) $< -o $@

clean:
	rm -rf $(BIN_DIR)/*.epp

run: all
	python3 main.py

