import streamlit as st
import pandas as pd
import yfinance as yf
from src.frontend.pages.landing import show_landing
from src.app.game_engine import GameEngine
from src.app.player import Player
from src.frontend.ui import show_game_ui
from datetime import datetime, timedelta
import plotly.graph_objects as go

# Initialize session state
if "game_engine" not in st.session_state:
    st.session_state.game_engine = GameEngine()
if "player" not in st.session_state:
    st.session_state.player = None


# def main():
#     st.title("Financial Life Simulator 💰")

#     if st.session_state.player is None:
#         show_start_screen()
#     else:
#         show_game_screen()


def main():
    if "page" not in st.session_state:
        st.session_state.page = "landing"

    player = st.session_state.player
    engine = st.session_state.game_engine

    # Show appropriate page
    if st.session_state.page == "landing":
        show_landing()
    else:
        show_game_ui(player)


def show_start_screen():
    st.markdown(
        """
    ## Welcome to Financial Life Simulator!
    Make smart financial decisions and build your wealth!
    """
    )


def show_game_screen():
    player = st.session_state.player
    engine = st.session_state.game_engine

    # Player stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Age", f"{player.age} years")
    with col2:
        st.metric("Cash", f"${player.cash:,.2f}")
    with col3:
        st.metric("Net Worth", f"${player.net_worth:,.2f}")

    # Financial Dashboard
    st.subheader("Financial Overview")
    show_financial_dashboard(player)

    # Events and Decisions
    st.subheader("Current Events")
    handle_events(engine, player)

    # Actions
    st.subheader("Available Actions")
    show_actions(player)


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
    st.plotly_chart(fig, use_container_width=True)


def handle_events(engine, player):
    current_event = engine.get_current_event()
    if current_event:
        st.info(current_event.description)
        for option in current_event.options:
            if st.button(option.description):
                option.execute(player)
                st.rerun()


def show_actions(player):
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Invest"):
            amount = st.number_input(
                "Investment amount:", min_value=0.0, max_value=player.cash
            )
            if st.button("Confirm Investment"):
                player.invest(amount)
                st.rerun()

    with col2:
        if st.button("Next Month"):
            player.advance_month()
            st.rerun()


if __name__ == "__main__":
    main()
