import streamlit as st
import random

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

PRODUCT_NAME = "AgriKit"

# --- Apply Minimal Styling ---
st.set_page_config(page_title="AgriKit", layout="wide")
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f4f4f4;
        padding: 20px;
    }
    .css-1v3fvcr, .css-1v0mbdj, .stButton > button {
        font-size: 16px;
        border-radius: 10px;
        width: 100%;
        margin-top: 10px;
    }
    .stApp {
        background-color: #ffffff;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# --- Navigation Buttons ---
st.sidebar.title("🚜 AgriKit")
if st.sidebar.button("🏠 Home"):
    st.session_state.current_page = "Home"
if not st.session_state.logged_in:
    if st.sidebar.button("🔐 Login"):
        st.session_state.current_page = "Login"
    if st.sidebar.button("🤞 Create Account"):
        st.session_state.current_page = "Create Account"
if st.sidebar.button("📊 Dashboard"):
    st.session_state.current_page = "Dashboard"
if st.sidebar.button("🔮 Prediction"):
    st.session_state.current_page = "Prediction"
if st.sidebar.button("🥕 About Us"):
    st.session_state.current_page = "About Us"
if st.sidebar.button("☎️ Contact Us"):
    st.session_state.current_page = "Contact Us"
if st.sidebar.button("📘 About the Product"):
    st.session_state.current_page = "About Product"


# --- Login Page ---
def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome back, {username}!")
            st.success(f"Go to your dashboard to view your statuses.")
        else:
            st.error("Username and password required")


# --- Create Account Page ---
def create_account():
    st.title("🤞 Create Account")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Create Account"):
        if not username or not password:
            st.error("Username and password required")
        elif password != confirm_password:
            st.error("Passwords do not match")
        else:
            st.success(f"Account created for {username}! You can now log in.")


# --- Home Page ---
def home():
    st.title("🌾 Welcome to AgriKit")
    st.markdown(f"""
        ### 🌟 Smart Agriculture for the Future
        **{PRODUCT_NAME}** is an device and software system that empowers farmers by providing:
        - 📉 Real-time monitoring: **Soil Moisture**, **Temperature**, **Nutrients**, **Irrigation Flow**
        - 🔄 Smart irrigation automation
        - 🔮 Crop yield predictions based on environmental data

    """)


# --- Dashboard Page ---
def dashboard():
    if not st.session_state.logged_in:
        st.warning("Please login to access the dashboard.")
        return

    st.title("📊 Sensor Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        soil_moisture = random.uniform(10, 70)
        temp = random.uniform(15, 35)
        st.metric("🌱 Soil Moisture (%)", f"{soil_moisture:.2f}")
        st.metric("🌡️ Temperature (°C)", f"{temp:.2f}")
    with col2:
        water_flow = random.uniform(1, 10)
        nutrients = random.uniform(0.2, 0.9)
        st.metric("💧 Water Flow (L/min)", f"{water_flow:.2f}")
        st.metric("🧪 Soil Nutrient Level", f"{nutrients:.2f}")

    if soil_moisture < 30:
        st.warning("⚠️ Soil moisture is low. Activating irrigation system.")
    else:
        st.success("✅ Soil moisture is adequate. Irrigation system on standby.")


# --- Prediction Page ---
def prediction():
    st.title("🔮 Crop Yield Prediction")
    st.markdown("Select a crop and adjust input values:")

    crop = st.selectbox("Choose Crop", ["Wheat", "Corn", "Rice", "Soybeans"])

    col1, col2, col3 = st.columns(3)
    with col1:
        soil_moisture = st.slider("Soil Moisture (%)", 0, 100, 50)
    with col2:
        temp = st.slider("Temperature (°C)", 0, 50, 25)
    with col3:
        nutrients = st.slider("Nutrient Level (0-1)", 0.0, 1.0, 0.5)

    crop_factors = {
        "Wheat": 1.0,
        "Corn": 1.2,
        "Rice": 1.1,
        "Soybeans": 0.9
    }
    base_yield = (soil_moisture * 0.4 + temp * 0.3 + nutrients * 100 * 0.3) / 10
    adjusted_yield = base_yield * crop_factors[crop]

    st.metric(f"Estimated Yield for {crop} (tons/ha)", f"{adjusted_yield:.2f}")


# --- About Us Page ---
def about():
    st.title("🥕 About Us")
    st.write("""
    We are a team of Brooklyn Tech students who are focused on using AI not just for convenience or luxury, but for real-world impact. Our mission began with a simple belief: that farmers are the backbone of society. Their work sustains communities, economies, and nations, yet they often lack access to cutting-edge technology.

    We chose agriculture as the foundation for this project because it's a field where technology can directly transform lives. Our goal is to turn digital innovation into practical, physical solutions that empower farmers to be more efficient and make data-driven decisions. 

    By integrating AI, IoT, and serverless cloud services, we're helping to bridge the gap between high-tech capability and grassroots needs. It's not just about improving crop yields — it's about uplifting the people and communities that depend on them.
    """)


# --- Contact Page ---
def contact():
    st.title("☎️ Contact Us")
    st.write("Contact us at: agrikit@gmail.com or 212-228-3813 for any maintenance or product concerns")


# --- About the Product Page ---
def about_product():
    st.title("📘 About the Product")
    st.markdown("""
    ## Smart AI-Driven Farming Assistant

    This system brings together:

    - **ESP32 & Sensors** to gather soil moisture, pH, temperature, rainfall, and light data.
    - **AWS API Gateway** as the secure communication bridge between the ESP32, cloud AI, and mobile app.
    - **AWS Lambda** to run on-demand code to process data, run AI models, and handle user commands.
    - **AWS DynamoDB** for fast, secure, scalable data storage.
    - **AWS SageMaker** for crop yield prediction.
    - **AWS Bedrock** to offer intelligent in-app assistance.
    - **Mobile App** to view data, receive AI decisions, and send manual commands.

    ### How It Works:
    1. ESP32 collects and sends data via API Gateway to Lambda.
    2. Lambda triggers AI models and stores results in DynamoDB.
    3. Mobile app gets data via GET requests and sends commands via POST.
    4. ESP32 receives commands from cloud and acts on them (e.g., irrigate).

    This architecture ensures real-time, automated decision-making to help farmers improve yield and efficiency through precision agriculture.
    """)


# --- Route Pages ---
if st.session_state.current_page == "Home":
    home()
elif st.session_state.current_page == "Login":
    login()
elif st.session_state.current_page == "Create Account":
    create_account()
elif st.session_state.current_page == "Dashboard":
    dashboard()
elif st.session_state.current_page == "Prediction":
    prediction()
elif st.session_state.current_page == "About Us":
    about()
elif st.session_state.current_page == "Contact Us":
    contact()
elif st.session_state.current_page == "About Product":
    about_product()
