import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Seaborn Data Visualization Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# SEABORN THEME
# ============================================================

sns.set_theme(
    style="whitegrid",
    context="notebook"
)


# ============================================================
# TITLE
# ============================================================

st.title("📊 Seaborn Data Visualization Dashboard")

st.write(
    """
    This project demonstrates different Seaborn visualizations
    using a student dataset.

    You can explore:
    - Relational plots
    - Distribution plots
    - Categorical plots
    - Regression plots
    - Pair plots
    - Joint plots
    - Heatmaps
    - Cluster maps
    """
)


# ============================================================
# CREATE DATASET
# ============================================================

data = {

    "Student": [
        "Aarav", "Riya", "Rahul", "Priya", "Aman",
        "Neha", "Karan", "Anjali", "Rohit", "Simran",
        "Vikas", "Pooja", "Arjun", "Sneha", "Aditya",
        "Kavya", "Nikhil", "Isha", "Varun", "Meera"
    ],

    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],

    "Department": [
        "Data Science", "Web Development", "Data Science",
        "AI", "Web Development", "AI", "Data Science",
        "Web Development", "AI", "Data Science",
        "Web Development", "AI", "Data Science",
        "Web Development", "AI", "Data Science",
        "Web Development", "AI", "Data Science", "AI"
    ],

    "Age": [
        21, 22, 21, 23, 22,
        21, 24, 22, 23, 21,
        25, 22, 24, 23, 21,
        22, 24, 21, 23, 22
    ],

    "Study_Hours": [
        2, 4, 3, 5, 2,
        6, 4, 5, 3, 7,
        2, 6, 4, 5, 3,
        8, 4, 6, 5, 7
    ],

    "Attendance": [
        65, 80, 72, 90, 68,
        95, 82, 88, 75, 96,
        60, 91, 85, 89, 73,
        98, 79, 94, 87, 92
    ],

    "Marks": [
        55, 72, 65, 88, 60,
        92, 78, 85, 68, 95,
        50, 89, 82, 86, 64,
        98, 75, 93, 84, 90
    ],

    "Salary": [
        25000, 35000, 30000, 50000, 28000,
        55000, 42000, 48000, 32000, 60000,
        22000, 52000, 45000, 49000, 31000,
        65000, 40000, 58000, 47000, 54000
    ],

    "Placement": [
        "No", "Yes", "No", "Yes", "No",
        "Yes", "Yes", "Yes", "No", "Yes",
        "No", "Yes", "Yes", "Yes", "No",
        "Yes", "Yes", "Yes", "Yes", "Yes"
    ]
}


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(data)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📌 Navigation")

option = st.sidebar.radio(
    "Choose Section",
    [
        "Dataset",
        "Relational Plots",
        "Distribution Plots",
        "Categorical Plots",
        "Regression Plots",
        "Multi-Variable Plots",
        "Heatmap",
        "Cluster Map",
        "Seaborn Styling"
    ]
)


# ============================================================
# DATASET
# ============================================================

if option == "Dataset":

    st.header("📋 Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    st.subheader("Dataset Information")

    st.write("Columns:")

    st.write(
        list(df.columns)
    )

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )


# ============================================================
# RELATIONAL PLOTS
# ============================================================

