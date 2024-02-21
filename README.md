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

### Fast & Easy Development

One of the most significant advantages of using Streamlit lies in its minimal learning curve, allowing users to comprehend its functionality and develop web applications in a short period. The Streamlit Python library is remarkably straightforward, eliminating the need to grasp every intricate concept. Proficiency in implementing components, such as buttons and inputs, along with understanding the control flow of Streamlit (data distribution and management), equips users to create web applications with essential functionality.

Moreover, Streamlit significantly accelerates the development process. Unlike traditional web application development, there is no requirement to dive into CSS for aesthetic enhancements; Streamlit takes care of design, ensuring a visually appealing interface. Additionally, diverse data types can effortlessly be presented using various chart types, requiring minimal effort on the part of the developer.

### Data Presentation

As previously highlighted, Streamlit excels in presenting diverse data types through a wide array of chart options. Whether it's simple line charts, scatterplots, or complex graphs, Streamlit accommodates them all. The inclusion of third-party extensions further expands the available charting options, streamlining the development process and enabling developers to concentrate on data processing, rather than spending excessive time on presentation details. Additionally, Streamlit facilitates easy experimentation with different chart types, allowing developers to explore various visualizations without significant time investment.

Example:
```python
    st.line_chart(total_money_course, y="Money in $")
```
Result:

### Good Documentation

The Streamlit [documentation](https://docs.streamlit.io/) stands out for its simplicity and clarity. Firstly, it provides a comprehensive introduction that facilitates a clear understanding of Streamlit's main concepts. Secondly, the API guide is notably well-structured and easily understandable, allowing users to quickly locate and access the information they need. Additionally, the documentation offers a convenient [cheatsheet](https://docs.streamlit.io/library/cheatsheet) that provides a rapid overview of the most crucial API calls.

### Uniform Design

As mentioned earlier, Streamlit simplifies the design process by eliminating the need to create a design framework or concept, followed by the development of reusable and uniform components (e.g., buttons, inputs, etc.). Instead, Streamlit provides pre-styled components that are ready to use, sparing developers from the initial design groundwork. While all components come with default styles, the Streamlit library offers ample customization options, allowing users to tailor the components to their specific use cases—whether it's changing button labels, adjusting input placeholders, or more.

In some instances, it might be beneficial to organize a composition of components into a reusable library, particularly when dealing with repetitive elements like a start-to-end date input across multiple pages, reducing code duplication. Additionally, Streamlit's [theming](https://docs.streamlit.io/library/advanced-features/theming) capabilities allow for global adjustments, enabling users to specify primary and secondary colors, fonts, and other stylistic elements that apply to all Streamlit components.

## CONS
- Session state is hard to manage
- Poor customizing/styling options
- Poor perfomance on rerender
- Interactivity
- Async is unpossible
- Coding can quickly escalate
- Hard multi page management