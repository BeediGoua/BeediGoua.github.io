"""Bilingual case-study page payloads used by build_site.py."""

SITE = "https://beedigoua.github.io"


def pages():
    return [
        square(),
        credit(),
        brokerflow(),
        retail(),
        finzuu(),
        ville(),
        survie(),
        reviewguardian(),
        music(),
        zimnat(),
        autres(),
    ]


def _base(slug, fr_file, en_file=None):
    en_file = en_file or fr_file.replace(".html", "-en.html")
    return {
        "slug": slug,
        "out_fr": f"projects/{fr_file}",
        "out_en": f"projects/{en_file}",
        "canonical_fr": f"{SITE}/projects/{fr_file}",
        "canonical_en": f"{SITE}/projects/{en_file}",
    }


def square():
    b = _base("square-management", "square-management.html")
    b["fr"] = {
        "title": "Square Research Center - Évaluation de systèmes RAG",
        "description": "Étude de cas : protocole d’évaluation de 189 configurations RAG sur documents longs.",
        "kicker": "Étude de cas · 2025",
        "heading": "Évaluation de systèmes RAG sur documents longs",
        "subtitle": "Chez Square Management, j’ai conçu un protocole pour comparer des pipelines RAG et comprendre où les réponses se trompent.",
        "meta": [
            {"label": "Organisation", "value": "Square Management"},
            {"label": "Rôle", "value": "Stage AI & Data Science"},
            {"label": "Année", "value": "2025"},
            {"label": "Périmètre", "value": "189 configurations"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Question",
                "body": "<p>Comment les choix d’OCR, de découpage, de retrieval et de ranking influencent-ils la qualité des réponses sur documents longs&nbsp;?</p>",
            },
            {
                "title": "Approche",
                "body": "<ul><li>Plan expérimental commun pour comparer les configurations.</li><li>Séparation retrieval / ranking / génération dans l’analyse d’erreurs.</li><li>Métriques automatiques, signaux type RAGAS et revue manuelle des cas limites.</li><li>Brique de recherche vectorielle (ChromaDB) et exposition via FastAPI / Docker.</li></ul>",
            },
            {
                "title": "Résultats publiables",
                "body": "<ul><li>189 configurations comparées.</li><li>Cadre d’évaluation réutilisable.</li><li>Typologie d’échecs : récupération, classement, génération.</li></ul><p>Les documents, questions et scores détaillés restent internes.</p>",
            },
        ],
        "limitations": "<ul><li>Données et livrables clients non publics.</li><li>Pas de chiffres de production externes publiés ici.</li></ul>",
        "back": "../index.html#projects",
    }
    b["en"] = {
        "title": "Square Research Center - RAG system evaluation",
        "description": "Case study: evaluation protocol across 189 RAG configurations on long documents.",
        "kicker": "Case study · 2025",
        "heading": "Evaluating RAG systems on long documents",
        "subtitle": "At Square Management, I designed a protocol to compare RAG pipelines and understand where answers fail.",
        "meta": [
            {"label": "Organization", "value": "Square Management"},
            {"label": "Role", "value": "AI & Data Science intern"},
            {"label": "Year", "value": "2025"},
            {"label": "Scope", "value": "189 configurations"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Question",
                "body": "<p>How do OCR, chunking, retrieval and ranking choices affect answer quality on long documents?</p>",
            },
            {
                "title": "Approach",
                "body": "<ul><li>Shared experimental plan across configurations.</li><li>Error analysis split across retrieval, ranking and generation.</li><li>Automated metrics, RAGAS-style signals and manual review of edge cases.</li><li>Vector search component (ChromaDB) exposed with FastAPI / Docker.</li></ul>",
            },
            {
                "title": "Publishable outcomes",
                "body": "<ul><li>189 configurations compared.</li><li>Reusable evaluation framework.</li><li>Failure taxonomy: retrieval, ranking, generation.</li></ul><p>Source documents, questions and detailed scores remain internal.</p>",
            },
        ],
        "limitations": "<ul><li>Client data and deliverables are not public.</li><li>No external production metrics are published here.</li></ul>",
        "back": "../index-en.html#projects",
    }
    return b


