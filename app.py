# -*- coding: utf-8 -*-
import sys

try:
    import streamlit as st
except ImportError:
    st = None


# ✅ First Streamlit command
if st:
    st.set_page_config(page_title="My Portfolio", page_icon="✨", layout="wide")


def theme_css():
    return """
        <style>
        body { background-color: #0e1117; color: #fafafa; }
        .stApp { background-color: #0e1117; color: #fafafa; }
        h1, h2, h3, h4, h5, h6, p, div { color: #fafafa !important; }

        /* Sidebar hamburger */
        button[kind="header"] div[data-testid="collapsedControl"] svg {
            display: none;
        }
        button[kind="header"] div[data-testid="collapsedControl"]::before {
            content: "☰";
            font-size: 26px;
            color: #fafafa;
            font-weight: bold;
        }

        /* Skill tags */
        .skill-tag {
            display: inline-block;
            background: linear-gradient(135deg, #4CAF50, #2e7d32);
            color: white;
            padding: 6px 14px;
            border-radius: 25px;
            margin: 5px;
            font-size: 14px;
            font-weight: 500;
            box-shadow: 0 3px 8px rgba(0,0,0,0.4);
            transition: transform 0.2s ease, box-shadow 0.3s ease;
        }
        .skill-tag:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 15px rgba(0,0,0,0.6);
        }

        /* Project cards */
        .project-card {
            background: linear-gradient(135deg, #1f1f2e, #292946);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0 6px 15px rgba(0,0,0,0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 25px rgba(0,0,0,0.6);
        }
        .project-title {
            font-size: 22px;
            font-weight: 600;
            color: #fff;
            margin-bottom: 8px;
        }
        .project-desc {
            font-size: 15px;
            color: #cfcfcf;
            margin-bottom: 15px;
        }
        .project-btn {
            background: #4CAF50;
            color: white !important;
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 15px;
            transition: background 0.3s ease;
        }
        .project-btn:hover {
            background: #45a049;
        }

        /* Contact form */
        .stTextInput > div > div > input,
        .stTextArea > div > textarea {
            background-color: #1f1f2e;
            color: white;
            border-radius: 10px;
            border: 1px solid #4CAF50;
        }
        </style>
    """


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
    st.markdown(
        """
        <style>
        .big-card {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 90vh;
            background: linear-gradient(135deg, #1e1e2f, #2c2c54, #3a3a7a);
            border-radius: 20px;
            padding: 30px 15px;
            color: white;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .typing {
            border-right: 2px solid white;
            white-space: nowrap;
            overflow: hidden;
            max-width: 95vw;
            animation: typing 4s steps(40, end) forwards, blink 0.7s step-end infinite;
        }
        @keyframes typing { from { width: 0; } to { width: 100%; } }
        @keyframes blink { 50% { border-color: transparent; } }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="big-card">
            <h2 class="typing">Hi, I'm <b>Swayam Sikarwar</b> ✨</h2>
            <h3 class="typing">Data Science Enthusiast | Aspiring Researcher</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )


def run_streamlit():
    st.markdown(theme_css(), unsafe_allow_html=True)

    st.sidebar.title("Navigation")
    selected = st.sidebar.radio("Go to:", ["Home", "About", "Projects", "Contact"], index=0)

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
                            f""
                            <div class="project-card">
                                <div class="project-title">{name}</div>
                                <div class="project-desc">{info['desc']}</div>
                                <a href="{info['url']}" target="_blank" class="project-btn">\U0001F310 Open {name}</a>
                            </div>
                            "",
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


