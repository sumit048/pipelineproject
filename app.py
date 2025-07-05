import streamlit as st
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

st.title("Diamond Price Predictor 💎")

st.write("Please enter the diamond features below:")

# Input fields
carat = st.number_input("Carat", min_value=0.0, format="%.2f")
depth = st.number_input("Depth", min_value=0.0, format="%.2f")
table = st.number_input("Table", min_value=0.0, format="%.2f")
x = st.number_input("X (Length in mm)", min_value=0.0, format="%.2f")
y = st.number_input("Y (Width in mm)", min_value=0.0, format="%.2f")
z = st.number_input("Z (Depth in mm)", min_value=0.0, format="%.2f")

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
        pred = predict_pipeline.predict(new_data)
        st.success(f"💰 Predicted Diamond Price: ${round(pred[0], 2)}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