def credit():
    b = _base("credit-scoring", "credit-scoring.html")
    b["fr"] = {
        "title": "Credit Scoring - Modélisation du risque de défaut",
        "description": "Cas académique de scoring crédit : logistique vs RF/XGBoost, grille de risque, limites.",
        "kicker": "Projet académique · ENSAI",
        "heading": "Credit scoring — performance et interprétabilité",
        "subtitle": "Construire un score de défaut à 12 mois lisible, puis le comparer à des modèles plus complexes.",
        "meta": [
            {"label": "Type", "value": "Cas académique"},
            {"label": "Données", "value": "532 567 comptes (initial)"},
            {"label": "Cible", "value": "Défaut 12 mois"},
            {"label": "Split", "value": "70/30 stratifié"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Données",
                "body": "<ul><li>532 567 comptes professionnels déclarés en entrée.</li><li>143 variables initiales, taux de défaut 12,76&nbsp;%.</li><li>Après traitement : 372 381 train + 159 845 test = 532 226.</li><li>Écart de 341 observations non expliqué ici (rapport source requis).</li></ul>",
            },
            {
                "title": "Modélisation",
                "body": "<p>Régression logistique retenue (9 variables). Challengers : Random Forest et XGBoost.</p><table><tr><th>Modèle</th><th>AUC test</th><th>Gini</th></tr><tr><td>Logistique</td><td>0,784</td><td>0,57</td></tr><tr><td>Random Forest</td><td>0,800</td><td>0,60</td></tr><tr><td>XGBoost</td><td>0,798</td><td>0,59</td></tr></table><p>Le gain des ensembles reste limité face à la perte d’interprétabilité.</p>",
            },
            {
                "title": "Grille de score",
                "body": "<p>Score 0–1000 et sept classes de risque (CHR1–CHR7) pour une lecture métier.</p>",
            },
        ],
        "limitations": "<ul><li>Pas de courbe de calibration ni Brier documentés — la calibration n’est pas affirmée.</li><li>Pas de validation en production.</li><li>Données confidentielles non publiables.</li></ul>",
        "back": "../index.html#projects",
    }
    b["en"] = {
        "title": "Credit Scoring - Default risk modelling",
        "description": "Academic credit scoring case: logistic vs RF/XGBoost, risk grid, limitations.",
        "kicker": "Academic project · ENSAI",
        "heading": "Credit scoring — performance and interpretability",
        "subtitle": "Build a readable 12-month default score, then compare it with more complex models.",
        "meta": [
            {"label": "Type", "value": "Academic case"},
            {"label": "Data", "value": "532,567 accounts (initial)"},
            {"label": "Target", "value": "12-month default"},
            {"label": "Split", "value": "70/30 stratified"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Data",
                "body": "<ul><li>532,567 professional accounts declared initially.</li><li>143 initial variables, 12.76% default rate.</li><li>After processing: 372,381 train + 159,845 test = 532,226.</li><li>Gap of 341 observations unexplained here (source report required).</li></ul>",
            },
            {
                "title": "Modelling",
                "body": "<p>Logistic regression retained (9 variables). Challengers: Random Forest and XGBoost.</p><table><tr><th>Model</th><th>Test AUC</th><th>Gini</th></tr><tr><td>Logistic</td><td>0.784</td><td>0.57</td></tr><tr><td>Random Forest</td><td>0.800</td><td>0.60</td></tr><tr><td>XGBoost</td><td>0.798</td><td>0.59</td></tr></table><p>Ensemble gains remain limited versus interpretability loss.</p>",
            },
            {
                "title": "Score grid",
                "body": "<p>0–1000 score and seven risk classes (CHR1–CHR7) for business reading.</p>",
            },
        ],
        "limitations": "<ul><li>No documented calibration curve or Brier score — calibration is not claimed.</li><li>No production validation.</li><li>Confidential data not publishable.</li></ul>",
        "back": "../index-en.html#projects",
    }
    return b


