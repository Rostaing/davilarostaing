import streamlit as st
from PIL import Image
from pathlib import Path
import datetime

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

profile_pic = current_dir / "assets" / "profile-pic.png"
info_pic = current_dir / "assets" / "info.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Davila Rostaing | Digital CV "
PAGE_ICON = "assets/logo.jpg"
NAME = "Davila Rostaing"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Masquer le menu principal de Streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Choix de la langue
lang = st.sidebar.selectbox("Choisir la langue / Choose language", ["Français", "English"])

# Traductions
def tr(fr, en):
    return fr if lang == "Français" else en

# Chargement de l'image de profil (ajouter votre photo dans le répertoire)
image = Image.open("assets/me.jpg")

# ------------------------------- Page d'accueil -------------------------------
# Année de début de l'expérience professionnelle
annee_debut = 2020  # Remplace par ton année de début réelle

# Calcul dynamique des années d'expérience
annees_experience = datetime.datetime.now().year - annee_debut

col1, col2 = st.columns([1,2])
col1.markdown("<div style='margin-top: 50px;'>", unsafe_allow_html=True)

# Redimensionner l'image (largeur x hauteur)
image_resized = image.resize((252, 290))  # Largeur = 250px, Hauteur = 300px
col1.image(image_resized)

col1.markdown("</div>", unsafe_allow_html=True)

# col1.image(image, width=150)
# col2.write("\n\n")
  
col2.title("Davila Rostaing")
col2.write(tr(
    f"**Data Scientist** et **Informaticien** avec plus de **{annees_experience} ans d'expérience**, passionné par l’analyse et la valorisation des données. Également créateur de contenu sur **YouTube**, où je partage mes connaissances en analyse de données, data science, intelligence artificielle et programmation à travers des tutoriels pratiques et des études de cas. Mon objectif est d'exploiter, analyser et modéliser des ensembles de données complexes afin d'apporter des solutions innovantes et adaptées aux défis concrets des entreprises, en optimisant leurs processus décisionnels et leur transformation digitale.",
    f"**Data Scientist** and **IT Specialist** with over **5 years of experience**, passionate about data analysis and leveraging data for actionable insights. Also a content creator on **YouTube**, where I share my knowledge in data analysis, data science, artificial intelligence, and programming through practical tutorials and case studies. My goal is to explore, analyze, and model complex datasets to provide innovative and tailored solutions to real-world business challenges, optimizing decision-making processes and driving digital transformation."
))

