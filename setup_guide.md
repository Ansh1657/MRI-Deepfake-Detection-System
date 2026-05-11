# 🛠️ Setup & Installation Guide

**Project:** MRI Deepfake Detection System  
**Author:** Ansh Chhibber  

> **⚠️ IP Protection Notice:** > This repository is a technical portfolio demonstration. To protect pending intellectual property, the trained model weights (`.pth` files) and the raw medical datasets are deliberately withheld. The instructions below detail the environment setup and architectural execution for evaluation purposes.

---

## 💻 System Prerequisites

Before initializing the environment, ensure your system meets the following requirements:

* **OS:** Windows 10/11 (WSL2 recommended), macOS, or Linux (Ubuntu 20.04+)
* **Python:** Version 3.10 or higher
* **Hardware:** 16GB RAM minimum. A CUDA-capable NVIDIA GPU (CUDA 11.8+) is highly recommended for executing the deep learning modules.
* **Tools:** Git, Bash terminal

---

## 🚀 One-Click Automated Setup (Recommended)

For UNIX-based systems (Linux/macOS) or Windows users running Git Bash/WSL, we have provided an automated setup script. This script will autonomously generate the required directory trees, initialize the Python virtual environment, and install all necessary PyTorch and Computer Vision dependencies.

**1. Clone the repository:**
```bash
git clone [https://github.com/Ansh1657/mri-deepfake-detection.git](https://github.com/Ansh1657/mri-deepfake-detection.git)
cd mri-deepfake-detection

```

**2. Make the script executable (Mac/Linux only):**

```bash
chmod +x setup.sh

```

**3. Execute the setup script:**

```bash
./setup.sh

```

**4. Activate your environment:**

* **Mac/Linux:** `source venv/bin/activate`
* **Windows (Git Bash):** `source venv/Scripts/activate`

---

## ⚙️ Manual Installation

If you prefer to configure the environment manually or encounter issues with the bash script, follow these steps:

**1. Initialize Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # (Use venv\Scripts\activate on Windows)

```

**2. Install PyTorch (CUDA 11.8):**

```bash
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)

```

*(Note: If you do not have a GPU, remove the `--index-url` flag to install the CPU-only version).*

**3. Install Core Dependencies:**

```bash
pip install -r requirements.txt

```

**4. Generate Directory Structure:**

```bash
mkdir -p data/raw_mri data/processed_256 data/synthetic_gans
mkdir -p saved_models results

```

---

## 🖥️ Running the Application

Once the environment is configured and activated, you can launch the local web server to interact with the system architecture.

```bash
python app.py

```

* The system will initialize the Gradio backend.
* Open your web browser and navigate to the local host address provided in the terminal (typically `http://127.0.0.1:7860`).
* *Note: Because the proprietary `.pth` weights are withheld, running inference on a newly uploaded image will yield simulated backend routing unless custom models are trained locally.*

---

## 🔧 Troubleshooting Common Issues

### 1. CUDA Out of Memory (OOM) Errors

If you are compiling the models locally and run out of VRAM, force CPU execution by modifying the device mapping in `app.py` or the inference scripts:

```python
device = torch.device('cpu')  # Overrides default 'cuda'

```

### 2. OpenCV Headless Errors (Linux)

If the UI crashes due to an OpenCV dependency error on Linux servers, replace standard OpenCV with the headless version:

```bash
pip uninstall opencv-python
pip install opencv-python-headless

```

### 3. Port Conflicts

If port `7860` is already in use by another Jupyter or Gradio instance, launch the app on an alternative port:

```bash
python app.py --server-port 7861

```
