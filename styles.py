import streamlit as st

def inject_premium_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        * {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        .main {
            background: linear-gradient(180deg, #f5f5f7 0%, #ffffff 100%);
        }
        
        .block-container {
            padding: 3rem 5% !important;
            max-width: 1400px !important;
        }
        
        /* Apple Navigation */
        .apple-nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 44px;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: saturate(180%) blur(20px);
            -webkit-backdrop-filter: saturate(180%) blur(20px);
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            z-index: 9999;
            animation: slideDown 0.6s ease;
        }
        
        @keyframes slideDown {
            from { transform: translateY(-100%); }
            to { transform: translateY(0); }
        }
        
        .nav-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .logo {
            font-size: 1.1rem;
            font-weight: 600;
            color: #1d1d1f;
            letter-spacing: -0.02em;
        }
        
        .tagline {
            font-size: 0.85rem;
            color: #86868b;
            font-weight: 500;
        }
        
        .nav-links {
            display: flex;
            gap: 2rem;
        }
        
        .nav-link {
            font-size: 0.875rem;
            color: #1d1d1f;
            font-weight: 400;
            cursor: pointer;
            transition: color 0.2s;
        }
        
        .nav-link:hover {
            color: #0071e3;
        }
        
        /* Login Hero */
        .login-hero {
            min-height: 85vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding-top: 44px;
        }
        
        .login-card {
            text-align: center;
            animation: fadeInUp 0.8s ease;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .icon-wrapper {
            margin-bottom: 2rem;
        }
        
        .floating-icon {
            font-size: 6rem;
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        .apple-title {
            font-size: 4rem;
            font-weight: 700;
            letter-spacing: -0.04em;
            color: #1d1d1f;
            margin-bottom: 1rem;
            line-height: 1.05;
        }
        
        .apple-subtitle {
            font-size: 1.5rem;
            font-weight: 400;
            color: #6e6e73;
            margin-bottom: 3rem;
        }
        
        /* Form Container */
        .form-container {
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(20px);
            border-radius: 18px;
            padding: 2.5rem;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        
        .stTextInput > div > div > input {
            background: #f5f5f7 !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 1rem 1.2rem !important;
            font-size: 1rem !important;
            color: #1d1d1f !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus {
            background: #ffffff !important;
            box-shadow: 0 0 0 4px rgba(0, 113, 227, 0.1) !important;
        }
        
        .stButton > button {
            background: #0071e3 !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.85rem 2rem !important;
            font-size: 1rem !important;
            font-weight: 500 !important;
            transition: all 0.3s ease !important;
            letter-spacing: -0.01em !important;
        }
        
        .stButton > button:hover {
            background: #0077ed !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0, 113, 227, 0.3) !important;
        }
        
        .demo-box {
            margin-top: 2rem;
            padding: 1.5rem;
            background: #f5f5f7;
            border-radius: 12px;
        }
        
        .demo-title {
            font-size: 0.875rem;
            font-weight: 600;
            color: #1d1d1f;
            margin-bottom: 0.75rem;
        }
        
        .demo-item {
            font-size: 0.875rem;
            color: #6e6e73;
            margin: 0.25rem 0;
            font-weight: 400;
        }
        
        /* Hero Section */
        .hero-section {
            text-align: center;
            padding: 5rem 0 4rem 0;
            margin-top: 44px;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 700;
            letter-spacing: -0.04em;
            color: #1d1d1f;
            margin-bottom: 1rem;
            line-height: 1.05;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            color: #6e6e73;
            font-weight: 400;
        }
        
        /* Stat Cards */
        .stat-card {
            background: white;
            padding: 2.5rem 2rem;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(0, 0, 0, 0.05);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .stat-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
        }
        
        .stat-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .stat-number {
            font-size: 3rem;
            font-weight: 700;
            color: #1d1d1f;
            margin: 0;
            letter-spacing: -0.03em;
        }
        
        .stat-label {
            font-size: 1rem;
            color: #86868b;
            margin-top: 0.5rem;
            font-weight: 500;
        }
        
        /* Feature Cards */
        .feature-card {
            background: white;
            padding: 3rem 2rem;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(0, 0, 0, 0.05);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            height: 100%;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
        }
        
        .feature-icon-large {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
        }
        
        .feature-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #1d1d1f;
            margin-bottom: 1rem;
            letter-spacing: -0.02em;
        }
        
        .feature-desc {
            font-size: 1rem;
            color: #6e6e73;
            line-height: 1.6;
        }
        
        /* Page Headers */
        .page-header {
            text-align: center;
            padding: 4rem 0 3rem 0;
            margin-top: 44px;
        }
        
        .page-title {
            font-size: 3rem;
            font-weight: 700;
            color: #1d1d1f;
            margin-bottom: 0.75rem;
            letter-spacing: -0.03em;
        }
        
        .page-subtitle {
            font-size: 1.2rem;
            color: #6e6e73;
        }
        
        /* Chat Container */
        .chat-container {
            background: white;
            border-radius: 18px;
            padding: 2rem;
            min-height: 500px;
            max-height: 700px;
            overflow-y: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        
        .message-group {
            margin-bottom: 2rem;
        }
        
        .message {
            padding: 1.2rem 1.5rem;
            border-radius: 16px;
            margin: 0.75rem 0;
        }
        
        .user-msg {
            background: #0071e3;
            color: white;
            margin-left: 15%;
        }
        
        .ai-msg {
            background: #f5f5f7;
            color: #1d1d1f;
            margin-right: 15%;
        }
        
        .msg-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }
        
        .msg-author {
            font-size: 0.875rem;
            font-weight: 600;
            opacity: 0.9;
        }
        
        .msg-time {
            font-size: 0.8rem;
            opacity: 0.6;
        }
        
        .msg-text {
            font-size: 1rem;
            line-height: 1.6;
            margin: 0;
        }
        
        /* History Cards */
        .history-card {
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            margin: 1rem 0;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        
        .history-card:hover {
            transform: translateX(8px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }
        
        .history-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
        }
        
        .history-number {
            font-size: 0.875rem;
            font-weight: 600;
            color: #0071e3;
        }
        
        .history-meta {
            font-size: 0.8rem;
            color: #86868b;
        }
        
        .history-content {
            padding-top: 0.75rem;
            border-top: 1px solid #f5f5f7;
        }
        
        .history-query, .history-answer {
            font-size: 0.95rem;
            line-height: 1.6;
            margin: 0.5rem 0;
            color: #1d1d1f;
        }
        
        /* Sidebar */
        .sidebar-header {
            padding: 1.5rem 0;
        }
        
        .user-profile {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .avatar {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #0071e3, #00a1ff);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 1.2rem;
        }
        
        .user-info {
            flex: 1;
        }
        
        .user-name {
            font-size: 1rem;
            font-weight: 600;
            color: #1d1d1f;
            margin: 0;
        }
        
        .user-status {
            font-size: 0.8rem;
            color: #86868b;
            margin: 0;
        }
        
        .sidebar-divider {
            height: 1px;
            background: #d2d2d7;
            margin: 1.5rem 0;
        }
        
        .sidebar-label {
            font-size: 0.75rem;
            font-weight: 600;
            color: #86868b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.75rem;
        }
        
        .sidebar-status {
            font-size: 0.875rem;
            color: #6e6e73;
            margin: 0.5rem 0;
        }
        
        /* Empty States */
        .empty-state {
            text-align: center;
            padding: 5rem 2rem;
        }
        
        .empty-icon {
            font-size: 4rem;
            margin-bottom: 1.5rem;
            opacity: 0.4;
        }
        
        .empty-state h3 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #1d1d1f;
            margin-bottom: 0.5rem;
        }
        
        .empty-state p {
            font-size: 1rem;
            color: #86868b;
        }
        
        /* Footer */
        .apple-footer {
            margin-top: 6rem;
            padding: 3rem 0;
            background: #f5f5f7;
            border-top: 1px solid #d2d2d7;
        }
        
        .footer-content {
            max-width: 1400px;
            margin: 0 auto;
            text-align: center;
        }
        
        .footer-brand {
            font-size: 1.5rem;
            font-weight: 700;
            color: #1d1d1f;
            margin-bottom: 1rem;
            letter-spacing: 0.02em;
        }
        
        .footer-text {
            font-size: 0.95rem;
            color: #6e6e73;
            margin: 0.5rem 0;
        }
        
        .footer-copyright {
            font-size: 0.875rem;
            color: #86868b;
            margin-top: 1rem;
        }
        
        .footer-legal {
            font-size: 0.8rem;
            color: #86868b;
            margin-top: 0.25rem;
        }
        
        /* Misc */
        .section-divider {
            height: 1px;
            background: #d2d2d7;
            margin: 3rem 0;
        }
        
        .section-title {
            font-size: 2rem;
            font-weight: 600;
            color: #1d1d1f;
            text-align: center;
            margin-bottom: 2rem;
            letter-spacing: -0.02em;
        }
        
        .info-pill {
            display: inline-block;
            background: #f5f5f7;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.875rem;
            color: #1d1d1f;
            font-weight: 500;
        }
        
        .quick-label {
            font-size: 0.875rem;
            font-weight: 600;
            color: #6e6e73;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }
        
        .mini-stat {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
        }
        
        .mini-stat h3 {
            font-size: 2rem;
            font-weight: 700;
            color: #1d1d1f;
            margin: 0;
        }
        
        .mini-stat p {
            font-size: 0.875rem;
            color: #86868b;
            margin-top: 0.25rem;
        }
        
        .chart-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #1d1d1f;
            margin-bottom: 1.5rem;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f5f5f7;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #d2d2d7;
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #b0b0b5;
        }
    </style>
    """, unsafe_allow_html=True)
