# ======================================================
# CUSTOMER SEGMENTATION APPLICATION
# Interactive UI using Gradio + MySQL
# ======================================================


import gradio as gr
import joblib
import pandas as pd
import plotly.express as px


from database import (
    save_prediction,
    get_cluster_details,
    get_history
)



# ======================================================
# LOAD MODEL AND SCALER
# ======================================================


model = joblib.load(
    "model.pkl"
)


scaler = joblib.load(
    "scaler (1).pkl"
)


print("MODEL LOADED SUCCESSFULLY")



# ======================================================
# PREDICTION FUNCTION
# ======================================================


def predict_customer(
        gender,
        age,
        income,
        spending
):


    if gender == "Male":
        gender_value = 0

    else:
        gender_value = 1



    input_data = pd.DataFrame(

        [[
            gender_value,
            age,
            income,
            spending
        ]],

        columns=[
            "Gender",
            "Age",
            "AnnualIncome",
            "SpendingScore"
        ]

    )



    scaled_data = scaler.transform(
        input_data
    )



    cluster = model.predict(
        scaled_data
    )[0]



    details = get_cluster_details(
        int(cluster)
    )



    if details:

        cluster_name = details["ClusterName"]

        description = details["Description"]

        recommendation = details["Recommendation"]


    else:

        cluster_name="Unknown"

        description="No information available"

        recommendation="No recommendation"



    save_prediction(

        gender,

        age,

        income,

        spending,

        cluster_name

    )



    result = f"""

## Customer Segment

### ⭐ {cluster_name}


### Description

{description}


### Business Recommendation

{recommendation}


### Cluster ID

{cluster}

"""


    return result



# ======================================================
# HISTORY FUNCTION
# ======================================================


def show_history():

    data = get_history()


    df = pd.DataFrame(

        data,

        columns=[

            "ID",

            "Gender",

            "Age",

            "Income",

            "Spending",

            "Cluster",

            "Date"

        ]

    )


    return df




# ======================================================
# CLUSTER VISUALIZATION
# ======================================================


def cluster_chart():

    data = get_history()


    if len(data)==0:

        return None



    df=pd.DataFrame(

        data,

        columns=[

            "ID",

            "Gender",

            "Age",

            "Income",

            "Spending",

            "Cluster",

            "Date"

        ]

    )



    fig = px.pie(

        df,

        names="Cluster",

        title="Customer Segment Distribution"

    )


    return fig



# ======================================================
# GRADIO UI
# ======================================================



with gr.Blocks(

    theme=gr.themes.Soft(),

    title="Customer Segmentation System"

) as app:



    # ---------------- HEADER ----------------


    gr.Markdown(

    """

# 🛒 Customer Segmentation System


### Machine Learning Based Customer Analysis

This system uses clustering algorithms to identify customer groups
and generate business recommendations.


**Technology Stack**

Python | Scikit-learn | MySQL | Gradio

"""

)



    # =================================================
    # PREDICTION TAB
    # =================================================


    with gr.Tab(
        "🔍 Predict Customer"
    ):


        with gr.Row():


            with gr.Column():


                gender = gr.Dropdown(

                    choices=[
                        "Male",
                        "Female"
                    ],

                    label="Gender"

                )


                age = gr.Number(

                    label="Age"

                )


                income = gr.Number(

                    label="Annual Income"

                )


                spending = gr.Number(

                    label="Spending Score"

                )



                with gr.Row():


                    predict_btn = gr.Button(

                        "🚀 Predict Segment",

                        variant="primary"

                    )


                    clear_btn = gr.ClearButton(

                        [
                            gender,
                            age,
                            income,
                            spending
                        ]

                    )



            with gr.Column():


                result = gr.Markdown(

                    label="Prediction Result"

                )



        predict_btn.click(

            predict_customer,

            inputs=[

                gender,
                age,
                income,
                spending

            ],

            outputs=result

        )





    # =================================================
    # HISTORY TAB
    # =================================================


    with gr.Tab(
        "📜 Prediction History"
    ):


        history_btn = gr.Button(

            "Load Previous Predictions"

        )


        history_table = gr.Dataframe(

            interactive=False

        )


        history_btn.click(

            show_history,

            outputs=history_table

        )





    # =================================================
    # ANALYTICS TAB
    # =================================================


    with gr.Tab(

        "📊 Analytics"

    ):


        chart_btn = gr.Button(

            "Generate Customer Segment Chart"

        )


        chart = gr.Plot()



        chart_btn.click(

            cluster_chart,

            outputs=chart

        )





    # =================================================
    # PROJECT INFORMATION TAB
    # =================================================


    with gr.Tab(

        "ℹ About Project"

    ):


        gr.Markdown(

        """

## Customer Segmentation


### Objective

Identify customer groups using clustering algorithms.


### Machine Learning Models

- K-Means
- Agglomerative Hierarchical Clustering
- DBSCAN
- Other clustering techniques


### Features Used

- Gender
- Age
- Annual Income
- Spending Score


### Application Workflow


Dataset

↓

Data Preprocessing

↓

Clustering Model

↓

Customer Segment Prediction

↓

Business Recommendation


"""

)





# ======================================================
# START APPLICATION
# ======================================================


import os

port = int(os.environ.get("PORT", 7860))

app.launch(
    server_name="0.0.0.0",
    server_port=port,
    share=False
)