elif option == "Relational Plots":

    st.header("🔗 Relational Plots")

    st.write(
        """
        Relational plots are used to understand the relationship
        between two or more variables.
        """
    )

    plot = st.selectbox(
        "Choose Plot",
        [
            "Scatterplot",
            "Lineplot",
            "Relplot"
        ]
    )


    # --------------------------------------------------------
    # SCATTERPLOT
    # --------------------------------------------------------

    if plot == "Scatterplot":

        st.subheader("Scatterplot")

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.scatterplot(
            data=df,
            x="Study_Hours",
            y="Marks",
            hue="Gender",
            style="Placement",
            size="Attendance",
            ax=ax
        )

        ax.set_title(
            "Study Hours vs Marks"
        )

        ax.set_xlabel(
            "Study Hours"
        )

        ax.set_ylabel(
            "Marks"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            Why use it?

            Scatterplot helps us understand whether two numerical
            variables have a relationship.

            Here we are checking whether study hours are related
            to marks.
            """
        )


    # --------------------------------------------------------
    # LINEPLOT
    # --------------------------------------------------------

    elif plot == "Lineplot":

        st.subheader("Lineplot")

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.lineplot(
            data=df,
            x="Study_Hours",
            y="Marks",
            marker="o",
            errorbar=None,
            ax=ax
        )

        ax.set_title(
            "Study Hours vs Marks"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            Why use it?

            Lineplot is useful when we want to see a trend
            or change in values.
            """
        )


    # --------------------------------------------------------
    # RELPLOT
    # --------------------------------------------------------

    elif plot == "Relplot":

        st.subheader("Relplot")

        fig = sns.relplot(
            data=df,
            x="Study_Hours",
            y="Marks",
            hue="Gender",
            col="Placement",
            kind="scatter",
            height=5,
            aspect=1
        )

        st.pyplot(fig.figure)

        plt.close(fig.figure)

        st.info(
            """
            relplot is a figure-level function.

            It can create multiple plots using variables such as
            row and col.
            """
        )


# ============================================================
# DISTRIBUTION PLOTS
# ============================================================

elif option == "Distribution Plots":

    st.header("📈 Distribution Plots")

    plot = st.selectbox(
        "Choose Distribution Plot",
        [
            "Histplot",
            "KDE Plot",
            "ECDF Plot",
            "Rug Plot",
            "Displot"
        ]
    )


    # --------------------------------------------------------
    # HISTPLOT
    # --------------------------------------------------------

    if plot == "Histplot":

        st.subheader("Histogram")

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.histplot(
            data=df,
            x="Marks",
            bins=8,
            kde=True,
            ax=ax
        )

        ax.set_title(
            "Distribution of Marks"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            Histplot shows how numerical values are distributed.

            KDE=True adds a smooth density curve.
            """
        )


    # --------------------------------------------------------
    # KDE
    # --------------------------------------------------------

    elif plot == "KDE Plot":

        st.subheader("KDE Plot")

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.kdeplot(
            data=df,
            x="Marks",
            hue="Gender",
            fill=True,
            ax=ax
        )

        ax.set_title(
            "Marks Distribution by Gender"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            KDE means Kernel Density Estimation.

            It represents the probability distribution of
            numerical data using a smooth curve.
            """
        )


    # --------------------------------------------------------
    # ECDF
    # --------------------------------------------------------

    elif plot == "ECDF Plot":

        st.subheader("ECDF Plot")

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.ecdfplot(
            data=df,
            x="Marks",
            hue="Gender",
            ax=ax
        )

        ax.set_title(
            "ECDF of Marks"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            ECDF shows the percentage/proportion of observations
            that are less than or equal to a particular value.
            """
        )


    # --------------------------------------------------------
    # RUGPLOT
    # --------------------------------------------------------

    elif plot == "Rug Plot":

        st.subheader("Rug Plot")

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.rugplot(
            data=df,
            x="Marks",
            height=0.05,
            ax=ax
        )

        ax.set_title(
            "Rug Plot of Marks"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            Rugplot displays individual observations as small
            vertical marks.
            """
        )


    # --------------------------------------------------------
    # DISPLOT
    # --------------------------------------------------------

    elif plot == "Displot":

        st.subheader("Displot")

        fig = sns.displot(
            data=df,
            x="Marks",
            hue="Gender",
            kde=True,
            height=5
        )

        st.pyplot(fig.figure)

        plt.close(fig.figure)

        st.info(
            """
            displot is a figure-level distribution function.

            It can create histograms, KDE plots and ECDF plots.
            """
        )


# ============================================================
# CATEGORICAL PLOTS
# ============================================================