def brokerflow():
    b = _base("brokerflow", "brokerflow.html")
    b["fr"] = {
        "title": "BrokerFlow AI - Décision crédit explicable",
        "description": "Prototype de décision crédit combinant modèle, règles et fallback, évalué sur 50 cas.",
        "kicker": "Prototype · ML systems",
        "heading": "BrokerFlow AI — décision contrôlée",
        "subtitle": "Garder une décision explicable quand un modèle, des règles et des composants agentiques cohabitent.",
        "meta": [
            {"label": "Type", "value": "Prototype"},
            {"label": "Benchmark", "value": "50 cas annotés"},
            {"label": "AUC", "value": "0,728"},
            {"label": "Tests", "value": "44"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Architecture",
                "body": "<ul><li>Modèle de scoring et règles déterministes séparés.</li><li>Fallback et reason codes.</li><li>Agents limités, pas un système autonome non contrôlé.</li></ul>",
            },
            {
                "title": "Évaluation",
                "body": "<p>Sur 50 cas annotés : AUC 0,728, Brier 0,150, seuil 0,231 (valeurs déclarées dans la source de vérité portfolio). Petit échantillon : utile pour le prototype, pas pour généraliser.</p>",
            },
        ],
        "limitations": "<ul><li>Benchmark réduit.</li><li>Pas de validation externe de production.</li><li>Distinguer perf du modèle et comportement du système complet.</li></ul>",
        "back": "../index.html#projects",
    }
    b["en"] = {
        "title": "BrokerFlow AI - Explainable credit decisions",
        "description": "Credit-decision prototype combining model, rules and fallback, evaluated on 50 cases.",
        "kicker": "Prototype · ML systems",
        "heading": "BrokerFlow AI — controlled decisions",
        "subtitle": "Keep decisions explainable when a model, rules and limited agentic parts coexist.",
        "meta": [
            {"label": "Type", "value": "Prototype"},
            {"label": "Benchmark", "value": "50 annotated cases"},
            {"label": "AUC", "value": "0.728"},
            {"label": "Tests", "value": "44"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Architecture",
                "body": "<ul><li>Scoring model and deterministic rules kept separate.</li><li>Fallback and reason codes.</li><li>Constrained agents, not an uncontrolled autonomous system.</li></ul>",
            },
            {
                "title": "Evaluation",
                "body": "<p>On 50 annotated cases: AUC 0.728, Brier 0.150, threshold 0.231 (values declared in the portfolio source of truth). Small sample: useful for a prototype, not for generalisation.</p>",
            },
        ],
        "limitations": "<ul><li>Small benchmark.</li><li>No external production validation.</li><li>Separate model score from full-system behaviour.</li></ul>",
        "back": "../index-en.html#projects",
    }
    return b


def retail():
    b = _base("retail-demand-forecasting", "retail-demand-forecasting.html")
    b["fr"] = {
        "title": "Retail Demand Forecasting - Prévision et stock",
        "description": "Prévision probabiliste Favorita, segmentation ADI/CV² et décision Newsvendor.",
        "kicker": "Projet time series",
        "heading": "Prévision de demande et décision de stock",
        "subtitle": "Passer d’une prévision ponctuelle à une décision de commande sous incertitude.",
        "meta": [
            {"label": "Données", "value": "Favorita"},
            {"label": "Horizon", "value": "8 semaines"},
            {"label": "Segmentation", "value": "ADI / CV²"},
            {"label": "Décision", "value": "Newsvendor"},
        ],
        "links": [
            {
                "href": "https://github.com/BeediGoua/retail-demand-forecasting-assistant",
                "label": "GitHub",
                "external": True,
            }
        ],
        "sections": [
            {
                "title": "Pipeline",
                "body": "<ul><li>ETL hebdomadaire, grille temporelle, Parquet / SQLite.</li><li>Segmentation Smooth / Erratic / Intermittent / Lumpy.</li><li>Quantiles P10 / P50 / P90 puis Newsvendor.</li></ul>",
            },
            {
                "title": "Évaluation",
                "body": "<p>Backtesting temporel et baselines naïves. Un WAPE préliminaire n’est <strong>pas</strong> mis en avant tant que le protocole n’est pas consolidé.</p>",
            },
        ],
        "limitations": "<ul><li>Coûts économiques simulés.</li><li>WAPE peu informatif sur faibles volumes.</li><li>Besoin d’un backtesting plus large.</li></ul>",
        "back": "../index.html#projects",
    }
    b["en"] = {
        "title": "Retail Demand Forecasting - Forecast and inventory",
        "description": "Probabilistic Favorita forecasting, ADI/CV² segmentation and Newsvendor decisions.",
        "kicker": "Time-series project",
        "heading": "Demand forecasting and inventory decisions",
        "subtitle": "Move from a point forecast to an order decision under uncertainty.",
        "meta": [
            {"label": "Data", "value": "Favorita"},
            {"label": "Horizon", "value": "8 weeks"},
            {"label": "Segmentation", "value": "ADI / CV²"},
            {"label": "Decision", "value": "Newsvendor"},
        ],
        "links": [
            {
                "href": "https://github.com/BeediGoua/retail-demand-forecasting-assistant",
                "label": "GitHub",
                "external": True,
            }
        ],
        "sections": [
            {
                "title": "Pipeline",
                "body": "<ul><li>Weekly ETL, time grid, Parquet / SQLite.</li><li>Smooth / Erratic / Intermittent / Lumpy segmentation.</li><li>P10 / P50 / P90 quantiles then Newsvendor.</li></ul>",
            },
            {
                "title": "Evaluation",
                "body": "<p>Temporal backtesting and naive baselines. A preliminary WAPE is <strong>not</strong> highlighted until the protocol is consolidated.</p>",
            },
        ],
        "limitations": "<ul><li>Simulated economic costs.</li><li>WAPE weak on low volumes.</li><li>Broader backtesting still needed.</li></ul>",
        "back": "../index-en.html#projects",
    }
    return b


