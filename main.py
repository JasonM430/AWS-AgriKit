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
PRODUCT_PRICE = 249.99

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
    if st.sidebar.button("🆕 Create Account"):
        st.session_state.current_page = "Create Account"
if st.sidebar.button("📊 Dashboard"):
    st.session_state.current_page = "Dashboard"
if st.sidebar.button("🔮 Prediction"):
    st.session_state.current_page = "Prediction"
if st.sidebar.button("🛍️ Store"):
    st.session_state.current_page = "Store"
if st.sidebar.button("🧺 Cart"):
    st.session_state.current_page = "Cart"

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
    st.title("🆕 Create Account")
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

        👉 Visit the store tab to view more information on pricing and purchasing.
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

    # Simple mock model logic based on crop type
    crop_factors = {
        "Wheat": 1.0,
        "Corn": 1.2,
        "Rice": 1.1,
        "Soybeans": 0.9
    }
    base_yield = (soil_moisture * 0.4 + temp * 0.3 + nutrients * 100 * 0.3) / 10
    adjusted_yield = base_yield * crop_factors[crop]

    st.metric(f"Estimated Yield for {crop} (tons/ha)", f"{adjusted_yield:.2f}")

# --- Store Page ---
def store():
    st.title("🛍️ Store")
    st.image("https://images.unsplash.com/photo-1581090700227-1e8eaf10c177", caption=PRODUCT_NAME, use_column_width=True)
    st.subheader(PRODUCT_NAME)
    st.write(f"**Price:** ${PRODUCT_PRICE}")
    if st.button("Add to Cart"):
        st.session_state.cart.append({"product": PRODUCT_NAME, "price": PRODUCT_PRICE})
        st.success("Added to cart!")

# --- Cart Page ---
def cart():
    st.title("🧺 Your Cart")
    if not st.session_state.cart:
        st.info("Your cart is empty.")
        return
    total = 0
    for item in st.session_state.cart:
        st.write(f"- {item['product']} - ${item['price']}")
        total += item['price']
    st.markdown(f"### 🧾 Total: ${total:.2f}")
    if st.button("Checkout"):
        st.session_state.cart = []
        st.success("✅ Checkout complete! Thank you for your purchase.")

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
elif st.session_state.current_page == "Store":
    store()
elif st.session_state.current_page == "Cart":
    cart()
