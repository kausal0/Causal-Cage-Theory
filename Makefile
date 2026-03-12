# Set build directory
PROTO_DIR = proto
GEN_DIR = generated
PYTHON_OUT = $(GEN_DIR)/python
TS_OUT = $(GEN_DIR)/typescript

.PHONY: all clean generate-python generate-ts

all: generate-python generate-ts

# Clean up the generated directory
clean:
rm -rf $(GEN_DIR)

# Generate Python code
generate-python:
mkdir -p $(PYTHON_OUT)
python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(PYTHON_OUT) \
--grpc_python_out=$(PYTHON_OUT) $(PROTO_DIR)/integrity.proto

# Generate TypeScript/JavaScript code
generate-ts:
mkdir -p $(TS_OUT)
protoc --plugin=protoc-gen-ts=`which protoc-gen-ts` \
-I$(PROTO_DIR) --js_out=import_style=commonjs,binary:$(TS_OUT) \
-ts_out=$(TS_OUT) $(PROTO_DIR)/integrity.proto

# Help
help:
@echo "make all: Generate stubs for all languages"
@echo "make generate-python: Generate stubs for Python"
@echo "make generate-ts: Generate stubs for TypeScript"
