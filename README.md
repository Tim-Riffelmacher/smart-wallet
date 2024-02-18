# Projektarbeit
## by Tim Riffelmacher

## Table of contents
1. [Idea](#idea)
2. [Installation](#example2)
3. [Evaluation](#third-example)

## Idea

The primary objective is to create a web application designed to assist users in effectively managing their finances. This is achieved through the implementation of three core functionalities. Firstly, an integrated stock tool provides users with the ability to track and stay updated on the latest trends in the stock market. Secondly, a personal wallet feature is implemented to facilitate the tracking of expenditures and income. Lastly, a chat network is developed to enable users to engage in discussions with others. These three core functionalities empower users to manage their finances with clarity and efficiency.

## Streamlit

The web application should be implemented in Streamlit. Streamlit is a python package that is used to develop web applications fast and easy. It is mainly used to visually prepare and present data via reports or dashboards.

### Structure

- .streamlit
- components
- pages
- utils

## Installation

Firstly, ensure that [Python3](https://www.python.org/downloads/) is installed on your system. Afterwards, proceed to install the required dependencies by executing the command `pip3 install -r requirements.txt` in the root directory of the repository. Once the dependencies are installed, initiate the web application by executing `streamlit run Dashboard.py`. If the streamlit command is not recognized, you may need to add it to the `$PATH`, or consider creating a virtual Python environment.

## Evaluation

## PROS
- Fast and easy
- Good for data
- Good documentation

## CONS
- Session state is hard to manage
- Poor customizing/styling options
- Poor perfomance on rerender
- Interactivity
- Async is unpossible