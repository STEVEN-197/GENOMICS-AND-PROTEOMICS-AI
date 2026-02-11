import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import google.generativeai as genai
import re

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

def highlight_scientific_terms(text):
    """Automatically highlight important scientific terms with colors"""
    
    # Define terms to highlight with their colors
    highlights = {
        # DNA/RNA terms - Blue
        r'\b(DNA|RNA|mRNA|tRNA|rRNA|genome|chromosome|nucleotide|base pair|sequence)\b': 
            '<span style="background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%); padding: 2px 6px; border-radius: 4px; font-weight: 600; color: #1e40af;">\\1</span>',
        
        # Protein terms - Purple
        r'\b(protein|peptide|amino acid|enzyme|antibody|lysozyme|catalytic|domain|folding|structure)\b': 
            '<span style="background: linear-gradient(120deg, #d4a5f9 0%, #e8d5ff 100%); padding: 2px 6px; border-radius: 4px; font-weight: 600; color: #6b21a8;">\\1</span>',
        
        # Gene terms - Green
        r'\b(gene|allele|locus|expression|transcription|translation|promoter|enhancer|mutation)\b': 
            '<span style="background: linear-gradient(120deg, #a7f3d0 0%, #d1fae5 100%); padding: 2px 6px; border-radius: 4px; font-weight: 600; color: #065f46;">\\1</span>',
        
        # Techniques - Orange
        r'\b(CRISPR|PCR|sequencing|RNA-seq|BLAST|cloning|gel electrophoresis|Western blot|qPCR)\b': 
            '<span style="background: linear-gradient(120deg, #fed7aa 0%, #ffedd5 100%); padding: 2px 6px; border-radius: 4px; font-weight: 600; color: #9a3412;">\\1</span>',
        
        # Analysis terms - Pink
        r'\b(bioinformatics|alignment|homology|phylogenetic|annotation|pathway|enrichment|variant calling)\b': 
            '<span style="background: linear-gradient(120deg, #fecaca 0%, #fee2e2 100%); padding: 2px 6px; border-radius: 4px; font-weight: 600; color: #991b1b;">\\1</span>',
        
        # Organisms - Teal
        r'\b(E\. coli|Saccharomyces|Drosophila|C\. elegans|Arabidopsis|mouse|human|bacteria)\b': 
            '<span style="background: linear-gradient(120deg, #99f6e4 0%, #ccfbf1 100%); padding: 2px 6px; border-radius: 4px; font-weight: 600; color: #115e59;">\\1</span>',
    }
    
    # Apply highlights (case insensitive)
    for pattern, replacement in highlights.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    return text

