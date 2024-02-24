# Project Work (2)

- Topic: **Webdevelopment with Streamlit and Python**
- Student: **Tim Riffelmacher**
- Supervisor: **Prof. Dr.-Ing. Holger Vogelsang**
- Begin: **25.09.2023**

## Table of contents

1. [Idea](#idea)
2. [Streamlit](#streamlit)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Manual](#manual)
6. [Evaluation](#evaluation)  
   6.1 [Advantages](#advantages)  
   6.2 [Disadvantages](#disadvantages)
7. [Summary](#summary)

## Idea

The primary objective is to create a web application designed to assist users in effectively managing their finances. This is achieved through the implementation of three core functionalities. Firstly, an integrated stock tool provides users with the ability to track and stay updated on the latest trends in the stock market. Secondly, a personal wallet feature is implemented to facilitate the tracking of expenditures and income. Lastly, a chat network is developed to enable users to engage in discussions with others. These three core functionalities empower users to manage their finances with clarity and efficiency.

## Streamlit

The implementation of the web application is designated to be executed using Streamlit, a Python package renowned for its rapid and straightforward web application development capabilities. According to developers, Streamlit excels in visually preparing and presenting data through reports or dashboards. Throughout the project's implementation, an assessment will be conducted to gauge Streamlit's suitability for the specified task. Furthermore, a comprehensive evaluation will be documented at a later stage.

## Project Structure

In the following the top-level folders and files present in the repository are listed and explained:

- **.streamlit/** - Environment variables for Streamlit
- **components/** - Stores reusable componentes (e.g. inputs)
- **pages/** - Defines the pages to be displayed
- **utils/** - Stores reusable functionality (e.g. db-connection)
- **.gitignore** - Configures Git
- **Dashboard.py** - The entry point of the web application
- **README.md** - Holds the documentation
- **requirements.txt** - Stores the Python dependencies to be installed

## Installation

Firstly, ensure that [Python3](https://www.python.org/downloads/) is installed on your system. Afterwards, proceed to install the required dependencies by executing the command `pip3 install -r requirements.txt` in the root directory of the repository. Once the dependencies are installed, initiate the web application by executing `streamlit run pages/Dashboard.py`. If the streamlit command is not recognized, you may need to add it to the `$PATH`, or consider creating a virtual Python environment.

## Manual

This section describes what functionality the web application offers and how it can be utilized.

### Navigation Bar

![](./resources/navigation_bar.png)

On the left side of the web application, a navigation bar is presented, facilitating navigation among the five distinct pages, each of which is elaborated upon in the following sections.

### Dashboard Page

![](./resources/dashboard.png)

This serves as the entry point for the web application. Analogous to the navigation bar, it offers access to the remaining four pages. Additionally, it includes a link to the documentation for further reference.

### Stocks Page

### Network Page

![](./resources/network_chat.png)

On the network page you can chat with others about finance topics. Therefore select the appropiate channel, write your message and send it. In the chat window the 6 latest messages are displayed. You can delete your own message by pressing on the _Remove_ button in case you made a mistake, so it is to no one visible anymore. Furthermore you can save every message by pressing on the _Star_. From now on it stored in your saved messages tab.

![](./resources/network_saved_messages.png)

Here you can see your saved messages. You also have the option to remove a message again from your saved ones by pressing on the _Remove_ button.

### Profile Page

![](./resources/profile.png)

In this section, users can update their personal settings, including their first and last names. The first name is displayed when posting a message on the network page.

## Evaluation

This chapter evaluates the advantages and disadvantages of using Streamlit for developing web applications.

### Advantages

#### Fast & Easy Development

One of the most significant advantages of using Streamlit lies in its minimal learning curve, allowing users to comprehend its functionality and develop web applications in a short period. The Streamlit Python library is remarkably straightforward, eliminating the need to grasp every intricate concept. Proficiency in implementing components, such as buttons and inputs, along with understanding the control flow of Streamlit (data distribution and management), equips users to create web applications with essential functionality.

Moreover, Streamlit significantly accelerates the development process. Unlike traditional web application development, there is no requirement to dive into CSS for aesthetic enhancements; Streamlit takes care of design, ensuring a visually appealing interface. Additionally, diverse data types can effortlessly be presented using various chart types, requiring minimal effort on the part of the developer.

#### Data Presentation

As previously highlighted, Streamlit excels in presenting diverse data types through a wide array of chart options. Whether it's simple line charts, scatterplots, or complex graphs, Streamlit accommodates them all. The inclusion of third-party extensions further expands the available charting options, streamlining the development process and enabling developers to concentrate on data processing, rather than spending excessive time on presentation details. Additionally, Streamlit facilitates easy experimentation with different chart types, allowing developers to explore various visualizations without significant time investment.

Example:

```python
    st.line_chart(total_money_course, y="Money in $")
```

Result:

#### Good Documentation

The Streamlit [documentation](https://docs.streamlit.io/) stands out for its simplicity and clarity. Firstly, it provides a comprehensive introduction that facilitates a clear understanding of Streamlit's main concepts. Secondly, the API guide is notably well-structured and easily understandable, allowing users to quickly locate and access the information they need. Additionally, the documentation offers a convenient [cheatsheet](https://docs.streamlit.io/library/cheatsheet) that provides a rapid overview of the most crucial API calls.

#### Uniform Design

As mentioned earlier, Streamlit simplifies the design process by eliminating the need to create a design framework or concept, followed by the development of reusable and uniform components (e.g., buttons, inputs, etc.). Instead, Streamlit provides pre-styled components that are ready to use, sparing developers from the initial design groundwork. While all components come with default styles, the Streamlit library offers ample customization options, allowing users to tailor the components to their specific use cases—whether it's changing button labels, adjusting input placeholders, or more.

In some instances, it might be beneficial to organize a composition of components into a reusable library, particularly when dealing with repetitive elements like a start-to-end date input across multiple pages, reducing code duplication. Additionally, Streamlit's [theming](https://docs.streamlit.io/library/advanced-features/theming) capabilities allow for global adjustments, enabling users to specify primary and secondary colors, fonts, and other stylistic elements that apply to all Streamlit components.

### Disadvantages

#### Confusing Session State

In a general context, the rendered pages within Streamlit are inherently stateless. To preserve state information, the utilization of Streamlit's provided [session state](https://docs.streamlit.io/library/api-reference/session-state) becomes imperative. This feature essentially operates as a key-value store with an indefinite growth capacity. Consequently, managing state complexity requires precise documentation to prevent it from spiraling out of control, necessitating clear records of the stored information within the session state.

#### Poor Styling Options

Regrettably, the Streamlit components exhibit a restricted array of styling options. Primarily, the available choices are confined to two colors—namely, the primary and secondary colors predetermined by the overarching theme. The absence of direct interaction with the underlying CSS of these components leaves developers with no recourse but to resort to crafting pure HTML code for extended customization. For instance, achieving the horizontal centering of a component lacks a straightforward option. Instead, one must resort to a column layout approach, placing the component within the central column and adjusting its width to match that of the container.

#### Poor Render Performance

Relative to other frameworks facilitating web application development, Streamlit exhibits suboptimal rendering performance. The time required to render a page with comparable components is notably extended compared to frameworks such as [React](https://react.dev/). While this may be tolerable for static pages that necessitate a single loading and rendering instance, the drawback becomes apparent in scenarios demanding frequent page rerendering due to dynamic component changes. In such cases, the prolonged rendering duration may result in user inconvenience and frustration.

#### No Real Asynchrony

Unfortunately, Streamlit's support for executing actions in the background is constrained to specific limitations. The prevailing concept dictates that a page achieves full loading status only upon the completion of all background operations. Consequently, the platform does not facilitate the loading of substantial data in the background, followed by asynchronous injection into the page. The inherent constraint is evident in the prolonged rendering times of pages necessitating substantial data retrieval from the backend, leading to potential delays in rendering.

#### Duplicated Code

Given the functional programming paradigm employed in page development, the propensity for code duplication in Streamlit is notable. The absence of inherent object orientation fails to necessitate thoughtful consideration regarding the decomposition of pages into multiple classes and their interrelations. The dearth of such structural considerations renders the code less amenable to effective testing and reusability.

Consequently, it becomes imperative to proactively establish a dedicated reusable component library early in the development process, one that can be universally applied across all pages. Failure to do so may result in significant challenges during subsequent refactoring endeavors.

#### Missing Control Flow Options

Until a recent update, Streamlit introduced the capability for programmatically altering pages, a feature previously unavailable. However, a persistent challenge remains as rerendering a page using `st.rerun()` is currently not viable within callbacks. The absence of this option poses limitations, particularly in scenarios where a page reload is desired, such as when a refresh button is pressed.

## Summary

In summary, Streamlit serves as an entry-level framework, facilitating the entry of non-technical users into web application development without significant concern for technical intricacies. It provides an extensive collection of reusable components and ensures a cohesive design, imparting a polished look-and-feel to the web application. Moreover, Streamlit excels in effortlessly visualizing large datasets through various chart options.

However, it comes with certain limitations. The framework lacks the flexibility found in other web application frameworks, as it is notably constrained to its predefined components with limited customization options. Additionally, Streamlit falls short in terms of tooling and performance compared to its counterparts. Consequently, Streamlit proves most suitable for scenarios where a static data-presenting web application with minimal interaction requirements is sufficient.