elif option == "Categorical Plots":

    st.header("📊 Categorical Plots")

    plot = st.selectbox(
        "Choose Categorical Plot",
        [
            "Countplot",
            "Barplot",
            "Boxplot",
            "Violinplot",
            "Stripplot",
            "Swarmplot",
            "Boxenplot",
            "Pointplot",
            "Catplot"
        ]
    )


    # --------------------------------------------------------
    # COUNTPLOT
    # --------------------------------------------------------

    if plot == "Countplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.countplot(
            data=df,
            x="Department",
            hue="Gender",
            ax=ax
        )

        ax.set_title(
            "Students by Department"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            "Countplot counts the number of observations in each category."
        )


    # --------------------------------------------------------
    # BARPLOT
    # --------------------------------------------------------

    elif plot == "Barplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.barplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            errorbar=None,
            ax=ax
        )

        ax.set_title(
            "Average Marks by Department"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            "Barplot is useful for comparing numerical values across categories."
        )


    # --------------------------------------------------------
    # BOXPLOT
    # --------------------------------------------------------

    elif plot == "Boxplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.boxplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            ax=ax
        )

        ax.set_title(
            "Marks Distribution by Department"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            Boxplot shows:

            - Median
            - Quartiles
            - Spread
            - Possible outliers
            """
        )


    # --------------------------------------------------------
    # VIOLINPLOT
    # --------------------------------------------------------

    elif plot == "Violinplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.violinplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            ax=ax
        )

        ax.set_title(
            "Violin Plot of Marks"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            "Violinplot combines distribution information with a boxplot-like summary."
        )


    # --------------------------------------------------------
    # STRIPPLOT
    # --------------------------------------------------------

    elif plot == "Stripplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.stripplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            dodge=True,
            ax=ax
        )

        ax.set_title(
            "Strip Plot of Marks"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            "Stripplot displays individual observations for each category."
        )


    # --------------------------------------------------------
    # SWARMPLOT
    # --------------------------------------------------------

    elif plot == "Swarmplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.swarmplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            dodge=True,
            ax=ax
        )

        ax.set_title(
            "Swarm Plot of Marks"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            "Swarmplot displays individual points without overlapping them as much as possible."
        )


    # --------------------------------------------------------
    # BOXENPLOT
    # --------------------------------------------------------

    elif plot == "Boxenplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.boxenplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            ax=ax
        )

        ax.set_title(
            "Boxen Plot of Marks"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            "Boxenplot is useful for understanding distributions, especially with larger datasets."
        )


    # --------------------------------------------------------
    # POINTPLOT
    # --------------------------------------------------------

    elif plot == "Pointplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.pointplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            errorbar=None,
            ax=ax
        )

        ax.set_title(
            "Point Plot of Marks"
        )

        ax.tick_params(
            axis="x",
            rotation=30
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            "Pointplot displays estimated values and helps compare categories."
        )


    # --------------------------------------------------------
    # CATPLOT
    # --------------------------------------------------------

    elif plot == "Catplot":

        st.subheader("Catplot")

        fig = sns.catplot(
            data=df,
            x="Department",
            y="Marks",
            hue="Gender",
            kind="box",
            height=5,
            aspect=1.5
        )

        fig.set_xticklabels(
            rotation=30
        )

        st.pyplot(fig.figure)

        plt.close(fig.figure)

        st.info(
            """
            catplot is a figure-level categorical plotting function.

            It can create several categorical plots using the
            kind parameter.
            """
        )


# ============================================================
# REGRESSION PLOTS
# ============================================================

elif option == "Regression Plots":

    st.header("📉 Regression Plots")

    plot = st.selectbox(
        "Choose Regression Plot",
        [
            "Regplot",
            "LMplot",
            "Residplot"
        ]
    )


    # --------------------------------------------------------
    # REGPLOT
    # --------------------------------------------------------

    if plot == "Regplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.regplot(
            data=df,
            x="Study_Hours",
            y="Marks",
            ax=ax
        )

        ax.set_title(
            "Study Hours vs Marks with Regression Line"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            Regplot shows the relationship between two numerical
            variables along with a regression line.
            """
        )


    # --------------------------------------------------------
    # LMPLOT
    # --------------------------------------------------------

    elif plot == "LMplot":

        fig = sns.lmplot(
            data=df,
            x="Study_Hours",
            y="Marks",
            hue="Gender",
            height=5,
            aspect=1.5
        )

        st.pyplot(fig.figure)

        plt.close(fig.figure)

        st.info(
            """
            lmplot is a figure-level regression plot.

            It is useful for comparing regression relationships
            between groups.
            """
        )


    # --------------------------------------------------------
    # RESIDPLOT
    # --------------------------------------------------------

    elif plot == "Residplot":

        fig, ax = plt.subplots(
            figsize=(9, 5)
        )

        sns.residplot(
            data=df,
            x="Study_Hours",
            y="Marks",
            ax=ax
        )

        ax.set_title(
            "Residual Plot"
        )

        st.pyplot(fig)

        plt.close(fig)

        st.info(
            """
            Residual plots help us understand the errors between
            actual and predicted values.
            """
        )


