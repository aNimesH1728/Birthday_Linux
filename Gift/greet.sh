SCRIPT_DIR="$(dirname "$(realpath "$0")")"
VENV_PYTHON="$SCRIPT_DIR/bin/python"

# Check if virtual environment exists
if [ ! -f "$VENV_PYTHON" ]; then
  echo "Virtual environment not found at $VENV_PYTHON"
  echo "Create one with: python3 -m venv .venv"
  exit 1
fi

# Run with the virtual environment's Python
"$VENV_PYTHON" "$SCRIPT_DIR/greeter.py" "$@"