def finzuu():
    b = _base("finzuu", "finzuu.html")
    b["fr"] = {
        "title": "FINZUU - Scoring agricole explicable",
        "description": "Cadre explicable d’analyse du risque agricole et de la capacité de remboursement.",
        "kicker": "Expérience · 2026",
        "heading": "FINZUU — scoring agricole explicable",
        "subtitle": "Estimer un risque agricole et une capacité de remboursement avec des contrôles humains et des indicateurs lisibles.",
        "meta": [
            {"label": "Rôle", "value": "Data Scientist"},
            {"label": "Année", "value": "2026"},
            {"label": "Stack", "value": "FastAPI · PostgreSQL/PostGIS"},
            {"label": "Statut", "value": "Prototype métier"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Travail réalisé",
                "body": "<ul><li>Cadre d’analyse risques / revenus / marge / remboursement.</li><li>Contrôles de cohérence, alertes, reason codes.</li><li>API FastAPI et base PostgreSQL/PostGIS.</li></ul>",
            }
        ],
        "limitations": "<ul><li>Ne pas présenter comme modèle de défaut certifié en production.</li><li>Détails clients et données internes non publiés.</li></ul>",
        "back": "../index.html#experience",
    }
    b["en"] = {
        "title": "FINZUU - Explainable agricultural scoring",
        "description": "Explainable framework for agricultural risk and repayment capacity analysis.",
        "kicker": "Experience · 2026",
        "heading": "FINZUU — explainable agricultural scoring",
        "subtitle": "Estimate agricultural risk and repayment capacity with human checks and readable indicators.",
        "meta": [
            {"label": "Role", "value": "Data Scientist"},
            {"label": "Year", "value": "2026"},
            {"label": "Stack", "value": "FastAPI · PostgreSQL/PostGIS"},
            {"label": "Status", "value": "Business prototype"},
        ],
        "links": [],
        "sections": [
            {
                "title": "What I worked on",
                "body": "<ul><li>Risk / revenue / margin / repayment analysis frame.</li><li>Consistency checks, alerts, reason codes.</li><li>FastAPI service and PostgreSQL/PostGIS store.</li></ul>",
            }
        ],
        "limitations": "<ul><li>Not presented as a production-certified default model.</li><li>Client details and internal data are not published.</li></ul>",
        "back": "../index-en.html#experience",
    }
    return b


