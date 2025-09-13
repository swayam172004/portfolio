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
    body {
        background: linear-gradient(135deg, #0e1117, #1c1c2e);
        color: #fafafa;
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background: transparent;
    }
    h1, h2, h3, h4, h5, h6, p, div {
        color: #fafafa !important;
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background: rgba(25, 25, 35, 0.85);
        backdrop-filter: blur(12px);
        border-right: 2px solid rgba(255,255,255,0.1);
    }

    /* --- Card styles for projects --- */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 12px 30px rgba(0,0,0,0.4);
    }
    .project-title {
        font-size: 22px;
        font-weight: bold;
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* --- Buttons --- */
    .glow-btn {
        background: linear-gradient(90deg, #4CAF50, #2ecc71);
        border: none;
        color: white;
        padding: 10px 22px;
        font-size: 16px;
        border-radius: 10px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0 0 12px rgba(46, 204, 113, 0.5);
    }
    .glow-btn:hover {
        box-shadow: 0 0 24px rgba(46, 204, 113, 0.8);
        transform: scale(1.05);
    }

    /* --- Typing animation reused for hero --- */
    .typing {
        border-right: 3px solid #fff;
        white-space: nowrap;
        overflow: hidden;
        display: inline-block;
        animation: typing 4s steps(40, end) forwards, blink 0.7s step-end infinite;
    }
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    @keyframes blink {
        50% { border-color: transparent; }
    }
    </style>
    """


def get_page_content(page: str):
    page = (page or "").strip().lower()
    projects = {
    "Movie Success Predictor": {
        "desc": "A machine learning app to predict movie success.",
        "url": "https://moivesucesspredictor-kms78vyimxfuf9kdbbobhs.streamlit.app/"
    },
    "Product Price Estimator": {
        "desc": "An AI-based estimator for predicting product prices.",
        "url": "https://appuctpriceestimator-bt7ajqzqdi7j989gbmsd8z.streamlit.app/"
    },
    "Power BI: Sales Dashboard": {
        "desc": "Power BI visualization of sales data.",
        "url": "https://github.com/swayam172004/Power-BI/blob/main/VISUALIZATION.pbix"
    },
    "Power BI: E-commerce Dashboard": {
        "desc": "Power BI visualization of e-commerce data.",
        "url": "https://github.com/swayam172004/Power-BI/blob/main/ecommerce%20power%20bi.pbix"
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
            background: linear-gradient(135deg, #1e1e2f, #2c2c54);
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
    # Apply theme + hamburger CSS
    st.markdown(theme_css(), unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.title("Navigation")
    selected = st.sidebar.radio(
        "Go to:", ["Home", "About", "Projects", "Contact"], index=0
    )

    # Page routing
    page_key = selected.lower()
    data = get_page_content(page_key)

    if page_key == "home":
        home()
    else:
        st.title(data.get("title", ""))
        if page_key == "about":
            st.write(data["body"])
            st.subheader("Skills")
            for s in data.get("skills", []):
                st.write(f"✅ {s}")

        elif page_key == "projects":
            projects = list(data.get("projects", {}).items())
            # Display 2 projects per row
            for i in range(0, len(projects), 2):
                cols = st.columns(2)
                for col, (name, info) in zip(cols, projects[i:i+2]):
                    with col:
                        st.markdown(
                            f"""
                            <div class="project-card">
                                <div class="project-title">{name}</div>
                                <p>{info['desc']}</p>
                                <a href="{info['url']}" target="_blank">
                                    <button class="glow-btn">🌐 Open {name}</button>
                                </a>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

        elif page_key == "contact":   # <-- fixed indentation
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
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        import unittest

        class TestPages(unittest.TestCase):
            def test_home(self):
                d = get_page_content("home")
                self.assertIn("title", d)
                self.assertIn("body", d)
                self.assertIn("image", d)

            def test_about(self):
                d = get_page_content("about")
                self.assertIn("skills", d)
                self.assertGreater(len(d["skills"]), 0)

            def test_projects(self):
                d = get_page_content("projects")
                self.assertIn("projects", d)
                self.assertIn("Movie Success Predictor", d["projects"])

            def test_contact(self):
                d = get_page_content("contact")
                self.assertIn("title", d)
                self.assertIn("body", d)

            def test_theme_css(self):
                css = theme_css()
                self.assertIn("#0e1117", css)

        unittest.main(argv=[sys.argv[0]])
    else:
        main()














