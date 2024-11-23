import streamlit as st
import pandas as pd
import yfinance as yf
from src.app.game_engine import GameEngine
from src.app.player import Player
from src.frontend.ui import set_page_config, show_game_ui
from datetime import datetime, timedelta
import plotly.graph_objects as go

# Initialize session state
if "game_engine" not in st.session_state:
    st.session_state.game_engine = GameEngine()
if "player" not in st.session_state:
    st.session_state.player = None


def main():
    set_page_config()

    if st.session_state.player is None:
        show_start_screen()
    else:
        show_game_ui()


def show_start_screen():
    # Add CSS for layout adjustments and styling
    st.markdown(
        """
        <style>
            .center-text {
                text-align: center;
                font-family: Arial, sans-serif;
            }
            .finsim-title {
                font-size: 72px; 
                font-weight: bold;
                margin-top: 20px;
                color: black;
            }
            .finsim-tagline {
                font-size: 18px;
                color: #333333;
                margin-top: 10px;
            }
            .stButton>button {
                background-color: #007BFF; 
                color: white;
                font-size: 16px;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
            }
            .stButton>button:hover {
                background-color: #0056b3; 
            }
            .right-column {
                display: flex;
                flex-direction: column;
                justify-content: center; 
                height: 100%;
                 margin-top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Two-column layout
    col1, col2 = st.columns([1, 1])

    # Left Column: Player creation form
    with col1:
        st.markdown("## Settings")
        st.markdown("Create your player profile to start your financial journey:")

        with st.form("player_creation"):
            name = st.text_input("Your Name")
            age = st.slider("Starting Age", 12, 50, 20)
            career = st.selectbox(
                "Initial Career", ["Student", "Employee", "Entrepreneur"]
            )
            if st.form_submit_button("Start Your Journey"):
                st.session_state.player = Player(name, age, career)
                st.rerun()  

    # Right Column: Welcome Message 
    with col2:
        # Using the new right-column class for vertical centering
        st.markdown(
            """
            <div class="right-column center-text">
                <h1 class="finsim-title">FinSim</h1>
                <p class="finsim-tagline">
                    Test your financial skills in a safe, simulated environment.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