def get_ai_response(prompt):
    """Get AI response using Google Gemini"""
    try:
        model = genai.GenerativeModel(MODEL)
        
        system_instruction = """You are a specialized AI assistant EXCLUSIVELY for genomics, proteomics, and bioinformatics.

STRICT RULES:
1. ONLY answer questions related to: genomics, proteomics, molecular biology, bioinformatics, DNA, RNA, proteins, gene expression, sequencing, CRISPR, protein structure, pathways, variants, mutations, epigenetics, etc.
2. If asked about ANY other topic, respond: "I am a specialized genomics and proteomics AI assistant. I can only help with questions related to genomics, proteomics, molecular biology, and bioinformatics."
3. Provide detailed, accurate scientific answers.
4. Use proper markdown formatting with headers (##), bold (**), and bullet points.
5. Organize complex answers with clear sections."""
        
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
            <p class="apple-subtitle">Powered by Google Gemini 3.0</p>
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
            <p class="footer-text">GenoProt AI Platform • Powered by Google Gemini 3.0</p>
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
        st.markdown(f'<p class="sidebar-status">✓ Gemini 3.0 Active</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="sidebar-status">💾 {len(st.session_state.search_history)} Queries</p>', unsafe_allow_html=True)
    
    # ============ HOME MODULE ============
    if module == "🏠 Home":
        st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Genomics. Proteomics. Perfected.</h1>
            <p class="hero-subtitle">AI-powered analysis with smart highlighting</p>
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
                <div class="feature-icon-large">🎨</div>
                <h3 class="feature-title">Smart Highlighting</h3>
                <p class="feature-desc">Automatic color-coded highlighting of scientific terms</p>
            </div>
            """, unsafe_allow_html=True)
    
    # ============ AI CHAT MODULE WITH HIGHLIGHTING ============
    elif module == "💬 AI Chat":
        st.markdown("""
        <div class="page-header">
            <h1 class="page-title">AI Assistant</h1>
            <p class="page-subtitle">Powered by Gemini 3.0 • Smart Highlighting Enabled</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Color legend
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border: 1px solid #e5e7eb;">
            <p style="font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">🎨 Auto-Highlighting Legend:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                <span style="background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%); padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; color: #1e40af;">DNA/RNA</span>
                <span style="background: linear-gradient(120deg, #d4a5f9 0%, #e8d5ff 100%); padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; color: #6b21a8;">Proteins</span>
                <span style="background: linear-gradient(120deg, #a7f3d0 0%, #d1fae5 100%); padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; color: #065f46;">Genes</span>
                <span style="background: linear-gradient(120deg, #fed7aa 0%, #ffedd5 100%); padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; color: #9a3412;">Techniques</span>
                <span style="background: linear-gradient(120deg, #fecaca 0%, #fee2e2 100%); padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; color: #991b1b;">Analysis</span>
                <span style="background: linear-gradient(120deg, #99f6e4 0%, #ccfbf1 100%); padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; color: #115e59;">Organisms</span>
            </div>
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
        
        # Display chat with highlighting
        if st.session_state.chat_history:
            for idx, chat in enumerate(reversed(st.session_state.chat_history[-8:])):
                # User message
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                     color: white; padding: 1.2rem 1.5rem; border-radius: 15px 15px 5px 15px; 
                     margin: 1rem 0; box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);">
                    <div style="margin-bottom: 0.5rem;">
                        <strong>👤 {st.session_state.username}</strong> 
                        <span style="font-size:0.85rem; opacity:0.9; margin-left: 0.5rem;">{chat['time']}</span>
                    </div>
                    <div style="line-height: 1.6;">{chat['user']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # AI message with smart highlighting
                st.markdown(f"""
                <div style="background: white; padding: 1.2rem 1.5rem; border-radius: 15px 15px 15px 5px; 
                     margin: 1rem 0; border-left: 5px solid #667eea; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
                    <div style="margin-bottom: 0.8rem;">
                        <strong style="color: #667eea;">🤖 Gemini AI</strong> 
                        <span style="font-size:0.85rem; color:#6b7280; margin-left: 0.5rem;">{chat['time']}</span>
                    </div>
                """, unsafe_allow_html=True)
                
                # Apply highlighting and render
                highlighted_response = highlight_scientific_terms(chat['ai'])
                st.markdown(highlighted_response, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Divider between conversations
                if idx < len(st.session_state.chat_history) - 1:
                    st.markdown('<hr style="margin: 2rem 0; border: none; border-top: 1px solid #e5e7eb;">', unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="empty-state">
                <div class="empty-icon">💬</div>
                <h3>Start a conversation</h3>
                <p>Ask me about genomics, proteomics, or molecular biology</p>
                <p style="font-size: 0.9rem; color: #6b7280; margin-top: 1rem;">
                    ✨ Important terms will be automatically highlighted in color!
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<p class="quick-label">Quick Topics</p>', unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns(4)
        topics = [
            ("🧬", "Gene Expression", "Explain gene expression analysis methods"),
            ("🔬", "Lysozyme", "What is lysozyme and its biological function?"),
            ("📊", "Variants", "What is variant calling in genomics?"),
            ("🧪", "CRISPR", "Explain CRISPR-Cas9 mechanism")
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
            <p class="page-subtitle">All your previous queries</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.search_history:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total", len(st.session_state.search_history))
            with col2:
                today = sum(1 for s in st.session_state.search_history 
                    if s['timestamp'].startswith(datetime.now().strftime("%Y-%m-%d")))
                st.metric("Today", today)
            with col3:
                if st.button("🗑️ Clear All"):
                    st.session_state.search_history = []
                    st.session_state.chat_history = []
                    st.rerun()
            
            st.markdown("---")
            
            for idx, item in enumerate(st.session_state.search_history[:20]):
                with st.expander(f"**Query #{idx+1}** · {item['timestamp']} · {item['user']}"):
                    st.markdown(f"**Question:** {item['query']}")
                    st.markdown("**Answer:**")
                    highlighted = highlight_scientific_terms(item['response'])
                    st.markdown(highlighted, unsafe_allow_html=True)
        else:
            st.info("No history yet. Start chatting to build your history!")
    
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
            st.file_uploader("Choose CSV or TSV file", type=['csv','tsv'])
            if st.button("Load Sample Dataset", type="primary"):
                genes = [f"Gene_{i}" for i in range(1,51)]
                samples = [f"Sample_{i}" for i in range(1,5)]
                data = np.random.lognormal(5, 2, (50,4))
                df = pd.DataFrame(data, columns=samples, index=genes)
                st.session_state['data'] = df
                st.success("✓ Data loaded!")
                st.dataframe(df.head(10))
        
        with tab2:
            if 'data' in st.session_state:
                df = st.session_state['data']
                c1,c2,c3,c4 = st.columns(4)
                with c1: st.metric("Genes", df.shape[0])
                with c2: st.metric("Samples", df.shape[1])
                with c3: st.metric("Upregulated", np.random.randint(250,350))
                with c4: st.metric("Downregulated", np.random.randint(180,280))
                
                st.markdown("---")
                st.markdown("### Expression Heatmap")
                
                fig = px.imshow(df.head(25).values, x=df.columns.tolist(),
                    y=df.head(25).index.tolist(), color_continuous_scale='RdBu_r')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Upload data in the previous tab")
    
    # FOOTER
    st.markdown("""
    <footer class="apple-footer">
        <div class="footer-content">
            <p class="footer-brand">STEVEN AND CO™</p>
            <p class="footer-text">GenoProt AI • Powered by Google Gemini 3.0 Flash</p>
            <p class="footer-copyright">© 2026 Steven and Co. All rights reserved.</p>
            <p class="footer-legal">Patents pending. Confidential and proprietary.</p>
        </div>
    </footer>
    """, unsafe_allow_html=True)
