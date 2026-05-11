#!/bin/bash

echo "🧠 Starting Setup for MRI Deepfake Detection System..."
echo "======================================================="

# 1. Create Directory Structure
echo "📁 Step 1: Building directory tree..."
mkdir -p data/raw_mri/real_dark data/raw_mri/real_bright
mkdir -p data/processed_256 data/synthetic_gans
mkdir -p saved_models results
mkdir -p src/preprocessing src/models src/inference
echo "✅ Directories created."

# 2. Create Python Virtual Environment
echo "🐍 Step 2: Creating Python virtual environment..."
python3 -m venv venv

# Activate the virtual environment
# (Note: Using the direct path to pip ensures it installs inside the venv)
VENV_PIP="./venv/bin/pip"

# For Windows compatibility (if someone runs this via Git Bash)
if [ -f "./venv/Scripts/pip" ]; then
    VENV_PIP="./venv/Scripts/pip"
fi

echo "✅ Virtual environment created."

# 3. Install Dependencies
echo "📦 Step 3: Installing dependencies (This may take a few minutes)..."

# Upgrade pip first
$VENV_PIP install --upgrade pip

# Install PyTorch (Configured for CUDA 11.8 by default)
echo "Installing PyTorch stack..."
$VENV_PIP install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install all other required libraries directly
echo "Installing Computer Vision and UI libraries..."
$VENV_PIP install \
    opencv-python>=4.8.0 \
    Pillow>=10.0.0 \
    numpy>=1.24.0 \
    scipy>=1.10.0 \
    scikit-learn>=1.3.0 \
    matplotlib>=3.7.0 \
    seaborn>=0.12.0 \
    gradio>=4.0.0 \
    jupyter>=1.0.0 \
    notebook>=7.0.0 \
    ipywidgets>=8.0.0 \
    tqdm>=4.65.0 \
    pandas>=2.0.0

echo "✅ All dependencies installed successfully."

# 4. Final Instructions
echo "======================================================="
echo "🚀 SETUP COMPLETE!"
echo ""
echo "To activate your environment and start coding, run:"
echo "👉 source venv/bin/activate    (On Mac/Linux)"
echo "👉 source venv/Scripts/activate (On Windows Git Bash)"
echo "======================================================="