col2.markdown(
    """
    <div style="display: flex; gap: 10px;">
        <a href="https://www.linkedin.com/in/davila-rostaing" target="_blank">
            <button style="color: white; background-color: #0073b1; border: none; padding: 5px 10px; cursor: pointer;">LinkedIn</button>
        </a>
        <a href="https://www.youtube.com/@RostaingAI" target="_blank">
            <button style="color: white; background-color: red; border: none; padding: 5px 10px; cursor: pointer;">YouTube</button>
        </a>
        <a href="mailto:davilarostaing@gmail.com" target="_blank">
            <button style="color: white; background-color: #D44638; border: none; padding: 5px 10px; cursor: pointer;">Email</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ------------------------------- Menu -------------------------------
menu = st.sidebar.radio(tr("Navigation", "Navigation"), [tr("Accueil", "Home"), tr("Compétences", "Skills"), tr("Expériences", "Experiences"), tr("Formations", "Educations"), tr("Certifications", "Certifications"), tr("Projets", "Projects"), tr("Distinctions & Récompenses", "Honors & Awards"), tr("Langues", "Languages"), tr("Organisations", "Organizations"), tr("Centres d'intérêt", "Hobbies")])

# ------------------------------- Section Compétences -------------------------------
if menu == tr("Compétences", "Skills"):
    st.subheader(tr("Compétences Techniques", "Technical Skills"))

    with st.expander(tr("### Langages de programmation", "### Programming languages")):
        st.write("Python, R, Java, Scala, JavaScript, PHP, C, Ruby, Dax...")

    with st.expander(tr("### Frameworks & Plateforme IA", "### Frameworks & AI platform")):
        st.write("Streamlit, Langchain, Phidata, Embedchain, Keras, Tensorflow, PyTorch, Flask, Ruby on Rails, Hugging Face, Ollama, Langflow, FlowiseAI, MLflow...")
    
    with st.expander(tr("### Base de données", "### Database")):
        st.write("MongoDB, Neo4j, ChromaDB, Oracle, PostgreSQL, MySQL, SQL Sever, Sqlite...")

    with st.expander(tr("### Data Engineering", "### Data Engineering")):
        st.write("Spark, Hadoop, SQL, SQLAlchemy, NoSQL, ETL, Denodo, Talend, Docker, Docling, Markitdown, HTML, JSON, API, VBA, Excel, Beautiful Soup, Scrapy, ScrapeGraphAI...")
    
    with st.expander(tr("### Data Analysis", "### Data Analysis")):
        st.write("Pandas, Polars, Numpy, Power BI, Tableau, Seaborn, Matplotlib, Skimpy, dtale, Qlik Sense, Plotly, SAS, Knime, RStudio, Shiny, Jupyter Lab | Notebook...")
    
    with st.expander(tr("### Machine Learning & Deep Learning", "### Machine Learning & Deep Learning")):
        st.write("Regression, Classification, KNN, K-means, Random Forest, Isolation Forest, PCA, Ensemble, Yellowbrick, Scikit-learn, Scikit-image, Pillow, NLTK, Neattext, TextHero, Lazypredic, NLP, Computer Vision, ANN, CNN, RNN, LSTM, LLM, AI Agent, OpenCV, Transformers, Fine-tuning...")
    
    with st.expander(tr("### Gestion de projets & Outils informatiques", "### Project Management & IT Tools")):
        st.write("Agile, Jira, Slack, Trello, Microsoft Project, Pack Office, Git, Github, AnyDesk, TeamViewerQS, Canva, Windows, Linux, MacOS...")

# ------------------------------- Section Expériences -------------------------------
elif menu == tr("Expériences", "Experiences"):
    st.subheader(tr("Expériences Professionnelles", "Professional Experiences"))
    with st.expander(tr("### Data Scientist · Riviera Réalisation (Promo+) · Mars 2024 - Mars 2026 · Nice, France", 
                        "Data Scientist · Riviera Réalisation (Promo+) · Mar 2024 - Mar 2026 · Nice, France")):
        st.markdown(tr("""  
        **Mission :**  
        - Assistance dans la mise en œuvre d'outils d'IA tels que la reconnaissance d'images  
        - Réalisation de statistiques sur les données  
        - Mise en place d'un chatbot basé sur l'IA  

        **Activités principales :**  
        - Collecte, nettoyage et analyse de jeux de données provenant de diverses sources en vue de leur exploitation
        - Développement et mise en œuvre de modèles prédictifs afin d’optimiser les processus de promotion immobilière, notamment la prévision de la demande, l’évaluation des prix et la segmentation de la clientèle
        - Collaboration étroite avec les équipes de développement pour intégrer les modèles dans les logiciels et assurer leur déploiement efficace 
        - Veille technologique régulière afin de rester à la pointe des avancées en apprentissage automatique et en analyse de données 
        """,  

        """  
        **Mission:**  
        - Assistance in implementing AI tools such as image recognition  
        - Conducting statistics on data  
        - Implementation of an AI Chatbot  

        **Main Activities:**  
        - Collecting, cleaning, and analyzing data sets from various sources for analysis  
        - Developing and implementing predictive models to optimize real estate promotion processes,  
          including demand forecasting, price evaluation, and customer segmentation 
        - Working closely with development teams to integrate models into software and ensure their efficient deployment 
        - Conducting regular technological monitoring to stay at the forefront of advances in machine learning and data analysis  
        """))

    with st.expander(tr("### Consultant Data Manager · ACDEC · Avril 2022 - Août 2023 · Brazzaville, Congo", 
                        "Data Manager consultant. · ACDEC · Apr 2022 - Aug 2023 · Brazzaville, Congo")):
        st.markdown(tr("""  
        **Tâches effectuées :**  
        
        - Préparer la pré-liste
        -  Examiner et piloter les questionnaires
        - Recenser les répondants
        - Assurer le suivi, le nettoyage des données et assister dans l’analyse préliminaire des données
        - Contribuer à l'élaboration des rapports de projet
        - Superviser la synchronisation des données réalisée par les enquêteurs
        - Soumettre des rapports réguliers à la division (RSU)
        """,  

        """  
        **Tasks performed:**  
        
        - Prepare the pre-list
        - Review and pilot questionnaires
        - List respondents
        - Monitor, clean data, and assist in the preliminary analysis of the data
        - Support the development of project reports
        - Supervise the synchronization of data carried out by the investigators
        - Submit regular reports to the division (RSU)
        """))

    with st.expander(tr("### Enseignant · ESGAE · Octobre 2021 - Juin 2023 · Brazzaville, Congo", 
                        "Teacher · ESGAE · Oct 2021 - Jun 2023 · Brazzaville, Congo")):
        st.markdown(tr("""  
        **Enseignant en :**  
        
        - Data Science avec Python
        - Administration MongoDB
        - Fondamentaux Oracle
        - Microsoft Power BI
        - Administration Oracle
        - Algorithmes et structures de données sous le langage C
        - CMS (WordPress)
        - Web service
        - Fondamentaux JavaScript
        - Développement web (HTML, CSS, Bootstrap et PHP)
        """,  

        """  
        **Instructor in:**  

        - Data Science with Python
        - MongoDB Administration
        - Oracle fundamentals
        - Microsoft Power BI
        - Oracle Administration
        - Algorithm and Data Structure
        - CMS (WordPress)
        - Web service
        - Fundamentals of JavaScript
        - Web Development (HTML, CSS, Bootstrap, and PHP)
        """))

    with st.expander(tr("### Consultant informaticien · Grinso & Associés · Février 2022 · Pointe-Noire, Congo", 
                        "IT Consultant · Grinso & Associés · Feb 2022 · Pointe-Noire, Congo")):
        st.markdown(tr("""  
        **Tâches effectuées :**  
        
        - Présenté les services offerts par le cabinet 'Grinso & Associés' en présence du Premier Ministre, Chef du Gouvernement, ainsi que d'autres membres du Gouvernement, lors de la 3e édition du Forum Numérique Congo :
            - Service de conseil
            - Service d'études
        """,  

        """  
        **Tasks performed:**  

        - Presented the services offered by the firm 'Grinso & Associés' in the presence of the Prime Minister, Head of Government, and other government members, at the 3rd edition of the Digital Forum Congo:
            - Advisory Service
            - Study Service
        """))

    with st.expander(tr("### Data Analyst · ACSI · Juin 2021 - Octobre 2021 · Brazzaville, Congo", 
                        "Data Analyst  · ACSI · Jun 2021 - Oct 2021 · Brazzaville, Congo")):
        st.markdown(tr("""  
        **Tâches effectuées :**  
        
        - Collecte et traitement des données manquantes
        - Création du jeu de données
        - Analyse exploratoire des données
        - Modélisation (régression linéaire multiple)
        - Analyse des besoins en indicateurs
        - Création d'indicateurs à l'aide de Microsoft Power BI
        - Cartographie des données
        - Développement et amélioration des tableaux de bord
        - Maintenance corrective et évolutive des tableaux de bord
        """,  

        """  
        **Tasks performed:**  

        - Collection and processing of missing data
        - Creation of the dataset
        - Exploratory data analysis
        - Modeling (multiple linear regression)
        - Analysis of indicator requirements
        - Creation of indicators using Microsoft Power BI
        - Data mapping
        - Development and improvement of dashboards
        - Corrective and evolutionary maintenance of dashboards.
        """))

    with st.expander(tr("### Data Scientist · Freelance · Décembre 2020 - Mai 2021 · Libreville, Gabon", 
                        "Data Scientist  · Freelance · Dec 2020 - May 2021 · Libreville, Gabon")):
        st.markdown(tr("""  
        **Tâches effectuées :**  
        
        - Préparation des données (chargement, évaluation et nettoyage des données)
        - Analyse exploratoire des données
        - Prétraitement des données
        - Développement et mise en œuvre d'un système d'aide à la décision basé sur l'intelligence artificielle pour les patients atteints du SARS-CoV-2 (COVID-19)
        """,  

        """  
        **Tasks performed:**  

        - Data preparation (Loading, assessing, and cleaning data)
        - Exploratory Data Analysis
        - Data preprocessing
        - Development and implementation of an artificial intelligence-based decision support system for -patients with SARS-CoV-2 (COVID-19)
        """))

    with st.expander(tr("### Ingénieur logiciel · ACSI · Août 2019 - Décembre 2019 · Brazzaville, Congo", 
                        "Software Engineer  · ACSI · Aug 2019 - Dec 2019 · Libreville, Congo")):
        st.markdown(tr("""  
        **Tâches effectuées :**  
        
        - Gérer efficacement les réunions afin d’éviter les conflits d’horaire (alerte en cas de réunions programmées simultanément, réunions se chevauchant avec les mêmes participants, notification des participants à une réunion)
        - Suivre l’avancement des activités liées à un contrat de service, vérifier le respect des délais impartis aux tâches, etc
        """,  

        """  
        **Tasks performed:**  

        - Efficiently manage meetings to avoid collisions (warning of meetings scheduled at the same time, meetings scheduled at the same time with participants, alerting participants to a meeting)
        - Monitor the progress of activities related to a service contract, verify the adherence to the task duration, etc
        """))

# ------------------------------- Section Formations -------------------------------
elif menu == tr("Formations", "Educations"):
    st.subheader(tr("Formations", "Educations"))
    with st.expander(tr("### Master appliqué en Data Science & Intelligence Artificielle, Expert en Science des Données", "Applied MSc in Data Science & Artificial Intelligence, Data Science Expert")):
        st.write(tr("**Data ScienceTech Institute (DSTI), Paris & Nice, France**", "**Data ScienceTech Institute (DSTI), Paris & Nice, France**"))

    with st.expander(tr("### Diplôme d'Ingénieur des Travaux Informatiques", "Computer Engineering ")):
        st.write(tr("**Institut Africain d'Informatique (IAI), Libreville, Gabon**", "**Institut Africain d'Informatique (IAI), Libreville, Gabon**"))

    with st.expander(tr("### Diplôme de Programmeur", "Programmer Diploma")):
        st.write(tr("**Institut Africain d'Informatique (IAI), Libreville, Gabon**", "**Institut Africain d'Informatique (IAI), Libreville, Gabon**"))

elif menu == tr("Certifications", "Certifications"):
    st.subheader(tr("Certifications", "Certifications"))
    with st.expander(tr("### Professionnel certifié Neo4j · Neo4j", "Neo4j Certified Professional - Neo4j")):
        st.write(tr("👉[Voir certification](https://graphacademy.neo4j.com/c/97fba52a-329d-4ba9-bcba-504d3f6f5bbb/)", "👉[View certification](https://graphacademy.neo4j.com/c/97fba52a-329d-4ba9-bcba-504d3f6f5bbb/)"))

    with st.expander(tr("### Certificat professionnel en Data Science · IBM", "IBM Data Science Professional Certificate")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/professional-cert/ARFJ6B6Z47V7)", "👉[View certification](https://www.coursera.org/account/accomplishments/professional-cert/ARFJ6B6Z47V7)"))

    with st.expander(tr("### Certificat professionnel de Développeur en IA · IBM", "IBM AI Developer Professional Certificate")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/professional-cert/4J7FMP9CLR2A)", "👉[View certification](https://www.coursera.org/account/accomplishments/professional-cert/4J7FMP9CLR2A)"))

    with st.expander(tr("### Certificat professionnel en Ingénierie de l'IA · IBM", "IBM AI Engineering Professional Certificate")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/professional-cert/S36JVGFEBHX4)", "👉[View certification](https://www.coursera.org/account/accomplishments/professional-cert/S36JVGFEBHX4)"))

    with st.expander(tr("### Certificat professionnel en Data Analyst · IBM", "IBM Data Analyst Professional Certificate")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/professional-cert/ZX2NN9RXKQNH)", "👉[View certification](https://www.coursera.org/account/accomplishments/professional-cert/ZX2NN9RXKQNH)"))
    
    with st.expander(tr("### Certificat professionnel en Data Analytics · Google", "Google Data Analytics Professional Certificate")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/professional-cert/Y2DZ95X9JZSH)", "👉[View certification](https://www.coursera.org/account/accomplishments/professional-cert/Y2DZ95X9JZSH)"))

    with st.expander(tr("### Certificat de spécialisation en Machine Learning · Université de Washington", "Machine Learning Specialization Certificate")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/specialization/Q4KCPC6RNQ42)", "👉[View certification](https://www.coursera.org/account/accomplishments/specialization/Q4KCPC6RNQ42)"))

    with st.expander(tr("### Certificat de spécialisation en Deep Learning · DeepLearning.AI", "Deep Learning Specialization Certificate · DeepLearning.AI")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/specialization/QT59H62LYMS3)", "👉[View certification](https://www.coursera.org/account/accomplishments/specialization/QT59H62LYMS3)"))

    with st.expander(tr("### Certificat de spécialisation en Big Data · Université de Californie à San Diego", "Big Data Specialization Certificate · University of California San Diego")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/specialization/8GKXXC9VAB5A)", "👉[View certification](https://www.coursera.org/account/accomplishments/specialization/8GKXXC9VAB5A)"))

    with st.expander(tr("### Certificat de spécialisation en Systèmes d'Information · Université du Minnesota", "Information​ ​Systems Specialization Certificate · University of Minnesota")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/specialization/NERYFJYZYPVX)", "👉[View certification](https://www.coursera.org/account/accomplishments/specialization/NERYFJYZYPVX)"))

    with st.expander(tr("### Certificat de spécialisation en Développement du leadership pour les ingénieurs · Université de Rice", "Leadership Development for Engineers Specialization Certificate · Rice University")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/specialization/MTGAQ7ZX844L)", "👉[View certification](https://www.coursera.org/account/accomplishments/specialization/MTGAQ7ZX844L)"))

    with st.expander(tr("### Certificat de spécialisation en gestion de produits logiciels · Université de l'Alberta", "Software Product Management Specialization Certificate · University of Alberta")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/specialization/X78VYKX2GW49)", "👉[View certification](https://www.coursera.org/account/accomplishments/specialization/X78VYKX2GW49)"))

    with st.expander(tr("### Certificat de spécialisation en Conception de logiciels sécurisés · Système de l'Université du Colorado", "Secure Software Design Specialization Certificate · University of Colorado System")):
        st.write(tr("👉[Voir certification](https://www.coursera.org/account/accomplishments/specialization/Z9G2X6B9492D)", "👉[View certification](https://www.coursera.org/account/accomplishments/specialization/Z9G2X6B9492D)"))

# ------------------------------- Section Projets -------------------------------
elif menu == tr("Projets", "Projects"):
    st.subheader(tr("Projets GitHub", "GitHub Projects"))
    with st.expander(tr("Retrouvez mes projets en cliquant sur le lien ci-dessous", "Find my projects by clicking on the link below)")):
        st.write(tr("**👉[GitHub](https://github.com/Rostaing)**", "**👉[GitHub](https://github.com/Rostaing)**"))

# ------------------------------- Section Distinctions & récompenses ------------------------------- 
elif menu == tr("Distinctions & Récompenses", "Honors & Awards"):
    st.subheader(tr("Distinctions & Récompenses", "Honors & Awards"))
    with st.expander(tr("### Défi d'applications spatiales de la NASA · Délivré par GALACTIC TEAM MEMBER · Oct 2018", "### NASA SPACE APPS CHALLENGE · Issued by GALACTIC TEAM MEMBER · Oct 2018")):
        st.write(tr("**International Space Apps Challenge. En reconnaissance spéciale pour les efforts visant à relever les défis sur Terre et dans l'espace.**", "**International Space Apps Challenge. In special appreciation for efforts to address challenges on Earth and in Space.**"))
    with st.expander(tr("### Portefeuille de badges · Badges Credly", "### Badge Wallet · Credly Badges")):
        st.write(tr("**👉[Voir badges](https://www.credly.com/users/diavilarostaingengandzi)**", "**👉[View badges](https://www.credly.com/users/diavilarostaingengandzi)**"))

# ------------------------------- Section Langues ------------------------------- 
elif menu == tr("Langues", "Languages"):
    st.subheader(tr("Langues", "Languages"))
    with st.expander(tr("### Français", "### French")):
        st.write(tr("**Langue maternelle**", "**Native language**"))
    with st.expander(tr("### Anglais", "### English")):
        st.write(tr("**Courant**", "**Fluent**"))

# ------------------------------- Section Organisation ------------------------------- 
elif menu == tr("Organisations", "Organizations"):
    st.subheader(tr("Organisations", "Organizations"))
    with st.expander(tr("### Data ScienceTech Institute (DSTI) Alumni · Membre · Oct 2024 - à ce jour", "### Data ScienceTech Institute (DSTI) Alumni · Member · Oct 2024 - Present")):
        st.write(tr("**👉[Voir profil](https://alumni.dsti.institute/fr/person/diavila-rostaing/836)**", "**👉[View profile](https://alumni.dsti.institute/fr/person/diavila-rostaing/836)**"))


# ------------------------------- Section Centres d'intérêt -------------------------------
elif menu == tr("Centres d'intérêt", "Hobbies"):
    st.subheader(tr("Centres d'intérêt", "Hobbies"))
    with st.expander(tr("### Recherche", "### Research")):
        st.write(tr("**Science de données, Analyse de donnée, Ingénieurie de données, Big Data, Machine Learning, Deep Learning, Traitement du Langage Naturel, IA générative, LLM, RAG, CAG, Agent IA, IAG...**", "**Data Science, Data Analytics, Data Engineering, Big Data, Machine Learning, Deep Learning, Natural Language Processing,Generative AI, LLM, RAG, CAG, Agent AI, AGI...**"))
    with st.expander(tr("### Sport", "### Sport")):
        st.write(tr("**Course à pied, Gym, Football, Basket, Golf**", "**Running, Gym, Football, Basket, Golf**"))
    with st.expander(tr("### Musique", "### Music")):
        st.write(tr("**Gospel...**", "**Gospel...**"))
    with st.expander(tr("### Voyage", "### Journey")):
        st.write(tr("**Congo-Brazzaville, Gabon, France...**", "**Republic of the Congo, Gabon, France...**"))

date = datetime.date.today().year

st.sidebar.markdown("---")
st.sidebar.write(tr(f"© {date} Davila Rostaing - Digital CV", f"© {date} Diavila Rostaing - Digital CV"))