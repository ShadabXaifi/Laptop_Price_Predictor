import streamlit as st
import pandas as pd
import pickle
from utils.feature_engineering import prepare_input
from utils.prediction import LaptopPricePredictor

# -------------------------------------
# Page Configuration
# -------------------------------------

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------
# Load CSS
# -------------------------------------

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------------------------
# Load Dataset
# -------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/laptop_price_dataset_india.csv")

df = load_data()

# -------------------------------------
# Load Model
# -------------------------------------

@st.cache_resource
def load_predictor():
    return LaptopPricePredictor()

predictor = load_predictor()

# -------------------------------------
# Header
# -------------------------------------

st.markdown(
"""
<div class='main-title'>
💻 AI Laptop Price Predictor
</div>

<div class='sub-title'>
Powered by XGBoost Regression
</div>
""",
unsafe_allow_html=True
)

st.divider()

# -------------------------------------
# Sidebar
# -------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/laptop.png",
        width=90
    )

    st.title("About")

    st.write(
"""
This application predicts laptop prices
using a Machine Learning model trained
on hundreds of laptops.

Model Used

✅ XGBoost Regressor

Accuracy

99.09% R²
"""
    )

    st.divider()

    st.success("Portfolio Project")

# -------------------------------------
# Layout
# -------------------------------------

left,right=st.columns([1,1])

# =====================================
# LEFT COLUMN
# =====================================

with left:

    st.markdown(
    "<div class='glass'>",
    unsafe_allow_html=True
    )

    st.subheader("Laptop Information")

    brand=st.selectbox(
        "Brand",
        sorted(df.brand.unique())
    )

    model=st.selectbox(
        "Model",
        sorted(
            df[
                df.brand==brand
            ].model.unique()
        )
    )

    processor_brand=st.selectbox(
        "Processor Brand",
        sorted(df.processor_brand.unique())
    )

    processor_model=st.selectbox(
        "Processor Model",
        sorted(df.processor_model.unique())
    )

    processor_generation=st.selectbox(
        "Processor Generation",
        sorted(df.processor_generation.unique())
    )

    gpu_brand=st.selectbox(
        "GPU Brand",
        sorted(df.gpu_brand.unique())
    )

    gpu_model=st.selectbox(
        "GPU Model",
        sorted(df.gpu_model.unique())
    )

    ram_gb=st.selectbox(
        "RAM (GB)",
        sorted(df.ram_gb.unique())
    )

    ram_type=st.selectbox(
        "RAM Type",
        sorted(df.ram_type.unique())
    )

    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )

# =====================================
# RIGHT COLUMN
# =====================================

with right:

    st.markdown(
    "<div class='glass'>",
    unsafe_allow_html=True
    )

    st.subheader("Display & Storage")

    storage_capacity_gb=st.selectbox(
        "Storage Capacity",
        sorted(
            df.storage_capacity_gb.unique()
        )
    )

    storage_type=st.selectbox(
        "Storage Type",
        sorted(
            df.storage_type.unique()
        )
    )

    screen_size_inches=st.selectbox(
        "Screen Size",
        sorted(
            df.screen_size_inches.unique()
        )
    )

    screen_resolution=st.selectbox(
        "Resolution",
        sorted(
            df.screen_resolution.unique()
        )
    )

    panel_type=st.selectbox(
        "Panel",
        sorted(
            df.panel_type.unique()
        )
    )

    refresh_rate_hz=st.selectbox(
        "Refresh Rate",
        sorted(
            df.refresh_rate_hz.unique()
        )
    )

    keyboard_backlit=st.selectbox(
        "Keyboard Backlit",
        sorted(
            df.keyboard_backlit.unique()
        )
    )

    fingerprint_sensor=st.selectbox(
        "Fingerprint Sensor",
        sorted(
            df.fingerprint_sensor.unique()
        )
    )

    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )

st.write("")

predict = st.button(
    "🔮 Predict Laptop Price",
    use_container_width=True
)


# ==========================================================
# Prediction
# ==========================================================

if predict:

    with st.spinner("Analyzing laptop specifications..."):

        input_df = prepare_input(

            brand=brand,
            model=model,

            processor_brand=processor_brand,
            processor_model=processor_model,
            processor_generation=processor_generation,

            gpu_brand=gpu_brand,
            gpu_model=gpu_model,

            ram_gb=ram_gb,
            ram_type=ram_type,

            storage_capacity_gb=storage_capacity_gb,
            storage_type=storage_type,

            screen_size_inches=screen_size_inches,
            screen_resolution=screen_resolution,
            refresh_rate_hz=refresh_rate_hz,
            panel_type=panel_type,

            keyboard_backlit=keyboard_backlit,
            fingerprint_sensor=fingerprint_sensor

        )

        prediction = predictor.predict(input_df)

    st.write("")

    st.markdown(
        f"""
        <div class="prediction">

        <h2>💰 Estimated Laptop Price</h2>

        <div class="price">
        ₹ {prediction:,.0f}
        </div>

        <br>

        <h4>
        Prediction generated using
        XGBoost Regressor
        </h4>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")



    st.markdown("## 📋 Configuration Summary")

    c1,c2,c3 = st.columns(3)

    with c1:

        st.metric(
            "Brand",
            brand
        )

        st.metric(
            "Model",
            model
        )

        st.metric(
            "Processor",
            processor_model
        )

    with c2:

        st.metric(
            "Graphics",
            gpu_model
        )

        st.metric(
            "RAM",
            f"{ram_gb} GB"
        )

        st.metric(
            "Storage",
            f"{storage_capacity_gb} GB"
        )

    with c3:

        st.metric(
            "Resolution",
            screen_resolution
        )

        st.metric(
            "Refresh Rate",
            f"{refresh_rate_hz} Hz"
        )

        st.metric(
            "Panel",
            panel_type
        )


    st.write("")

    st.subheader("🖥 Hardware Overview")

    hardware = pd.DataFrame({

        "Component":[

            "Processor",

            "Graphics",

            "RAM",

            "Storage",

            "Display",

            "Keyboard",

            "Fingerprint"

        ],

        "Specification":[

            processor_model,

            gpu_model,

            f"{ram_gb} GB {ram_type}",

            f"{storage_capacity_gb} GB {storage_type}",

            f'{screen_size_inches}" {screen_resolution} {refresh_rate_hz}Hz',

            keyboard_backlit,

            fingerprint_sensor

        ]

    })

    st.dataframe(
        hardware,
        use_container_width=True,
        hide_index=True
    )


    with st.expander("🔍 View Complete Feature Vector"):

        st.dataframe(
            input_df,
            use_container_width=True
        )

st.divider()

st.markdown(
"""
<center>

Made with ❤️ using

Streamlit + Scikit-Learn + XGBoost

</center>
""",
unsafe_allow_html=True
)

