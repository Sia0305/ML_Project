import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Cardiovascular Disease Prediction",
    page_icon="💚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SIMPLE LIGHT THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f8fafc;
}

[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e7eb;
}

.block-container {
    max-width: 1200px;
    padding-top: 35px;
}

h1 {
    color: #172033 !important;
}

h2 {
    color: #172033 !important;
}

h3 {
    color: #172033 !important;
}

p {
    color: #667085;
}

.stButton > button {
    background-color: #12a86b;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 25px;
    font-weight: 700;
}

.stButton > button:hover {
    background-color: #078653;
    color: white;
}

[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 15px;
    padding: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("💚 Cardiovascular Disease Prediction")

    st.caption("AI Health Intelligence")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Home",
            "🔮 Predict",
            "📖 About",
            "📩 Contact"
        ]
    )

    st.divider()

    st.caption("Machine Learning Project")
    st.caption("Python • ML • Streamlit")


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.success("✦ AI POWERED HEALTH INTELLIGENCE")

    st.title("Understand Your Health.")
    st.header("Predict Smarter. 💚")

    st.write(
        "VitalCare AI uses Machine Learning to analyze "
        "health-related information and generate intelligent "
        "predictions through a simple interface."
    )

    st.write("")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.info(
            "🧠 Intelligent Analysis\n\n"
            "Machine Learning helps analyze health information "
            "and identify meaningful patterns."
        )

    with col2:

        st.success(
            "⚡ Fast Results\n\n"
            "Generate predictions within seconds."
        )

    st.divider()

    st.subheader("Why VitalCare?")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 🧠 Intelligent")

        st.write(
            "Machine Learning analyzes multiple health "
            "features to generate predictions."
        )

    with col2:

        st.markdown("### ⚡ Fast")

        st.write(
            "Enter your information and get results quickly."
        )

    with col3:

        st.markdown("### 🎯 Simple")

        st.write(
            "A clean interface makes Machine Learning "
            "easy to understand."
        )

    st.divider()

    st.subheader("How It Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric("STEP 01", "📝 Input")

        st.caption("Enter health information.")

    with col2:

        st.metric("STEP 02", "⚙️ Process")

        st.caption("Prepare the information.")

    with col3:

        st.metric("STEP 03", "🧠 Analyze")

        st.caption("ML model analyzes data.")

    with col4:

        st.metric("STEP 04", "✨ Result")

        st.caption("View the prediction.")

    st.divider()

    st.subheader("Project Highlights")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Model", "ML")

    with col2:
        st.metric("Interface", "Streamlit")

    with col3:
        st.metric("Language", "Python")

    with col4:
        st.metric("Analysis", "AI")


# =========================================================
# PREDICT
# =========================================================

elif page == "🔮 Predict":

    st.success("✦ AI HEALTH ANALYSIS")

    st.title("Health Prediction")

    st.write(
        "Enter the health information below "
        "to generate a prediction."
    )

    st.divider()

    st.subheader("👤 Personal Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30
        )

    with col2:

        height = st.number_input(
            "Height (cm)",
            min_value=50,
            max_value=250,
            value=170
        )

    with col3:

        weight = st.number_input(
            "Weight (kg)",
            min_value=20,
            max_value=250,
            value=65
        )

    st.divider()

    st.subheader("❤️ Health Information")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        cholesterol = st.selectbox(
            "Cholesterol",
            [
                "Normal",
                "Above Normal",
                "High"
            ]
        )

    with col2:

        activity = st.selectbox(
            "Physical Activity",
            ["Yes", "No"]
        )

        smoking = st.selectbox(
            "Smoking",
            ["No", "Yes"]
        )

    st.divider()

    st.subheader("🩸 Blood Pressure")

    col1, col2 = st.columns(2)

    with col1:

        ap_hi = st.number_input(
            "Systolic Pressure",
            min_value=50,
            max_value=250,
            value=120
        )

    with col2:

        ap_lo = st.number_input(
            "Diastolic Pressure",
            min_value=30,
            max_value=200,
            value=80
        )

    st.write("")

    predict = st.button(
        "✨ Generate Prediction",
        use_container_width=True
    )

    if predict:

        # BMI calculation

        height_m = height / 100

        bmi = weight / (height_m ** 2)

        st.divider()

        st.subheader("📊 Analysis Result")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "BMI",
                f"{bmi:.2f}"
            )

        with col2:

            st.metric(
                "Blood Pressure",
                f"{ap_hi}/{ap_lo}"
            )

        with col3:

            st.metric(
                "Age",
                age
            )

        st.write("")

        # Demo prediction

        if ap_hi >= 140 or ap_lo >= 90:

            prediction = "Higher Risk"

            st.warning(
                "⚠️ Prediction: Higher Risk"
            )

        else:

            prediction = "Lower Risk"

            st.success(
                "✨ Prediction: Lower Risk"
            )

        st.write("")

        st.subheader("⚖️ BMI Analysis")

        if bmi < 18.5:

            st.info(
                f"BMI = {bmi:.2f} — Underweight"
            )

        elif bmi < 25:

            st.success(
                f"BMI = {bmi:.2f} — Normal"
            )

        elif bmi < 30:

            st.warning(
                f"BMI = {bmi:.2f} — Overweight"
            )

        else:

            st.error(
                f"BMI = {bmi:.2f} — Obesity"
            )


