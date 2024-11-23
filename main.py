import streamlit as st
import pandas as pd
import yfinance as yf
from src.app.game_engine import GameEngine
from src.app.player import Player
from src.constants.data_constants import CAREERS_LIST
from datetime import datetime, timedelta
import plotly.graph_objects as go

# Initialize session state
if "game_engine" not in st.session_state:
    st.session_state.game_engine = GameEngine()
if "player" not in st.session_state:
    st.session_state.player = None

st.set_page_config(page_title="FinSim", page_icon="💰", layout="wide")


def main():
    if st.session_state.player is None:
        show_start_screen()
    else:
        show_game_screen()


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


def show_financial_monthly(player: Player):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            y=player.salary_history,
            name="Monthly Income",
            line=dict(color="#00875A"),
        )
    )
    fig.add_trace(
        go.Scatter(
            y=player.rent_history,
            name="Current rent",
            line=dict(color="#FF0000"),
        )
    )
    fig.add_trace(
        go.Scatter(
            y=player.expenses_history,
            name="Monthly expenses",
            line=dict(color="#00FF00"),
        )
    )

    fig.update_layout(
        title="Financial History",
        height=300,
        yaxis_title="Amount ($)",
        xaxis_title="Months",
    )
    return fig


def show_financial_history(player: Player):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=player.networth_history, name="Net Worth", line=dict(color="#FFD700")
        )
    )
    fig.add_trace(
        go.Scatter(y=player.cash_history, name="Cash", line=dict(color="#4682B4"))
    )

    fig.update_layout(
        title="Financial History",
        height=300,
        yaxis_title="Amount ($)",
        xaxis_title="Months",
    )
    return fig


def show_game_screen():
    player: Player = st.session_state.player
    engine: GameEngine = st.session_state.game_engine

    st.title("FinSim 💰")
    main_bar, sidebar = st.columns([4, 1])

    with main_bar:
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.plotly_chart(show_financial_dashboard(player), use_container_width=True)
        with col2:
            st.plotly_chart(show_financial_history(player), use_container_width=True)
        with col3:
            st.plotly_chart(show_financial_monthly(player), use_container_width=True)

        show_events(engine, player)

    with sidebar:
        st.markdown("##### Age")
        st.caption("Affected by the immortal passage of time")
        st.progress(player.age_in_months / 12 / 100)
        st.write(f"{round(player.age_in_months / 12, 2)} years")
        # Happiness
        st.markdown("##### Happiness")
        st.caption("Affected by financial decisions and life events")
        st.progress(player.happiness / 100)
        st.write(f"{player.happiness}%")

        # Health
        st.markdown("##### Health")
        st.caption("Impacted by lifestyle choices and stress management")
        st.progress(player.health / 100)
        st.write(f"{player.health}%")

        # Education
        st.markdown("##### Education")
        st.caption("Represents knowledge and skills development, helps with jobs")
        st.progress(player.education / 100)
        st.write(f"{player.education}")

        st.markdown("##")

        col21, col22 = st.columns(2)
        months_to_advance = 1
        with col22:
            months_to_advance = st.selectbox(
                "", [1, 2, 4, 6, 8, 12, 24], 1, label_visibility="collapsed"
            )
        with col21:
            if st.button("Advance months", type="primary", use_container_width=True):
                for _ in range(months_to_advance):
                    player.advance_month(engine)
                st.rerun()

        show_actions(player)


def stats_card(title, stats):
    st.markdown(
        f"""
        <div class="stat-card">
            <h3 style='font-size: 1.1rem; font-weight: 600; margin-bottom: 0.8rem;'>{title}</h3>
            {''.join([f"<div style='margin: 0.5rem 0;'>{k}: {v}</div>" for k, v in stats.items()])}
        </div>
    """,
        unsafe_allow_html=True,
    )


def show_financial_dashboard(player):
    # Portfolio chart
    fig = go.Figure()
    fig.add_trace(
        go.Pie(
            labels=["Cash", "Investments", "Real Estate"],
            values=[player.cash, player.investments_value, player.real_estate_value],
            marker_colors=["#00875A", "#FFD700", "#4682B4"],
        )
    )
    fig.update_layout(height=300)
    return fig  # Return the figure instead of displaying it


def show_events(engine, player):
    for event in player.events:
        if event is None:
            continue
        st.info(event.title, icon="🚨")
        st.info(event.description)
        for option in event.options:
            if option.requirements is None or not option.requirements(player):
                if st.button(option.description):
                    option.execute(player)
                    st.rerun()
        player.events = []


def show_actions(player):

    if st.button("Invest"):
        amount = st.number_input(
            "Investment amount:", min_value=0.0, max_value=player.cash
        )
        if st.button("Confirm Investment"):
            player.invest(amount)
            st.rerun()


if __name__ == "__main__":
    main()
