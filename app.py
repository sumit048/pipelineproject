import streamlit as st
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

# Page config
st.set_page_config(page_title="Diamond Price Predictor 💎", layout="centered")

# Background image from your URL
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://png.pngtree.com/background/20230618/original/pngtree-abstract-red-crystal-formation-in-3d-rendering-picture-image_3710248.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 1rem;
            max-width: 600px;
            margin: auto;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

st.markdown("<h1 style='text-align: center;'>Diamond Price Predictor 💎</h1>", unsafe_allow_html=True)
st.write("### Enter diamond specifications to predict its price.")

carat = st.number_input("Carat", min_value=0.0, step=0.01)
depth = st.number_input("Depth", min_value=0.0, step=0.1)
table = st.number_input("Table", min_value=0.0, step=0.1)
x = st.number_input("X (mm)", min_value=0.0, step=0.1)
y = st.number_input("Y (mm)", min_value=0.0, step=0.1)
z = st.number_input("Z (mm)", min_value=0.0, step=0.1)

cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["J", "I", "H", "G", "F", "E", "D"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

if st.button("Predict"):
    try:
        data = CustomData(
            carat=carat,
            depth=depth,
            table=table,
            x=x,
            y=y,
            z=z,
            cut=cut,
            color=color,
            clarity=clarity
        )
        new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(new_data)
        st.success(f"💰 Predicted Diamond Price: ${round(result[0], 2)}")
    except Exception as e:
        st.error(f"Error: {e}")
