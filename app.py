import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CardioPredict AI",
    page_icon="❤️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #64748b;
    margin-bottom: 30px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.result {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

try:
    model = joblib.load("cardio_model.pkl")
    model_loaded = True

except:
    model_loaded = False


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">❤️ CardioPredict AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Cardiovascular Disease Prediction'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# MODEL STATUS
# --------------------------------------------------

if model_loaded:
    st.success("🟢 AI Model Loaded Successfully")
else:
    st.error("🔴 Model not found. Please create cardio_model.pkl first.")


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Patient Settings")

st.sidebar.info(
    "Enter patient health information "
    "to generate a cardiovascular disease prediction."
)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.header("👤 Patient Information")

col1, col2, col3 = st.columns(3)

with col1:

    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=120,
        value=50
    )

    height = st.number_input(
        "📏 Height (cm)",
        min_value=50,
        max_value=250,
        value=165
    )


with col2:

    gender = st.selectbox(
        "⚧ Gender",
        ["Female", "Male"]
    )

    weight = st.number_input(
        "⚖️ Weight (kg)",
        min_value=20.0,
        max_value=300.0,
        value=65.0
    )


with col3:

    smoke = st.selectbox(
        "🚬 Smoking",
        ["No", "Yes"]
    )

    alco = st.selectbox(
        "🍷 Alcohol",
        ["No", "Yes"]
    )


# --------------------------------------------------
# MEDICAL INFORMATION
# --------------------------------------------------

st.header("🩺 Medical Information")

col1, col2, col3 = st.columns(3)

with col1:

    ap_hi = st.number_input(
        "🩸 Systolic BP",
        min_value=50,
        max_value=250,
        value=120
    )

    ap_lo = st.number_input(
        "🩸 Diastolic BP",
        min_value=30,
        max_value=150,
        value=80
    )


with col2:

    cholesterol = st.selectbox(
        "🧪 Cholesterol",
        [1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Above Normal",
            3: "Well Above Normal"
        }[x]
    )


with col3:

    gluc = st.selectbox(
        "🍬 Glucose",
        [1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Above Normal",
            3: "Well Above Normal"
        }[x]
    )

    active = st.selectbox(
        "🏃 Physically Active",
        ["No", "Yes"]
    )


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

st.divider()

predict_button = st.button(
    "🔍  PREDICT CARDIOVASCULAR RISK",
    use_container_width=True
)


if predict_button:

    if not model_loaded:

        st.error(
            "Please train the model first using train_model.py"
        )

    else:

        # Convert values

        gender_value = 1 if gender == "Male" else 2

        smoke_value = 1 if smoke == "Yes" else 0

        alco_value = 1 if alco == "Yes" else 0

        active_value = 1 if active == "Yes" else 0


        # Create input

        input_data = pd.DataFrame({

            "age": [age * 365],

            "gender": [gender_value],

            "height": [height],

            "weight": [weight],

            "ap_hi": [ap_hi],

            "ap_lo": [ap_lo],

            "cholesterol": [cholesterol],

            "gluc": [gluc],

            "smoke": [smoke_value],

            "alco": [alco_value],

            "active": [active_value]

        })


        # Prediction

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]


        # --------------------------------------------------
        # RESULT
        # --------------------------------------------------

        st.header("📊 Prediction Result")


        if prediction == 1:

            st.markdown(
                '<div class="result">'
                '⚠️ Higher Cardiovascular Risk'
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="result">'
                '✅ Lower Cardiovascular Risk'
                '</div>',
                unsafe_allow_html=True
            )


        st.write("")

        # Probability

        st.subheader("📈 Risk Probability")

        st.progress(float(probability))

        st.metric(
            "Predicted Risk",
            f"{probability * 100:.2f}%"
        )


        # Show entered data

        with st.expander("🔎 View Patient Data"):

            st.dataframe(
                input_data,
                use_container_width=True
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🤖 CardioPredict AI | Machine Learning Project | "
    "Built with Python + Scikit-learn + Streamlit"
)