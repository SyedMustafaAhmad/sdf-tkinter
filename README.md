# sdf-tkinter
stable-diffusion v2.1 tkinter application written in python

## Setup
1. Install [Python](https://www.python.org/downloads/). On Linux, it usually comes pre-installed.

2. Create a python virtual environment.
On Linux,
```console
python3 -m venv name-of-environment
```
On Windows,
```console
python -m venv name-of-environment
```

3. Activate the virtual environment
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

4. Install all packages in requirements.txt by using the command,
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
