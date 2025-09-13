import streamlit as st

st.set_page_config(page_title="Anusha Parashar Portfolio", layout="wide")

# Custom CSS for card alignment and styling
st.markdown("""
<style>
    .project-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        height: 400px;
        display: flex;
        flex-direction: column;
    }
    
    .project-image {
        width: 100%;
        height: 150px;
        object-fit: cover;
        object-position: center;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    .project-title {
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        color: #333;
    }
    
    .project-description {
        font-size: 0.9rem;
        color: #666;
        flex-grow: 1;
        margin-bottom: 1rem;
        line-height: 1.4;
    }
    
    .github-button {
        background-color: #24292e;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        text-decoration: none;
        text-align: center;
        display: inline-block;
        margin-top: auto;
    }
    
    .github-button:hover {
        background-color: #444d56;
        color: white;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("Anusha Parashar")
st.markdown("""
Vellore Institute of Technology
B.Tech in Electronics & Communication (Biomedical Engineering)| CGPA 9.12/10  
📧 anushajp@gmail.com | 📞 +91-7972211730  
[LinkedIn](https://www.linkedin.com/in/anusha-j-parashar) | [GitHub](https://github.com/anewsha)
""")
st.markdown("---")

# --- About Me ---
st.header("About Me")
st.write("""
I'm a problem-solver who loves turning challenges into solutions and ideas into conversations. 
Fueled by coffee and curiosity, I make learning—and teamwork—both fun and impactful.
""")
st.markdown("---")

# --- Work Experience ---
st.header("Work Experience")
st.subheader("Tata Motors (Digital.AI Labs) – Data Science Intern, Pune")
st.write("""
- Vehicle Crank Behaviour Analysis – Time-series analysis to detect early signs of failure.  
- Paint Shop Oven Optimization – Predicted oven start-time; backend development with Flask; potential savings ₹75+ lakh/paint shop.  
- GenAI RAG Applications – Root cause analysis, HR SMART goal assistant, safety chatbot; backend/API development.  
- TCF Shop Optimization – Backend logic for Line-up buffers; Streamlit POC.
""")

st.markdown("---")

# --- Projects Section with Cards ---
st.header("Projects Portfolio")

projects = [
    {
        "title": "Chi-Squared Goodness-of-Fit with GEMS",
        "description": "Statistical analysis tool implementing chi-squared tests for goodness-of-fit testing using the GEMS dataset. Features comprehensive hypothesis testing and data visualization to validate statistical models.",
        "link": "https://github.com/anewsha/Chi-squared-Goodness-of-Fit-with-GEMS",
        "img": "chi_gems.jpg"  # your old local image
    },
    {
        "title": "XOR Neural Network from Scratch",
        "description": "Complete neural network implementation from scratch without external ML libraries. Demonstrates deep understanding of backpropagation, gradient descent, and fundamental machine learning concepts.",
        "link": "https://github.com/anewsha/XOR-NeuralNetwork-from-Scratch",
        "img": "xor_nn.jpg"  # your old local image
    },
    {
        "title": "Agentic Research Assistant",
        "description": "AI-powered research assistant that autonomously conducts comprehensive research. Features intelligent query processing, multi-source information gathering, and automated report generation.",
        "link": "https://github.com/anewsha/Agentic-Research-Assistant/tree/main",
        "img": "agentic_researcher.png"  # your old local image
    },
    {
        "title": "Construction Business Analysis (BDM)",
        "description": "Comprehensive business intelligence solution for construction industry analysis. Includes data-driven insights, performance metrics, and predictive analytics for better business decision making.",
        "link": "https://github.com/anewsha/Construction-Business-Analysis",
        "img": "bdm.png"  # your old local image
    },
    {
        "title": "British Airways Review Analysis",
        "description": "Sentiment analysis and customer insights extraction from British Airways reviews. Uses natural language processing to analyze customer feedback and provide actionable business intelligence.",
        "link": "https://github.com/anewsha/British_Airways_review_Analysis",
        "img": "ba_review.png"  # your old local image
    },
  
    {
        "title": "AI Writer Assistant",
        "description": "Intelligent writing companion powered by AI that helps create compelling content across various formats. Includes style adaptation, tone analysis, and creative writing capabilities.",
        "link": "https://github.com/anewsha/writer-AI/tree/main",
        "img": "agentic_writer.png"  # your old local image
    }
    
]


import base64

def get_image_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Display projects in aligned cards with local image support
cols_per_row = 3
for i in range(0, len(projects), cols_per_row):
    cols = st.columns(cols_per_row, gap="medium")
    
    for j in range(cols_per_row):
        if i + j < len(projects):
            project = projects[i + j]
            with cols[j]:
                # Convert local images to base64
                if project['img'].endswith((".png", ".jpg", ".jpeg")):
                    img_base64 = get_image_base64(project['img'])
                    img_src = f"data:image/png;base64,{img_base64}"
                else:
                    img_src = project['img']  # external URLs
                
                st.markdown(f"""
                <div class="project-card">
                    <img src="{img_src}" class="project-image" alt="{project['title']}">
                    <div class="project-title">{project['title']}</div>
                    <div class="project-description">{project['description']}</div>
                    <a href="{project['link']}" target="_blank" class="github-button">View GitHub</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Empty column for alignment
            with cols[j]:
                st.write("")

st.markdown("---")

# --- Skills ---
st.header("Technical Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming")
    st.write("• Python")
    st.write("• SQL")
    st.write("• FastAPI")
    st.write("• Flask")

with col2:
    st.subheader("Data Science & AI")
    st.write("• Machine Learning")
    st.write("• Deep Learning")
    st.write("• Natural Language Processing")
    st.write("• Statistical Analysis")

with col3:
    st.subheader("Tools & Frameworks")
    st.write("• Streamlit")
    st.write("• Pandas")
    st.write("• Pytorch")
    st.write("• CrewAI")

st.markdown("---")

# --- Footer ---
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>Built with ❤️ using Streamlit</p>
    <p>© 2025 Anusha Parashar - Fueled by coffee and curiosity ☕</p>
</div>
""", unsafe_allow_html=True)