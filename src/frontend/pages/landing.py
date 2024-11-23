import streamlit as st

def show_landing():
    # Custom CSS 
    st.markdown("""
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 1.5s ease-out forwards;
            opacity: 0;
        }
        
        .fade-in-delay-1 {
            animation: fadeIn 1.5s ease-out 0.5s forwards;
            opacity: 0;
        }
        
        .fade-in-delay-2 {
            animation: fadeIn 1.5s ease-out 1s forwards;
            opacity: 0;
        }
        
        .main-heading {
            font-size: 3.5rem;
            font-weight: 700;
            color: #1a365d;
            text-align: center;
            margin: 2rem 0;
        }
        
        .sub-heading {
            font-size: 1.5rem;
            color: #4a5568;
            text-align: center;
            margin: 1.5rem 0;
            line-height: 1.5;
        }
        
        .centered-button {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
        }
        
        .start-button {
            background-color: #4299e1;
            color: white;
            padding: 1rem 2rem;
            border-radius: 9999px;
            font-size: 1.25rem;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .start-button:hover {
            background-color: #2b6cb0;
            transform: translateY(-2px);
        }
        
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 1rem;
            background-color: #f7fafc;
            text-align: center;
            font-size: 0.875rem;
            color: #4a5568;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main content with animations
    st.markdown("""
        <div class="fade-in main-heading">
            FinSim
        </div>
        
        <div class="fade-in-delay-1 sub-heading">
            Make smart financial decisions and build your wealth.<br>
            Learn through simulation, grow through experience.
        </div>
        
        <div class="fade-in-delay-2 centered-button">
            <button class="start-button" onclick="window.location.href='?page=simulation'">
                Start Your Journey
            </button>
        </div>
        
        <div class="footer">
            <p>© 2024 Financial Life Simulator | Created with ❤️ at the KBC + Engeto Hackathon</p>
        </div>
    """, unsafe_allow_html=True)

    # Handle button click 
    if st.button("Start Your Journey", key="start_button", type="primary"):
        st.session_state.page = "simulation"
        st.rerun()