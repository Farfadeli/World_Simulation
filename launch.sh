#!/usr/bin/env bash

# Usage: ./launch.sh --name NAME --population POP --gap GAP --limit LIMIT

# --- Parse arguments ---
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --name) name="$2"; shift ;;
        --population) population="$2"; shift ;;
        --gap) gap="$2"; shift ;;
        --limit) limit="$2"; shift ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

# --- Check if Python 3 is installed ---
echo "Checking for Python 3..."
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 not found. Installing..."

    # Try Homebrew first
    if command -v brew >/dev/null 2>&1; then
        echo "Installing Python 3 using Homebrew..."
        brew install python
    else
        echo "Homebrew not found. Please install Homebrew or download Python manually from:"
        echo "https://www.python.org/downloads/macos/"
        exit 1
    fi
else
    echo "Python 3 is already installed at: $(which python3)"
fi

# --- Check pip ---
if ! python3 -m pip --version >/dev/null 2>&1; then
    echo "pip not found. Installing..."
    python3 -m ensurepip --upgrade
    python3 -m pip install --upgrade pip
else
    echo "pip is available."
fi

# --- Create virtual environment ---
if [ ! -d "./world_sims" ]; then
    echo "Creating virtual environment..."
    python3 -m venv world_sims
    ./world_sims/bin/python3 -m pip install --upgrade pip
    ./world_sims/bin/python3 -m pip install -r requirements.txt
    echo "--------------------------------------------------------------"
    echo "Virtual environment has been configured"
    echo "--------------------------------------------------------------"
else
    echo "--------------------------------------------------------------"
    echo "Virtual environment already configured"
    echo "--------------------------------------------------------------"
fi

# --- Run the Python simulation ---
./world_sims/bin/python3 ./world_simulation.py \
    --name "$name" \
    --population "$population" \
    --gap "$gap" \
    --limit "$limit"
