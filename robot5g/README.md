# robot5G
![](https://i.imgur.com/2vlbyp1.png)
## Purpose
Use AGV(automated guided vehicle) to :
* measure 5G signal automatically
* draw heatmap
## Package
* Config: some setting
* Node: it cant do something for us, BIGGER things
* result: output
* Robot: Restful API for Mir100
* Sensors: instrument code to read 5g signal
* Testfile: some `*.py` and `*.ipynb` test file
* Tools: some tools for setting parameters and code
* Utils: some functions
## How to run
### Create your python 3.6.9 executable environment(Anaconda for example)
```shell script
conda create -n robot5G python=3.6.9
conda activate robot5G
```
### Install package
```shell script
pip install -r requirements.txt
```
### Choose what you want to execute
1. control.py: control the mir100 by joystick and webbrowser
2. crawler.py: choose the mission and measuring the signal of 5G 
3. main.py: create a new scanning mission and scan
```shell script
python main.py
```