# ============================================================
# MULTI-VARIABLE PLOTS
# ============================================================

elif option == "Multi-Variable Plots":

    st.header("🔍 Multi-Variable Visualization")

    plot = st.selectbox(
        "Choose Plot",
        [
            "Pairplot",
            "Jointplot"
        ]
    )


    # --------------------------------------------------------
    # PAIRPLOT
    # --------------------------------------------------------

    if plot == "Pairplot":

        st.subheader("Pairplot")

        selected_columns = [
            "Age",
            "Study_Hours",
            "Attendance",
            "Marks",
            "Salary"
        ]

        pair_fig = sns.pairplot(
            df[selected_columns],
            diag_kind="hist"
        )

        st.pyplot(
            pair_fig.figure
        )

        plt.close(
            pair_fig.figure
        )

        st.info(
            """
            Pairplot creates pairwise relationships between
            numerical variables.

            It is very useful during EDA.
            """
        )


    # --------------------------------------------------------
    # JOINTPLOT
    # --------------------------------------------------------

    elif plot == "Jointplot":

        st.subheader("Jointplot")

        fig = sns.jointplot(
            data=df,
            x="Study_Hours",
            y="Marks",
            kind="scatter",
            height=7
        )

        st.pyplot(
            fig.figure
        )

        plt.close(
            fig.figure
        )

        st.info(
            """
            Jointplot combines a main relationship plot with
            distributions of individual variables.
            """
        )


# ============================================================
# HEATMAP
# ============================================================

elif option == "Heatmap":

    st.header("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(
        include="number"
    )

    correlation = numeric_df.corr()

    fig, ax = plt.subplots(
        figsize=(10, 7)
    )

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5,
        square=True,
        ax=ax
    )

    ax.set_title(
        "Correlation Heatmap"
    )

    st.pyplot(fig)

    plt.close(fig)

    st.info(
        """
        Heatmap represents values using colors.

        Correlation values range from:

        -1 → Strong negative relationship
         0 → No linear relationship
        +1 → Strong positive relationship

        annot=True displays the correlation values.
        """ 
    )


# ============================================================
# CLUSTER MAP
# ============================================================

elif option == "Cluster Map":

    st.header("🌳 Cluster Map")

    numeric_df = df.select_dtypes(
        include="number"
    )

    correlation = numeric_df.corr()

    cluster_fig = sns.clustermap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        figsize=(9, 8)
    )

    st.pyplot(
        cluster_fig.figure
    )

    plt.close(
        cluster_fig.figure
    )

    st.info(
        """
        Clustermap performs hierarchical clustering and displays
        the relationships between variables in a clustered form.
        """
    )


# ============================================================
# SEABORN STYLING
# ============================================================

elif option == "Seaborn Styling":

    st.header("🎨 Seaborn Styling")

    style = st.selectbox(
        "Choose Seaborn Style",
        [
            "whitegrid",
            "darkgrid",
            "white",
            "dark",
            "ticks"
        ]
    )

    context = st.selectbox(
        "Choose Context",
        [
            "paper",
            "notebook",
            "talk",
            "poster"
        ]
    )

    if st.button("Apply Style"):

        sns.set_theme(
            style=style,
            context=context
        )

        st.success(
            "Style applied!"
        )

    st.subheader("Available Styles")

    st.write(
        """
        whitegrid
        → White background with grid

        darkgrid
        → Dark background with grid

        white
        → White background

        dark
        → Dark background

        ticks
        → White background with ticks
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.sidebar.markdown("---")

st.sidebar.info(
    """
    📊 Seaborn Visualization Project

    Built using:
    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Streamlit
    """
)