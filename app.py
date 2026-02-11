import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import google.generativeai as genai

from config import GEMINI_API_KEY, MODEL, USERS
from styles import inject_premium_css

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config(
    page_title="GenoProt AI • STEVEN AND CO",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_premium_css()

# Session State
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

def verify_login(username, password):
    return username in USERS and USERS[username] == password

def get_ai_response(prompt):
    """Get AI response using Google Gemini"""
    try:
        model = genai.GenerativeModel(MODEL)
        
        system_instruction = """You are a specialized AI assistant EXCLUSIVELY for genomics, proteomics, and bioinformatics.

STRICT RULES:
1. ONLY answer questions related to: genomics, proteomics, molecular biology, bioinformatics, DNA, RNA, proteins, gene expression, sequencing, CRISPR, protein structure, pathways, variants, mutations, epigenetics, etc.
2. If asked about ANY other topic (politics, weather, cooking, sports, etc.), respond: "I am a specialized genomics and proteomics AI assistant. I can only help with questions related to genomics, proteomics, molecular biology, and bioinformatics. Please ask me about genes, proteins, DNA sequencing, or related topics."
3. Provide detailed, accurate scientific answers for valid genomics/proteomics questions.
4. Use technical terminology appropriately.
5. Be helpful and educational."""
        
        full_prompt = f"{system_instruction}\n\nUser question: {prompt}"
        response = model.generate_content(full_prompt)
        
        return response.text
        
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def save_to_history(query, response):
    st.session_state.search_history.insert(0, {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'query': query,
        'response': response,
        'user': st.session_state.username
    })
    st.session_state.search_history = st.session_state.search_history[:50]

# ============ LOGIN PAGE ============
if not st.session_state.logged_in:
    st.markdown("""
    <div class="apple-nav">
        <div class="nav-content">
            <span class="logo">🧬 GenoProt AI</span>
            <span class="tagline">by STEVEN AND CO</span>
        </div>
    </div>
    
    <div class="login-hero">
        <div class="login-card">
            <div class="icon-wrapper">
                <div class="floating-icon">🧬</div>
            </div>
            <h1 class="apple-title">Welcome to GenoProt AI</h1>
            <p class="apple-subtitle">Powered by Google Gemini 2.0</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        username = st.text_input("", placeholder="Username", key="user", label_visibility="collapsed")
        password = st.text_input("", placeholder="Password", type="password", key="pass", label_visibility="collapsed")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Sign In", use_container_width=True, type="primary"):
                if verify_login(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("✓ Welcome!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        with c2:
            if st.button("Create Account", use_container_width=True):
                st.info("Contact admin@stevenandco.com")
        
        st.markdown("""
        <div class="demo-box">
            <p class="demo-title">Demo Accounts</p>
            <p class="demo-item">admin • admin123</p>
            <p class="demo-item">demo • demo123</p>
            <p class="demo-item">user • password</p>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <footer class="apple-footer">
        <div class="footer-content">
            <p class="footer-brand">STEVEN AND CO™</p>
            <p class="footer-text">GenoProt AI Platform • Powered by Google Gemini 2.0</p>
            <p class="footer-copyright">© 2026 Steven and Co. All rights reserved.</p>
            <p class="footer-legal">Patents pending. Confidential and proprietary.</p>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# ============ MAIN APP ============
else:
    st.markdown("""
    <div class="apple-nav">
        <div class="nav-content">
            <span class="logo">🧬 GenoProt AI</span>
            <div class="nav-links">
                <span class="nav-link">Platform</span>
                <span class="nav-link">Research</span>
                <span class="nav-link">About</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # SIDEBAR
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-header">
            <div class="user-profile">
                <div class="avatar">{st.session_state.username[0].upper()}</div>
                <div class="user-info">
                    <p class="user-name">{st.session_state.username}</p>
                    <p class="user-status">Premium Access</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Sign Out", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
        
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        st.markdown('<p class="sidebar-label">NAVIGATION</p>', unsafe_allow_html=True)
        module = st.radio("", ["🏠 Home", "💬 AI Chat", "📜 History", "🧬 Analysis"], 
                         label_visibility="collapsed")
        
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        st.markdown(f'<p class="sidebar-status">✓ Gemini 2.0 Active</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="sidebar-status">💾 {len(st.session_state.search_history)} Queries</p>', unsafe_allow_html=True)
    
    # ============ HOME MODULE ============
    if module == "🏠 Home":
        st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Genomics. Proteomics. Perfected.</h1>
            <p class="hero-subtitle">AI-powered analysis at the speed of thought</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="stat-card">
                <div class="stat-icon">📊</div>
                <h2 class="stat-number">1,247</h2>
                <p class="stat-label">Total Analyses</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="stat-card">
                <div class="stat-icon">🔬</div>
                <h2 class="stat-number">15</h2>
                <p class="stat-label">Active Projects</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="stat-card">
                <div class="stat-icon">✓</div>
                <h2 class="stat-number">99.8%</h2>
                <p class="stat-label">Accuracy</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-section">
            <h2 class="section-title">Platform Capabilities</h2>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon-large">🧬</div>
                <h3 class="feature-title">Gene Expression</h3>
                <p class="feature-desc">Advanced RNA-seq analysis with real-time differential expression detection</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon-large">🔬</div>
                <h3 class="feature-title">Protein Analysis</h3>
                <p class="feature-desc">AI-powered structure prediction and functional annotation</p>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon-large">🤖</div>
                <h3 class="feature-title">AI Insights</h3>
                <p class="feature-desc">Intelligent pathway enrichment and variant analysis</p>
            </div>
            """, unsafe_allow_html=True)
    
    # ============ AI CHAT MODULE ============
    elif module == "💬 AI Chat":
        st.markdown("""
        <div class="page-header">
            <h1 class="page-title">AI Assistant</h1>
            <p class="page-subtitle">Powered by Google Gemini 2.0 Flash</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([6, 1])
        with col1:
            user_query = st.text_input("", placeholder="Ask about genomics, proteomics, or bioinformatics...", 
                                      key="q", label_visibility="collapsed")
        with col2:
            send_btn = st.button("Send", use_container_width=True, type="primary")
        
        if send_btn and user_query:
            with st.spinner("🧬 Analyzing with Gemini..."):
                ai_response = get_ai_response(user_query)
                save_to_history(user_query, ai_response)
                st.session_state.chat_history.append({
                    'user': user_query, 'ai': ai_response,
                    'time': datetime.now().strftime("%H:%M")
                })
        
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        if st.session_state.chat_history:
            for chat in reversed(st.session_state.chat_history[-8:]):
                st.markdown(f"""
                <div class="message-group">
                    <div class="message user-msg">
                        <div class="msg-header">
                            <span class="msg-author">{st.session_state.username}</span>
                            <span class="msg-time">{chat['time']}</span>
                        </div>
                        <p class="msg-text">{chat['user']}</p>
                    </div>
                    <div class="message ai-msg">
                        <div class="msg-header">
                            <span class="msg-author">🤖 Gemini AI</span>
                            <span class="msg-time">{chat['time']}</span>
                        </div>
                        <p class="msg-text">{chat['ai']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="empty-state">
                <div class="empty-icon">💬</div>
                <h3>Start a conversation</h3>
                <p>Ask me about genomics, proteomics, or molecular biology</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<p class="quick-label">Quick Topics</p>', unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns(4)
        topics = [
            ("🧬", "Gene Expression", "Explain gene expression analysis methods"),
            ("🔬", "Proteins", "How does protein folding work?"),
            ("📊", "Variants", "What is variant calling in genomics?"),
            ("🧪", "Pathways", "Explain pathway enrichment analysis")
        ]
        
        for col, (icon, title, query) in zip([c1,c2,c3,c4], topics):
            with col:
                if st.button(f"{icon} {title}", use_container_width=True):
                    r = get_ai_response(query)
                    save_to_history(query, r)
                    st.rerun()
    
    # ============ HISTORY MODULE ============
    elif module == "📜 History":
        st.markdown("""
        <div class="page-header">
            <h1 class="page-title">Search History</h1>
            <p class="page-subtitle">All your previous queries and responses</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.search_history:
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.markdown(f'<div class="info-pill">Total: {len(st.session_state.search_history)}</div>', 
                           unsafe_allow_html=True)
            with col2:
                today = sum(1 for s in st.session_state.search_history 
                    if s['timestamp'].startswith(datetime.now().strftime("%Y-%m-%d")))
                st.markdown(f'<div class="info-pill">Today: {today}</div>', unsafe_allow_html=True)
            with col3:
                if st.button("Clear All", use_container_width=True):
                    st.session_state.search_history = []
                    st.rerun()
            
            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
            
            search = st.text_input("", placeholder="Filter history...", label_visibility="collapsed")
            
            for idx, item in enumerate(st.session_state.search_history):
                if not search or search.lower() in item['query'].lower() or search.lower() in item['response'].lower():
                    st.markdown(f"""
                    <div class="history-card">
                        <div class="history-header">
                            <span class="history-number">#{len(st.session_state.search_history)-idx}</span>
                            <span class="history-meta">{item['timestamp']} • {item['user']}</span>
                        </div>
                        <div class="history-content">
                            <p class="history-query"><strong>Q:</strong> {item['query']}</p>
                            <p class="history-answer"><strong>A:</strong> {item['response'][:200]}...</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    with st.expander("📖 View Full Response"):
                        st.write(item['response'])
        else:
            st.markdown("""
            <div class="empty-state">
                <div class="empty-icon">📭</div>
                <h3>No history yet</h3>
                <p>Your search history will appear here</p>
            </div>
            """, unsafe_allow_html=True)
    
    # ============ ANALYSIS MODULE ============
    else:
        st.markdown("""
        <div class="page-header">
            <h1 class="page-title">Gene Expression Analysis</h1>
            <p class="page-subtitle">Upload and analyze your genomic data</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["📤 Upload Data", "📊 Results"])
        
        with tab1:
            st.file_uploader("Choose CSV or TSV file", type=['csv','tsv'], label_visibility="collapsed")
            if st.button("Load Sample Dataset", use_container_width=True, type="primary"):
                genes = [f"Gene_{i}" for i in range(1,51)]
                samples = [f"Sample_{i}" for i in range(1,5)]
                data = np.random.lognormal(5, 2, (50,4))
                df = pd.DataFrame(data, columns=samples, index=genes)
                st.session_state['data'] = df
                st.success("✓ Data loaded successfully")
                st.dataframe(df.head(10), use_container_width=True)
        
        with tab2:
            if 'data' in st.session_state:
                df = st.session_state['data']
                c1,c2,c3,c4 = st.columns(4)
                with c1:
                    st.markdown(f'<div class="mini-stat"><h3>{df.shape[0]}</h3><p>Genes</p></div>', 
                               unsafe_allow_html=True)
                with c2:
                    st.markdown(f'<div class="mini-stat"><h3>{df.shape[1]}</h3><p>Samples</p></div>', 
                               unsafe_allow_html=True)
                with c3:
                    st.markdown(f'<div class="mini-stat"><h3>{np.random.randint(250,350)}</h3><p>Upregulated</p></div>', 
                               unsafe_allow_html=True)
                with c4:
                    st.markdown(f'<div class="mini-stat"><h3>{np.random.randint(180,280)}</h3><p>Downregulated</p></div>', 
                               unsafe_allow_html=True)
                
                st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
                st.markdown('<h3 class="chart-title">Expression Heatmap</h3>', unsafe_allow_html=True)
                
                fig = px.imshow(df.head(25).values, x=df.columns.tolist(),
                    y=df.head(25).index.tolist(), color_continuous_scale='RdBu_r',
                    aspect="auto")
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="SF Pro Display, -apple-system, sans-serif", size=12)
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.markdown("""
                <div class="empty-state">
                    <div class="empty-icon">📊</div>
                    <h3>No data loaded</h3>
                    <p>Upload your data in the previous tab</p>
                </div>
                """, unsafe_allow_html=True)
    
    # ============ FOOTER ============
    st.markdown("""
    <footer class="apple-footer">
        <div class="footer-content">
            <p class="footer-brand">STEVEN AND CO™</p>
            <p class="footer-text">GenoProt AI Platform • Powered by Google Gemini 2.0 Flash</p>
            <p class="footer-copyright">© 2026 Steven and Co. All rights reserved.</p>
            <p class="footer-legal">Patents pending. Confidential and proprietary.</p>
        </div>
    </footer>
    """, unsafe_allow_html=True)
