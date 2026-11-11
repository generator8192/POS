CC = python3 tools/compiler.py
SRC_DIR = src
BIN_DIR = bin

SRCS := $(shell find $(SRC_DIR) -name '*.py')
BINS := $(patsubst $(SRC_DIR)/%.py,$(BIN_DIR)/%.epp,$(SRCS))

all: $(BINS)

$(BIN_DIR)/%.epp: $(SRC_DIR)/%.py
	@mkdir -p $(dir $@)
	$(CC) $< -o $@

clean:
	rm -rf $(BIN_DIR)/*
