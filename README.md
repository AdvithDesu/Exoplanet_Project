# Exoplanet_Project

## Overview
This code allows us to analyse lightcurve data from MAST database using the lightkurve module.

The main code is split into Webscrapping (Allows us to download several csv data files from MAST database) and LightCurve (Code for producing and storing Lightcurves).

---
## Instructions to use the code

### 1. Required Python modules

The following are the modules you will need for the code to run smoothly:
  
  - **Selenium** (For Web-scrapping)
  - **Lightkurve** (For generating Lightcurves)
  - **Pandas**
  - **Numpy**
  - **Matplotlib**

---

### 2. Web-Scrapping

Download the latest version of the Chrome driver from - <https://sites.google.com/a/chromium.org/chromedriver/downloads> <br />
(**Side Note**: Make sure your current version of Chrome matchs the Chrome driver version that you download)

After the download is complete, move the driver into Program Files (x86) which is located in the C drive.

The program will ask for one input

  - **Range of RA** - Enter the range of RA values you want to download data from. <br />
    For example if you want to download data from all stars with RA 90 to 95 just input "90 95" without the quotes.

---

### 3. LightCurve

It is advisable to run this code in Jupyter Notebook (Installation - <https://jupyter.org/install.html>)

You are required to change both the input and output directory in the program
  
  - **input_dir** = "{folder directory in your pc}" + "\\StarData_" + str(file_no) + ".csv" <br />
    (**Note** that you have to only change the text in the { } brackets, and it must be the same directory where the csv files are located) 
    
  - **output_dir** can just be set to the path where you want the final lightcurves to be stored
  
The program will ask you for two inputs

  -  **First Input** - Enter the starting file number and end file number in the input screen <br />
     For example if you want to analyse from file 3 to file 10 you have to enter "3 10" (without the quotes ofc)
     
  - **Second Input** - If you happen to stop the program previously on some index, make sure to enter that here the next time you start the program <br />
    (**Note:** Just enter 0 otherwise)
---
## Contributors

- **Advith Desu** (Github profile - <https://github.com/AdvithDesu>)
- **Nitya Shah** (Github profile - <https://github.com/nitya-6>)
- **Manasa SK** (Github profile - <https://github.com/manasa-sk>)
- **Mokshith Thakkilapati** (Github profile - <https://github.com/mokshith002>)