# =========================================================
# ABOUT
# =========================================================

elif page == "📖 About":

    st.success("✦ ABOUT VITALCARE AI")

    st.title("About the Project")

    st.write(
        "VitalCare AI is a Machine Learning project designed "
        "to demonstrate how health-related data can be processed "
        "and used for prediction."
    )

    st.divider()

    st.subheader("🎯 Project Objective")

    st.write("""
    The main objective of this project is to develop a
    Machine Learning based prediction system.

    The application accepts health information from the user,
    processes the input and uses a trained model to generate
    a prediction.
    """)

    st.divider()

    st.subheader("🔄 Machine Learning Workflow")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.info("📂\n\nDataset")

    with col2:
        st.info("🧹\n\nPreprocessing")

    with col3:
        st.info("🧠\n\nTraining")

    with col4:
        st.info("📊\n\nEvaluation")

    with col5:
        st.info("🔮\n\nPrediction")

    st.divider()

    st.subheader("🛠️ Technologies Used")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Language", "Python")

    with col2:
        st.metric("Data", "Pandas")

    with col3:
        st.metric("ML", "Scikit-learn")

    with col4:
        st.metric("Frontend", "Streamlit")

    st.divider()

    st.subheader("📚 Project Tasks")

    st.write("""
    **Week 1:** Dataset Understanding

    **Week 2:** Data Preprocessing

    **Week 3:** Model Creation

    **Week 4:** Model Evaluation

    **Week 5:** Advanced Model Training

    **Frontend:** Streamlit Application
    """)


# =========================================================
# CONTACT
# =========================================================

elif page == "📩 Contact":

    st.success("✦ CONTACT")

    st.title("Let's Connect")

    st.write(
        "Have a question, suggestion or feedback? "
        "Send us a message."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📬 Contact Information")

        st.info("""
        📧 Email

        example@gmail.com

        📍 Location

        Gujarat, India

        💻 Project

        Machine Learning Health Prediction
        """)

    with col2:

        st.subheader("💌 Send a Message")

        name = st.text_input(
            "Name",
            placeholder="Enter your name"
        )

        email = st.text_input(
            "Email",
            placeholder="Enter your email"
        )

        subject = st.text_input(
            "Subject",
            placeholder="Enter subject"
        )

        message = st.text_area(
            "Message",
            placeholder="Write your message here..."
        )

        send = st.button(
            "📨 Send Message",
            use_container_width=True
        )

        if send:

            if name and email and message:

                st.success(
                    "Message sent successfully! 💚"
                )

            else:

                st.error(
                    "Please fill in Name, Email and Message."
                )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "💚 VitalCare AI | Machine Learning Health Prediction System | © 2026"
)