def ville():
    b = _base("ville-de-paris", "ville-de-paris.html")
    b["fr"] = {
        "title": "Ville de Paris - Données de mobilité",
        "description": "Pipeline multi-sources LAPI/SIV/SIREN et indicateurs pour la mobilité.",
        "kicker": "Stage · 2024",
        "heading": "Ville de Paris — mobilité et données multi-sources",
        "subtitle": "Rapprocher des sources hétérogènes pour produire des indicateurs utiles aux équipes.",
        "meta": [
            {"label": "Organisation", "value": "Agence de la Mobilité"},
            {"label": "Année", "value": "2024"},
            {"label": "Sources", "value": "LAPI · SIV · SIREN"},
            {"label": "Restitution", "value": "Digdash"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Travail réalisé",
                "body": "<ul><li>Nettoyage, contrôles qualité, jointures d’entités.</li><li>Indicateurs et segmentations.</li><li>Tableaux de bord Digdash.</li></ul><p>Le schéma de pipeline présenté publiquement reste conceptuel.</p>",
            }
        ],
        "limitations": "<ul><li>Aucune donnée personnelle ou opérationnelle confidentielle n’est publiée.</li><li>Pas de chiffres internes sans autorisation.</li></ul>",
        "back": "../index.html#experience",
    }
    b["en"] = {
        "title": "City of Paris - Mobility data",
        "description": "Multi-source LAPI/SIV/SIREN pipeline and mobility indicators.",
        "kicker": "Internship · 2024",
        "heading": "City of Paris — mobility and multi-source data",
        "subtitle": "Reconcile heterogeneous sources to produce indicators useful to operational teams.",
        "meta": [
            {"label": "Organization", "value": "Mobility Agency"},
            {"label": "Year", "value": "2024"},
            {"label": "Sources", "value": "LAPI · SIV · SIREN"},
            {"label": "Delivery", "value": "Digdash"},
        ],
        "links": [],
        "sections": [
            {
                "title": "What I worked on",
                "body": "<ul><li>Cleaning, quality checks, entity joins.</li><li>Indicators and segmentation.</li><li>Digdash dashboards.</li></ul><p>Any public pipeline diagram remains conceptual.</p>",
            }
        ],
        "limitations": "<ul><li>No confidential personal or operational data is published.</li><li>No internal figures without authorization.</li></ul>",
        "back": "../index-en.html#experience",
    }
    return b


def survie():
    b = _base("analyse-survie", "analyse-survie.html")
    b["fr"] = {
        "title": "Analyse de survie - HEGP",
        "description": "Analyse de survie post-Covid : censure, Kaplan-Meier / Cox, sans résultats médicaux publics.",
        "kicker": "Projet académique / hospitalier",
        "heading": "Analyse de survie post-Covid",
        "subtitle": "Étudier un temps jusqu’à événement en tenant compte de la censure, sans exposer de résultats cliniques non autorisés.",
        "meta": [
            {"label": "Contexte", "value": "HEGP"},
            {"label": "Méthodes", "value": "Kaplan-Meier · Cox"},
            {"label": "Publication", "value": "Méthode seule"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Méthode",
                "body": "<ul><li>Définition événement / censure.</li><li>Courbes de survie et modèle de Cox si utilisés dans le travail.</li><li>Lecture prudente des hypothèses.</li></ul>",
            }
        ],
        "limitations": "<ul><li>Aucun résultat médical chiffré public sans rapport et autorisation.</li></ul>",
        "back": "../index.html#projects",
    }
    b["en"] = {
        "title": "Survival analysis - HEGP",
        "description": "Post-Covid survival analysis: censoring, Kaplan-Meier / Cox, no public clinical results.",
        "kicker": "Academic / hospital project",
        "heading": "Post-Covid survival analysis",
        "subtitle": "Study time-to-event with censoring, without exposing unauthorized clinical results.",
        "meta": [
            {"label": "Context", "value": "HEGP"},
            {"label": "Methods", "value": "Kaplan-Meier · Cox"},
            {"label": "Publication", "value": "Methods only"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Method",
                "body": "<ul><li>Event / censoring definition.</li><li>Survival curves and Cox model when actually used.</li><li>Careful reading of assumptions.</li></ul>",
            }
        ],
        "limitations": "<ul><li>No public clinical numeric results without a report and authorization.</li></ul>",
        "back": "../index-en.html#projects",
    }
    return b


