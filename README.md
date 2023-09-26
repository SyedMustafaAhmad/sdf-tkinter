# sdf-tkinter
stable-diffusion v2.1 tkinter application written in python
<img src="https://raw.githubusercontent.com/SyedMustafaAhmad/sdf-tkinter/main/output/sample-image.png" style="width: 800px; max-width: 100%; height: auto" title="Click to enlarge picture" />
</br>

## Setup
### 1. Install [Python](https://www.python.org/downloads/)
On Linux, it usually comes pre-installed.
### 2. Create a Python Virtual Environment (venv)
On Linux,
```console
python3 -m venv name-of-environment
```
On Windows,
```console
python -m venv name-of-environment
```

### 3. Activate the Virtual Environment
On Linux,
```console
source venv/bin/activate
```
On Windows (one of these),
```console
venv-name\Scripts\activate
venv-name\Scripts\activate.bat
venv-name\Scripts\Activate.ps1
```

### 4. Install all Packages
In the requirements.txt use the command,
On Linux,
```console
pip3 install -r requirements.txt
```
On Windows,
```console
pip install -r requirements.txt
```

## How to use?
Simple run the src/main.py file using python,
On Linux,
```console
python3 main.py
```
On Windows,
```console
python main.py
```

## Some Extra Information
- I made this application on a 12th Gen Intel CPU with Xe graphics so I've added the Pipe to CPU checkbox. By default, it should use CUDA but it is untested.
- The image generation takes time. On a good GPU it will be faster. You can see progress of the image generation in the console/terminal in which you ran the final command.
