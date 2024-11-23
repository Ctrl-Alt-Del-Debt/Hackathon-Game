import streamlit as st
import plotly.graph_objects as go

def create_line_chart(data):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data['date'],
            y=data['value'],
            mode='lines',
            line=dict(color='#4299E1', width=2),
            fill='tonexty',
            fillcolor='rgba(66, 153, 225, 0.1)'
        )
    )
    fig.update_layout(
        height=150,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        showlegend=False
    )
    return fig

def create_pie_chart(data):
    fig = go.Figure()
    fig.add_trace(
        go.Pie(
            labels=data['labels'],
            values=data['values'],
            hole=0.6,
            marker_colors=['#90CDF4', '#63B3ED', '#4299E1']
        )
    )
    fig.update_layout(
        height=150,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )
    return fig

def stats_card(title, stats):
    st.markdown(f"""
        <div class="stat-card">
            <h3 style='font-size: 1.1rem; font-weight: 600; margin-bottom: 0.8rem;'>{title}</h3>
            {''.join([f"<div style='margin: 0.5rem 0;'>{k}: {v}</div>" for k, v in stats.items()])}
        </div>
    """, unsafe_allow_html=True)

def event_card(amount, description):
    st.markdown(f"""
        <div class="event-card">
            <div style='color: {'#E53E3E' if amount < 0 else '#38A169'}; margin-bottom: 0.3rem;'>
                {amount:+.2f}$
            </div>
            <div>{description}</div>
        </div>
    """, unsafe_allow_html=True)

def header():
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='color: #2D3748; font-size: 2rem; font-weight: 700;'>Financial Life Simulator</h1>
            <p style='color: #4A5568; font-size: 1.1rem;'>Your learning tool for understanding financial decisions.</p>
        </div>
    """, unsafe_allow_html=True)

def footer():
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0; margin-top: 2rem; border-top: 1px solid #E2E8F0;'>
            <p style='color: #4A5568; font-size: 0.875rem;'>
                © 2024 Financial Life Simulator | Created with ❤️ at the Hackathon
            </p>
        </div>
    """, unsafe_allow_html=True)