def reviewguardian():
    b = _base("reviewguardian", "reviewguardian.html")
    b["fr"] = {
        "title": "ReviewGuardian - Modération d’avis",
        "description": "Modération locale et explicable de la toxicité des avis clients.",
        "kicker": "NLP · classification",
        "heading": "ReviewGuardian — modération explicable",
        "subtitle": "Détecter des contenus toxiques localement, avec des explications LIME/SHAP.",
        "meta": [
            {"label": "Corpus", "value": "7 296 avis (dépôt)"},
            {"label": "Approche", "value": "TF-IDF · classifieurs"},
            {"label": "Expliquabilité", "value": "LIME · SHAP"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Solution",
                "body": "<ul><li>Pipeline d’entraînement et prédiction unitaire / lot.</li><li>API FastAPI, démo Streamlit, Docker.</li><li>Architecture locale pour limiter l’exposition des données.</li></ul>",
            }
        ],
        "limitations": "<ul><li>Performances à lire dans le contexte du corpus.</li><li>Pas de claim de détection de bots / fraude (ancien EN retiré).</li></ul>",
        "back": "../projects/autres-projets.html",
    }
    b["en"] = {
        "title": "ReviewGuardian - Review moderation",
        "description": "Local, explainable toxicity moderation for customer reviews.",
        "kicker": "NLP · classification",
        "heading": "ReviewGuardian — explainable moderation",
        "subtitle": "Detect toxic content locally, with LIME/SHAP explanations.",
        "meta": [
            {"label": "Corpus", "value": "7,296 reviews (repo)"},
            {"label": "Approach", "value": "TF-IDF · classifiers"},
            {"label": "Explainability", "value": "LIME · SHAP"},
        ],
        "links": [],
        "sections": [
            {
                "title": "Solution",
                "body": "<ul><li>Training pipeline with single-item and batch prediction.</li><li>FastAPI, Streamlit demo, Docker.</li><li>Local architecture to limit data exposure.</li></ul>",
            }
        ],
        "limitations": "<ul><li>Performance must be read in corpus context.</li><li>No bot/fraud-detection claim (old EN narrative removed).</li></ul>",
        "back": "../projects/autres-projets-en.html",
    }
    return b


def music():
    b = _base("music-recommender", "music-recommender.html")
    b["fr"] = {
        "title": "Music Recommender - Recommandation hybride",
        "description": "Recommandation musicale Word2Vec + embeddings de contenu, interface Streamlit.",
        "kicker": "Recommandation",
        "heading": "Music Recommender — signaux hybrides",
        "subtitle": "Mélanger cooccurrences Word2Vec et similarité sémantique de métadonnées.",
        "meta": [
            {"label": "Signaux", "value": "Word2Vec · embeddings"},
            {"label": "UI", "value": "Streamlit"},
        ],
        "links": [
            {
                "href": "https://github.com/BeediGoua/music-recommender-hybrid",
                "label": "GitHub",
                "external": True,
            },
            {
                "href": "https://music-recommender-hybrid.onrender.com",
                "label": "Démo",
                "external": True,
            },
        ],
        "sections": [
            {
                "title": "Approche",
                "body": "<ul><li>Prétraitement des métadonnées.</li><li>Fusion hybride et filtres dynamiques.</li><li>Exploration de playlists.</li></ul>",
            }
        ],
        "limitations": "<ul><li>Aucun Precision@10 / sérendipité / latence publié sans protocole vérifié.</li></ul>",
        "back": "../projects/autres-projets.html",
    }
    b["en"] = {
        "title": "Music Recommender - Hybrid recommendation",
        "description": "Music recommendation with Word2Vec + content embeddings and a Streamlit UI.",
        "kicker": "Recommendation",
        "heading": "Music Recommender — hybrid signals",
        "subtitle": "Blend Word2Vec co-occurrence with semantic metadata similarity.",
        "meta": [
            {"label": "Signals", "value": "Word2Vec · embeddings"},
            {"label": "UI", "value": "Streamlit"},
        ],
        "links": [
            {
                "href": "https://github.com/BeediGoua/music-recommender-hybrid",
                "label": "GitHub",
                "external": True,
            },
            {
                "href": "https://music-recommender-hybrid.onrender.com",
                "label": "Demo",
                "external": True,
            },
        ],
        "sections": [
            {
                "title": "Approach",
                "body": "<ul><li>Metadata preprocessing.</li><li>Hybrid fusion and dynamic filters.</li><li>Playlist exploration.</li></ul>",
            }
        ],
        "limitations": "<ul><li>No Precision@10 / serendipity / latency published without a verified protocol.</li></ul>",
        "back": "../projects/autres-projets-en.html",
    }
    return b


