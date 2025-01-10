# PyMol-Bearing

PyMol-Bearing: A virtual bearing test bench built by Modelica and Python calling interface

[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
![eg](/main_ui_eg.png)
## Dependencies
### Python
- Python 2.7 and Python 3.x supported
### Modelica
- Most version of OpenModelica
- Since the model uses ModelicaServices 3.2.3, it is recommended to install OpenModelica 1.16. The link can be found at: https://build.openmodelica.org/omc/builds/windows/releases/
### OMPython
- Installation link: https://pypi.org/project/OMPython/
### PyQt5
- Installation link: https://pypi.org/project/PyQt5/

- The process of downloading PyMol-Bearing from GitHub, creating a virtual environment using Anaconda, and using it in PyCharm can be referred to in [the installation demonstration video](https://github.com/xiangmianmian/PyMol-Bearing/blob/main/GUI%20installation%20demonstration%20video.mp4)
## Usage steps
- Download the GUI file package (which includes the code for the UI interface and the Modelica model files)
```sh
git clone https://github.com/xiangmianmian/PyMol-Bearing.git
```
- Locate `login.py` in the file, and run it
- For details, please refer to [the demo video of the GUI](https://github.com/xiangmianmian/PyMol-Bearing/blob/main/GUI%20operation%20demonstration%20video.mp4)
       
### 1. Log in to the GUI
- Open `login.py` and log in to the GUI using the username: `123` and password: `222` (customizable)
- Select the Dynamic Bearing Model to enter the main interface
  
### 2. Configure the bearing-related parameters and select the bearing fault location
- Click button 4 to enter the bearing configuration interface
- Enter the relevant bearing parameters as needed (Material parameters, Design parameters). You can also use the default values without configuration. Click Confirm after finishing the configuration
- Select the bearing fault location:
  - Choose "RaceWay" from the dropdown menu and click Finish to enter the inner and outer ring fault size parameter configuration interface
    - If selecting outer ring fault, set the race value to 1
    - If selecting inner ring fault, set the race value to 2
  - Choose "Ball" and click Finish to enter the ball fault size parameter configuration interface
  - If selecting "Healthy", no fault size configuration is needed. Click Finish to return to the main interface

### 3. (Optional): Configure the motor, shaft, and hydraulic load servo system parameters (this step can usually be skipped by using all default parameters)
- Click button 1 to enter the motor parameters configuration interface
- Click button 2 to enter the shaft parameters configuration interface
- Click button 3 to enter the hydraulic loading system parameters configuration interface

### 4. Set the shaft speed
- Click button 5 to enter the PID-control shaft speed configuration interface
- Enter the shaft speed (the PID-control parameters for shaft speed usually do not need configuration; you can use the default values)

### 5. Set the load size
- Click button 6 to enter the load configuration interface
- Enter the load value (the PID-control parameters for load usually do not need configuration; you can use the default values)

### 6. Simulation
- Click the Simulate button to enter the simulation interface
- Enter the simulation-related parameters as needed
- Click the Run button to start the simulation
- After the system runs for a period, the results will be displayed, and the results will be written to output.csv

## Modelica modeling principles  
For detailed modeling principles, please refer to the published papers.  
1. [Ruan, D., Li, Z., & Gühmann, C. (2021). Modeling of A Bearing Test Bench and Analysis of Defect Bearing Dynamics in Modelica. Proceedings of 14th Modelica Conference 2021, Linköping, Sweden, September 20-24, 2021.]( https://doi.org/10.3384/ecp21181373)
2. [Ruan, D.; Chen, Y.; Gühmann, C.; Yan, J.; Li, Z. Dynamics Modeling of Bearing with Defect in Modelica and Application in Direct Transfer Learning from Simulation to Test Bench for Bearing Fault Diagnosis. Electronics 2022, 11, 622.](https://doi.org/10.3390/electronics11040622)




<!-- links -->
[your-project-path]:xiangmianmian/PyMol-Bearing
[stars-shield]: https://img.shields.io/github/stars/xiangmianmian/PyMol-Bearing.svg?style=flat-square
[stars-url]: https://github.com/xiangmianmian/PyMol-Bearing/stargazers
[license-shield]: https://img.shields.io/github/license/xiangmianmian/PyMol-Bearing.svg?style=flat-square
[license-url]: https://github.com/xiangmianmian/PyMol-Bearing/blob/master/LICENSE.txt
