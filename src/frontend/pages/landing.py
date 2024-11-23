import streamlit as st

from ...app.player import Player


def show_landing():
    st.markdown(
        """
        <style>
            .landing-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 80vh;
                text-align: center;
                padding: 2rem;
            }

            .main-title {
                font-size: 4rem;
                font-weight: bold;
                margin-bottom: 2rem;
                color: #2D3748;
            }

            .subtitle {
                font-size: 1.5rem;
                color: #4A5568;
                margin-bottom: 3rem;
                max-width: 600px;
            }

            .start-button {
                background-color: #4299E1;
                color: white;
                padding: 1rem 2rem;
                border-radius: 10px;
                font-size: 1.2rem;
                cursor: pointer;
                transition: background-color 0.3s ease;
                border: none;
                margin-bottom: 2rem;
            }

            .start-button:hover {
                background-color: #3182CE;
            }

            .small-text {
                font-size: 0.9rem;
                color: #718096;
            }

            .footer {
                position: fixed;
                bottom: 0;
                width: 100%;
                text-align: center;
                padding: 1rem;
                background: white;
                border-top: 1px solid #E2E8F0;
            }
        </style>

        <div class="landing-container">
            <h1 class="main-title">FinSim</h1>
            <p class="subtitle">Make smart financial decisions and build your wealth. Learn through simulation, grow through experience.</p>
            <button class="start-button" onclick="handleStartClick()">Start Your Journey</button>
            <p class="small-text">Experience the power of financial decision-making in a risk-free environment</p>
        </div>

        <div class="footer">
            © 2024 Financial Life Simulator | Created with ❤️ at the KBC + Engeto Hackathon
        </div>

        <script>
            function handleStartClick() {
                window.location.href = "?page=simulation";
            }
        </script>
    """,
        unsafe_allow_html=True,
    )
    with st.form("player_creation"):
        name = st.text_input("Your Name")
        age = st.slider("Starting Age", 18, 30, 20)
        career = st.selectbox("Initial Career", ["Student", "Employee", "Entrepreneur"])

        if st.form_submit_button("Start Your Journey"):
            st.session_state.page = "simulation"
            st.session_state.player = Player(name, age, career)
            st.rerun()
