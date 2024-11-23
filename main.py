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


# def main():
#     st.title("Financial Life Simulator 💰")

#     if st.session_state.player is None:
#         show_start_screen()
#     else:
#         show_game_screen()


def main():
    set_page_config()
    show_game_ui()


def show_start_screen():
    st.markdown(
        """
    ## Welcome to Financial Life Simulator!
    Make smart financial decisions and build your wealth!
    """
    )

    with st.form("player_creation"):
        name = st.text_input("Your Name")
        age = st.slider("Starting Age", 12, 50, 20)
        career = st.selectbox("Initial Career", ["Student", "Employee", "Entrepreneur"])

        if st.form_submit_button("Start Your Journey"):
            st.session_state.player = Player(name, age, career)
            st.rerun()


def show_financial_history(player):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            y=player.salary_history, name="Monthly Income", line=dict(color="#00875A")
        )
    )
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
    player = st.session_state.player
    engine = st.session_state.game_engine

    # Player stats
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric("Age", f"{player.age_in_months / 12} years")
    with col2:
        st.metric("Cash", f"${player.cash:,.2f}")
    with col3:
        st.metric("Net Worth", f"${player.net_worth:,.2f}")

    # Player well-being stats
    st.markdown("### 🎯 Personal Development Stats")

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
    st.caption("Represents knowledge and skills development")
    st.progress(player.education / 100)
    st.write(f"{player.education}%")

    # Financial Dashboard
    st.subheader("Financial Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(show_financial_dashboard(player), use_container_width=True)
    with col2:
        st.plotly_chart(show_financial_history(player), use_container_width=True)

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
    return fig  # Return the figure instead of displaying it


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
        col21, col22 = st.columns(2)
        months_to_advance = 1
        with col22:
            months_to_advance = st.selectbox("Months to advance:", range(1, 13), 1)
        with col21:
            if st.button("Next Month"):
                for _ in range(months_to_advance):
                    player.advance_month()
                st.rerun()


if __name__ == "__main__":
    main()
