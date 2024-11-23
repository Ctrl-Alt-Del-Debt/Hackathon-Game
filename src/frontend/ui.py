import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from src.frontend.components import (
    create_line_chart,
    create_pie_chart,
    stats_card,
    event_card,
    header,
    footer
)

# Set the page configuration before anything else
st.set_page_config(page_title="Financial Life Simulator", layout="wide")

def inject_custom_css():
    st.markdown("""
        <style>
            .tile {
                background: white;
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            
            .main-container {
                background: white;
                border-radius: 20px;
                padding: 30px;
                margin: 20px;
            }
            
            .progress-container {
                margin: 15px 0;
            }
            
            .progress-bar {
                width: 100%;
                height: 10px;
                background: #f0f0f0;
                border-radius: 5px;
                overflow: hidden;
            }
            
            .progress-fill {
                height: 100%;
                background: #4299E1;
                transition: width 0.3s ease;
            }
            
            .progress-label {
                font-size: 14px;
                margin-bottom: 5px;
            }
            
            .progress-value {
                font-size: 12px;
                color: #666;
                margin-top: 3px;
            }
            
            .event-card {
                background: none;
                box-shadow: none;
                border: 1px solid #e1e1e1;
            }
            
            .amount {
                font-size: 18px;
                font-weight: bold;
            }
            
            .amount.positive { color: #48BB78; }
            .amount.negative { color: #F56565; }
            
            .description {
                margin: 5px 0 0 0;
                color: #4A5568;
            }
            
            .header {
                text-align: center;
                margin-bottom: 2rem;
            }
            
            .header h1 {
                color: #2D3748;
                margin-bottom: 0.5rem;
            }
            
            .header p {
                color: #4A5568;
            }
            
            footer {
                text-align: center;
                padding: 20px;
                color: #4A5568;
                position: fixed;
                bottom: 0;
                width: 100%;
                left: 0;
                background: white;
                border-top: 1px solid #e1e1e1;
            }
        </style>
    """, unsafe_allow_html=True)

def show_game_ui():
    inject_custom_css()
    
    # Header
    st.markdown(header(), unsafe_allow_html=True)
    
    with st.container():
        # Main container
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
        # Sample data
        financial_data = pd.DataFrame({
            "date": pd.date_range(start="2024-01-01", periods=6, freq="M"),
            "value": [4000, 3800, 4200, 3900, 4100, 4300],
        })
        
        portfolio_data = {
            "labels": ["Savings", "Investments", "Real Estate"],
            "values": [40, 35, 25],
        }
        
        # Top section - Charts and Stats
        col1, col2, col3, stats_col = st.columns([1, 1, 1, 1])
        
        with col1:
            st.markdown('<div class="tile">', unsafe_allow_html=True)
            st.plotly_chart(create_line_chart(financial_data), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="tile">', unsafe_allow_html=True)
            st.plotly_chart(create_pie_chart(portfolio_data), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col3:
            st.markdown('<div class="tile">', unsafe_allow_html=True)
            placeholder_data = {
                "labels": ["Category A", "Category B", "Category C"],
                "values": [33, 33, 34],
            }
            st.plotly_chart(create_pie_chart(placeholder_data), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with stats_col:
            stats = {
                "Age": "25",
                "Health": "95%",
                "Happiness": "85%",
                "Education": "Bachelor's",
            }
            st.markdown(stats_card("Stats", stats), unsafe_allow_html=True)

        # Bottom section - Events and Controls
        events_col, controls_col = st.columns([3, 1])
        
        with events_col:
            st.markdown('<div class="tile">', unsafe_allow_html=True)
            st.markdown("<h3>Events</h3>", unsafe_allow_html=True)
            st.markdown(event_card(-1000, "Break a leg"), unsafe_allow_html=True)
            st.markdown(event_card(500, "Got a bonus"), unsafe_allow_html=True)
            st.markdown(event_card(-200, "Car repair"), unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with controls_col:
            st.markdown('<div class="tile">', unsafe_allow_html=True)
            st.markdown("<h3>Controls</h3>", unsafe_allow_html=True)
            st.button("Advance 6 months")
            st.selectbox("Choose Event", ["Buy house", "Get dog", "Start business"])
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        
    # Footer
    st.markdown(footer(), unsafe_allow_html=True)
