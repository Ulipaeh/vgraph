# Vgraph

A graphical interface to visibility graph

## Install 🔧

1. Install python 3.7 (download link https://www.python.org/downloads/release/python-370/ ), mark "Add to path" option, add click next  
2.Open CMD or Terminal and install packages: numpy, pandas, networkx, sklearn, pyqtgraph and pyqt5, with pip install comand:
```
pip install numpy      # enter
pip install pandas     # enter
pip install pyqtgraph  # enter
pip install networkx   # enter
pip install sklearn    # enter
```
<img width="360" alt="librerias" src="https://user-images.githubusercontent.com/53945790/76443786-98e3f600-6388-11ea-88d6-8395e908a4a7.PNG">


## Run program ⚙️
1. Locate (with cd comand) interface folder and run python main.py in CMD:

<img width="413" alt="Ejecutar" src="https://user-images.githubusercontent.com/53945790/76440640-c0848f80-6383-11ea-9521-b4ed3ad08c28.PNG">


## Use Vgraph ⌨️

1. Load signal(s) in format 1 column .txt or .csv:

<img width="497" alt="Abrir" src="https://user-images.githubusercontent.com/53945790/76441566-3fc69300-6385-11ea-9735-59488d43673f.png">

2. Select the parameters to create visibility graph and maxclique graph and click in "visibility graph" button: 

<img width="500" alt="Parametros" src="https://user-images.githubusercontent.com/53945790/76441876-b5326380-6385-11ea-9abc-4fa5763a37c5.png">

3. At the end of the process, the files are automatically saved in the folder of the loaded signal:

<img width="655" alt="Localizacion" src="https://user-images.githubusercontent.com/53945790/76443160-9df47580-6387-11ea-990f-d78c5f14cdf8.PNG">

## K-means clustering 🛠️
1. This interface can perform k-means clustering with graphs parameters:

<img width="499" alt="Kmeans1" src="https://user-images.githubusercontent.com/53945790/76446804-350ffc00-638d-11ea-9f16-56439ab9b0e0.png">

2. Load 2 files (parameters) to k-means clustering, set axis labels to graph and number of clusters and click "k-means" button:

<img width="717" alt="Kmeans2" src="https://user-images.githubusercontent.com/53945790/76447094-aea7ea00-638d-11ea-84dd-b461e161fb59.png">

3. The clasification image is automatically saved in the folder of the loaded parameters:

<img width="582" alt="Kmeans3" src="https://user-images.githubusercontent.com/53945790/76447359-2b3ac880-638e-11ea-8df6-e8f1620a525c.png">

