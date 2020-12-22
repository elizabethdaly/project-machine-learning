# project-machine-learning
HDip Data Analytics 2020 Machine Learning &amp; Statistics Project

<p align="middle">
  <img src="img/python.jpg" width="100" />
</p>

## Description

This README describes work done for the Machine Learning and Statistics module project, due 8 January 2021.

We have been asked to ... put description here.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- [Anaconda distribution of Python](https://www.anaconda.com/distribution/)
- [Python Software Foundation](https://www.python.org/)
- [Project Jupyter](https://jupyter.org/)
- [matplotlib: Python plotting library](https://matplotlib.org/)
- [NumPy](https://numpy.org/)
- [SciPy](https://www.scipy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [TensorFlow]()
- [Docker]()

### Installing
Download and install the Anaconda distribution of Python from the link above. The other packages (Jupyter notebook, Pandas, matplotlib, NumPy, and Scikit-learn) come as part of that distribution.

### Project repository
This project is hosted on [GitHub](https://github.com/) at 
https://github.com/elizabethdaly/project-machine-learning

### Instructions for cloning the repository
A repository on GitHub exists as a remote repository. You can clone this repository to create a local copy on your computer by following these instructions:
1. On GitHub, navigate to the main page of the repository https://github.com/elizabethdaly/project-machine-learning
2. Under the repository name, click Clone or download.
3. Choose "Clone with HTTPS".
4. Open a terminal on your machine. Change the current working directory to the location where you want the cloned directory to be made.
5. Type git clone, and then paste the URL you copied in 2 above.
```
git clone https://github.com/elizabethdaly/project-machine-learning
```
6. Press enter to clone the repository to your machine.

## Static version of the notebook
Alternatively, one can view a static version of the notebook using [Jupyter Nbviewer](https://nbviewer.jupyter.org/). Enter the GitHub url to view the file.

```
https://github.com/elizabethdaly/tasks-machine-learning/blob/master/project-machine-learning.ipynb
```

## Files
- Data analysis and model training/evaluation in a single Jupyter notebook _project-machine-learning.ipynb_
- Data set _powerproduction.csv_ in **data** subdirectory.
- _index.html_ file for for the web server front end in **static** subdirectory.
- _MLserver.py_ file for flask server at repository top level.
- Some references in **references** subdirectory.
- All images in **img** subdirectory of this repository.
- Rough work/old files in **rough** subdirectory.
- Model files in **models** subdirectory.
    - _poly-reg.pkl_ (polynomial regression)
	- _svm-reg.pkl_ (support vector machine regression)
	- _scalerX.pkl_ (scaler pre-processing for SVM regression above)
	- _neural-nw.h5_ (sequential neural network)
- _requirements.txt_ requirements to run flask app in a virtual environment.

(Please not that the steps to save these four files have been commented out in the Jupyter notebook so that my final models are not overwritten. If you wish to resave, just remove comments.)

## Virtual environment

## How to run the server instructions

## Docker instructions

## Author
Elizabeth Daly for HDip in Data Analytics 2019/2020.

## Licence

This project is licensed under the GNU General Public License v3.0 - see the LICENSE.md file for details.
