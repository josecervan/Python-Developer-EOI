<a href="https://pm1.narvii.com/6583/b5fb020cf0c3974e16cdc0869cb5abcec613803a_hq.jpg"><img src="https://pm1.narvii.com/6583/b5fb020cf0c3974e16cdc0869cb5abcec613803a_hq.jpg" title="Your name in Korean" alt="Your name in Korean"></a>

# Korean-Name-Generator
> What is your name in korean? Discover it from your birthday

**You will need:**
- Python 3
- <a href="https://docs.python.org/3/library/tkinter.html"> Tkinter</a>
- <a href="https://www.pyinstaller.org/"> Pyinstaller</a>

## Table of Contents
- [Clone](#clone)
- [Distributable](#distributable)
- [Installation](#installation)
- [Structure](#structure)
- [Test](#test)
- [Executable](#executable)
- [Author](#author)

## Clone
- If you want to clone this repo to your local machine, use `https://github.com/josecervan/Korean-Name-Generator`

## Distributable
- To generate the `korean_name` package, use `pip setup.py sdist --formats==zip,gztar` in `distributable` dir.
- The previous command will generate both `distributable/dist/korean_name-1.0.0.zip` and `distributable/dist/korean_name-1.0.0.tar.gz` files.

## Installation
- To install the `korean_name` package, use:
  - `pip install distributable/dist/korean_name-1.0.0.zip` on Windows.
  - `pip install distributable/dist/korean_name-1.0.0.tar.gz` on Linux or MAC.

## Structure
- Inside `korean_name` dir, the package structure consists of:
```cmd
├───korean_name
│   ├───front
│   │   ├───images
│   │   └───pages
│   ├───back
│   └───data
├───test
├───korean_name.egg-info
└───dist
```

## Test
- You can test the package using `python KorNameApp.py` from `distributable/test`, once `korean_name` is installed.

## Executable
- Generate a KorNameApp executable file by following the steps below (`pyinstaller` installation required):
  - For executing the app on a terminal window: `pyinstaller distributable/test/KorNameApp.py`.
  - For executing the app from a single file: `pyinstaller --windowed --icon=korea_flag.ico --onefile KorNameApp.py`. Besides, an icon will be added.
  
## Author
- Contact the author <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/cervan/"> via LinkedIn</a>.


