import plotly.graph_objects as go
import streamlit as st

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

def create_progress_bar(value, max_value, label):
    progress = value / max_value
    return f"""
        <div class="progress-container">
            <div class="progress-label">{label}</div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <div class="progress-value">{value}</div>
        </div>
    """

def stats_card(title, stats):
    progress_bars = ""
    education_levels = {"No Education": 0, "High School": 25, "Bachelor's": 50, "Master's": 75, "PhD": 100}
    
    for k, v in stats.items():
        if k == "Age":
            progress_bars += create_progress_bar(int(v), 99, "Age")
        elif k == "Education":
            edu_value = education_levels.get(v, 0)
            progress_bars += create_progress_bar(edu_value, 100, "Education")
        else:
            progress_bars += create_progress_bar(int(v.strip('%')), 100, k)
    
    return f"""
        <div class="tile stats-card">
            <h3>{title}</h3>
            {progress_bars}
        </div>
    """

def event_card(amount, description):
    color = "positive" if amount >= 0 else "negative"
    return f"""
        <div class="tile event-card">
            <span class="amount {color}">{amount:+.2f}$</span>
            <p class="description">{description}</p>
        </div>
    """

def header():
    return """
        <div class="header tile">
            <h1>Financial Life Simulator</h1>
            <p>Your learning tool for understanding financial decisions.</p>
        </div>
    """

def footer():
    return """
        <footer>
            © 2024 Financial Life Simulator | Created with ❤️ at the KBC + Engeto Hackathon
        </footer>
    """
