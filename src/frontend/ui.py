import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from .components import (
    create_line_chart,
    create_pie_chart,
    stats_card,
    event_card,
    header,
    footer,
)


def set_page_config():
    st.set_page_config(page_title="FinSim", page_icon="💰", layout="wide")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f8fafc;
        }
        .css-1d391kg {
            background-color: white;
            border-radius: 15px;
            padding: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .stat-card {
            background-color: #f1f5f9;
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem 0;
        }
        .event-card {
            background-color: white;
            border-radius: 8px;
            padding: 0.8rem;
            margin: 0.5rem 0;
            border: 1px solid #e2e8f0;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


def show_game_ui():
    header()

    # Sample data - PLACEHOLDER !!!!!!!!!!!!!!!!!!!!!!!!!!
    financial_data = pd.DataFrame(
        {
            "date": pd.date_range(start="2024-01-01", periods=6, freq="M"),
            "value": [4000, 3800, 4200, 3900, 4100, 4300],
        }
    )

    portfolio_data = {
        "labels": ["Savings", "Investments", "Real Estate"],
        "values": [40, 35, 25],
    }

    # Main container
    with st.container():
        # Top section - Charts and Stats
        col1, col2, col3, stats_col = st.columns([1, 1, 1, 1])

        with col1:
            st.plotly_chart(create_line_chart(financial_data), use_container_width=True)

        with col2:
            st.plotly_chart(create_pie_chart(portfolio_data), use_container_width=True)

        with col3:
            st.empty()  # Placeholder

        with stats_col:
            stats = {
                "Age": "25",
                "Health": "95%",
                "Happiness": "85%",
                "Education": "Bachelor's",
            }
            stats_card("Stats", stats)

        # Bottom section - Events and Controls
        events_col, controls_col = st.columns([3, 1])

        with events_col:
            st.markdown(
                "<h3 style='font-size: 1.1rem; font-weight: 600;'>Events</h3>",
                unsafe_allow_html=True,
            )
            event_card(-1000, "Break a leg")

        with controls_col:
            # Time advancement
            st.markdown(
                """
                <div class="stat-card">
                    <div style='font-size: 0.9rem; font-weight: 500;'>Advance Time</div>
                    <div style='font-size: 1.2rem; font-weight: 600;'>6 months</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # Static events
            st.markdown(
                """
                <div class="stat-card">
                    <h4 style='font-size: 0.9rem; font-weight: 500; margin-bottom: 0.5rem;'>Events</h4>
                    <div style='font-size: 0.9rem;'>Buy house</div>
                    <div style='font-size: 0.9rem;'>Get dog</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

    footer()