def zimnat():
    b = _base("zimnat", "zimnat.html")
    b["fr"] = {
        "title": "Zimnat - Recommandation d’assurance",
        "description": "Prototype de recommandation multi-produits avec CatBoost et règles métier.",
        "kicker": "Prototype · assurance",
        "heading": "Zimnat — recommandation multi-produits",
        "subtitle": "Proposer des produits pertinents sans recommander ceux déjà détenus.",
        "meta": [
            {"label": "Modèle", "value": "CatBoost + règles"},
            {"label": "UI", "value": "Streamlit"},
            {"label": "Statut", "value": "Démonstrateur"},
        ],
        "links": [
            {
                "href": "https://github.com/BeediGoua/Insurance_product_recommender",
                "label": "GitHub",
                "external": True,
            }
        ],
        "sections": [
            {
                "title": "Approche",
                "body": "<ul><li>Baseline statistique et modèle CatBoost.</li><li>Recalibrage des probabilités.</li><li>Exclusion des produits déjà détenus (règle métier).</li></ul>",
            }
        ],
        "limitations": "<ul><li>Règle d’exclusion ≠ garantie d’erreur commerciale nulle.</li><li>Prototype / démonstrateur, pas un déploiement validé en production.</li></ul>",
        "back": "../projects/autres-projets.html",
    }
    b["en"] = {
        "title": "Zimnat - Insurance recommendation",
        "description": "Multi-product recommendation prototype with CatBoost and business rules.",
        "kicker": "Prototype · insurance",
        "heading": "Zimnat — multi-product recommendation",
        "subtitle": "Suggest relevant products without recommending ones already owned.",
        "meta": [
            {"label": "Model", "value": "CatBoost + rules"},
            {"label": "UI", "value": "Streamlit"},
            {"label": "Status", "value": "Demonstrator"},
        ],
        "links": [
            {
                "href": "https://github.com/BeediGoua/Insurance_product_recommender",
                "label": "GitHub",
                "external": True,
            }
        ],
        "sections": [
            {
                "title": "Approach",
                "body": "<ul><li>Statistical baseline and CatBoost model.</li><li>Probability recalibration.</li><li>Exclusion of already-owned products (business rule).</li></ul>",
            }
        ],
        "limitations": "<ul><li>Exclusion rule ≠ zero commercial-error guarantee.</li><li>Prototype / demonstrator, not a validated production deployment.</li></ul>",
        "back": "../projects/autres-projets-en.html",
    }
    return b


def autres():
    b = _base("autres-projets", "autres-projets.html")
    b["fr"] = {
        "title": "Autres projets",
        "description": "Index des projets complémentaires du portfolio de Goua Beedi.",
        "kicker": "Index",
        "heading": "Autres projets",
        "subtitle": "Travaux complémentaires, avec le même niveau d’exigence sur ce qui est affirmé.",
        "meta": [],
        "links": [],
        "sections": [
            {
                "title": "Liste",
                "body": """<ul>
<li><a href="retail-demand-forecasting.html">Retail Demand Forecasting</a> — prévision et stock</li>
<li><a href="analyse-survie.html">Analyse de survie</a> — méthode, sans résultats cliniques publics</li>
<li><a href="reviewguardian.html">ReviewGuardian</a> — modération de toxicité</li>
<li><a href="music-recommender.html">Music Recommender</a> — recommandation hybride</li>
<li><a href="zimnat.html">Zimnat</a> — recommandation d’assurance (prototype)</li>
<li><a href="finzuu.html">FINZUU</a> — scoring agricole</li>
<li><a href="ville-de-paris.html">Ville de Paris</a> — mobilité</li>
</ul>""",
            }
        ],
        "limitations": "",
        "back": "../index.html#projects",
    }
    b["en"] = {
        "title": "Other projects",
        "description": "Index of additional projects in Goua Beedi's portfolio.",
        "kicker": "Index",
        "heading": "Other projects",
        "subtitle": "Additional work, with the same care about what is claimed.",
        "meta": [],
        "links": [],
        "sections": [
            {
                "title": "List",
                "body": """<ul>
<li><a href="retail-demand-forecasting-en.html">Retail Demand Forecasting</a> — forecast and inventory</li>
<li><a href="analyse-survie-en.html">Survival analysis</a> — methods only, no public clinical results</li>
<li><a href="reviewguardian-en.html">ReviewGuardian</a> — toxicity moderation</li>
<li><a href="music-recommender-en.html">Music Recommender</a> — hybrid recommendation</li>
<li><a href="zimnat-en.html">Zimnat</a> — insurance recommendation (prototype)</li>
<li><a href="finzuu-en.html">FINZUU</a> — agricultural scoring</li>
<li><a href="ville-de-paris-en.html">City of Paris</a> — mobility</li>
</ul>""",
            }
        ],
        "limitations": "",
        "back": "../index-en.html#projects",
    }
    return b
