# -*- coding: utf-8 -*-
import sys

try:
    import streamlit as st
except ImportError:
    st = None

if st:
    st.set_page_config(page_title="My Portfolio", page_icon="✨", layout="wide")

def theme_css():
    return """<style>
    /* Add your CSS styling here */
    .project-card {
        background: #1e1e1e;
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .project-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .project-desc {
        font-size: 14px;
        margin-bottom: 10px;
    }
    .project-btn {
        display: inline-block;
        padding: 8px 12px;
        background: #4CAF50;
        color: white;
        text-decoration: none;
        border-radius: 6px;
        transition: background 0.3s;
    }
    .project-btn:hover {
        background: #45a049;
    }
    .skill-tag {
        display: inline-block;
        margin: 4px;
        padding: 6px 10px;
        background: #444;
        color: #fff;
        border-radius: 8px;
        font-size: 13px;
    }
    </style>"""

def get_page_content(page: str):
    page = (page or "").strip().lower()
    projects = {
        "Movie Success Predictor": {
            "desc": "A machine learning app to predict movie success.",
            "url": "https://moivesucesspredictor-kms78vyimxfuf9kdbbobhs.streamlit.app/",
        },
        "Product Price Estimator": {
            "desc": "An AI-based estimator for predicting product prices.",
            "url": "https://appuctpriceestimator-bt7ajqzqdi7j989gbmsd8z.streamlit.app/",
        },
        "Power BI: Sales Dashboard": {
            "desc": "Power BI visualization of sales data.",
            "url": "https://github.com/swayam172004/Power-BI/blob/main/VISUALIZATION.pbix",
        },
        "Power BI: E-commerce Dashboard": {
            "desc": "Power BI visualization of e-commerce data.",
            "url": "https://github.com/swayam172004/Power-BI/blob/main/ecommerce%20power%20bi.pbix",
        },
    }

    skills = ["Python", "Streamlit", "Machine Learning", "Data Science", "SQL", "Git"]

    if page == "home":
        return {"title": "Home", "body": "Welcome to my portfolio!", "image": None}
    if page == "about":
        return {
            "title": "About Me",
            "body": (
                "I'm Swayam Sikarwar, a passionate developer who loves exploring Data Science, "
                "Machine Learning, and Web Development. "
                "This portfolio showcases my journey, skills, and projects."
            ),
            "skills": skills,
        }
    if page == "projects":
        return {"title": "My Projects", "projects": projects}
    if page == "contact":
        return {
            "title": "📬 Get in Touch",
            "body": "Feel free to connect with me through this form below.",
        }
    return {"title": "Not Found", "body": "The requested page does not exist."}

def home():
    st.markdown("""<style>
    /* Add animated typing effect if needed */
    </style>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="big-card">
        <h2 class="typing">Hi, I'm <b>Swayam Sikarwar</b> ✨</h2>
        <h3 class="typing">Data Science Enthusiast | Aspiring Researcher</h3>
    </div>
    """, unsafe_allow_html=True)

def run_streamlit():
    st.markdown(theme_css(), unsafe_allow_html=True)

    st.sidebar.title("Navigation")
    selected = st.sidebar.radio("Go to:", ["Home", "About", "Projects", "Contact"], index=0)

    # ✅ Social Media Links
    st.sidebar.markdown("### Connect with me")
    st.sidebar.markdown("""
    [![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/swayam172004)  
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/swayam172004/)  
    [![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue?logo=kaggle)](https://www.kaggle.com/swayam172004)
    """, unsafe_allow_html=True)

    page_key = selected.lower()
    data = get_page_content(page_key)

    if page_key == "home":
        home()
    else:
        st.title(data.get("title", ""))
        if page_key == "about":
            st.write(data["body"])
            st.subheader("Skills")
            st.markdown(
                "".join([f"<span class='skill-tag'>{s}</span>" for s in data.get("skills", [])]),
                unsafe_allow_html=True,
            )

        elif page_key == "projects":
            projects = list(data.get("projects", {}).items())
            for i in range(0, len(projects), 2):
                cols = st.columns(2)
                for col, (name, info) in zip(cols, projects[i:i+2]):
                    with col:
                        st.markdown(
                            f"""
                            <div class="project-card">
                                <div class="project-title">{name}</div>
                                <div class="project-desc">{info['desc']}</div>
                                <a href="{info['url']}" target="_blank" class="project-btn">Open {name}</a>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

        elif page_key == "contact":
            st.write(data["body"])
            with st.form("contact_form"):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Message")
                submit = st.form_submit_button("Send")
                if submit:
                    st.success("Thanks! Your message has been sent.")

def run_cli():
    pages = ["home", "about", "projects", "contact"]
    for p in pages:
        d = get_page_content(p)
        print("== " + d.get("title", ""))
        if p == "home":
            print(d.get("body", ""))
        elif p == "about":
            print(d.get("body", ""))
            print("SKILLS:" + ", ".join(d.get("skills", [])))
        elif p == "projects":
            for k, v in d.get("projects", {}).items():
                print(f"{k}: {v['desc']} (URL: {v['url']})")
        elif p == "contact":
            print(d.get("body", ""))

def main():
    if st is not None:
        run_streamlit()
    else:
        run_cli()

if __name__ == "__main__":
    main()
