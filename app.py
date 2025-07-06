import streamlit as st
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

# Page config
st.set_page_config(page_title="💎 Diamond Price Predictor", layout="centered")

# Custom CSS for background, form box, and fonts
def set_premium_style():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://png.pngtree.com/background/20230618/original/pngtree-abstract-red-crystal-formation-in-3d-rendering-picture-image_3710248.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
    }
    .main-container {
        background-color: rgba(0, 0, 0, 0.65);
        padding: 2rem;
        border-radius: 1rem;
        max-width: 600px;
        margin: 2rem auto;
        box-shadow: 0 0 20px rgba(0,0,0,0.4);
    }
    h1, h2, h3, label, p {
        color: #ffffff !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

set_premium_style()

# Layout container
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown("<h1>💎 Diamond Price Predictor</h1>", unsafe_allow_html=True)
    st.write("### Enter your diamond specifications:")

    # Inputs
    carat = st.number_input("Carat", min_value=0.0, step=0.01)
    depth = st.number_input("Depth", min_value=0.0, step=0.1)
    table = st.number_input("Table", min_value=0.0, step=0.1)
    x = st.number_input("X (mm)", min_value=0.0, step=0.1)
    y = st.number_input("Y (mm)", min_value=0.0, step=0.1)
    z = st.number_input("Z (mm)", min_value=0.0, step=0.1)

    cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
    color = st.selectbox("Color", ["J", "I", "H", "G", "F", "E", "D"])
    clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

    # Predict
    if st.button("💰 Predict Price"):
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
            df = data.get_data_as_dataframe()
            pipeline = PredictPipeline()
            result = pipeline.predict(df)
            st.success(f"🎯 Estimated Price: ${round(result[0], 2)}")
        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)
