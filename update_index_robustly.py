
import os
import re

file_path = r'c:\Users\gouab\Desktop\Projet_perso\portefolio\BeediGoua.github.io\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the entire projects grid
pattern = re.compile(r'(<div id="projects-grid">)(.*?)(</div>\s*</section>)', re.DOTALL)

new_grid_content = """
      <!-- Project 3 : Zimnat Insurance -->
      <div class="project-item project-card expert-mode reveal-up" data-category="ml eda">
        <div class="browser-header">
          <span class="browser-dot dot-red"></span>
          <span class="browser-dot dot-yellow"></span>
          <span class="browser-dot dot-green"></span>
        </div>
        
        <div class="project-title-row">
          <i data-feather="umbrella" style="color: #fff; width: 32px; height: 32px;"></i>
          <h3 data-i18n="project3_title">Système de Recommandation d'Assurance (Zimnat)</h3>
        </div>

        <p class="project-desc" data-i18n="project3_desc">
          Approche ML hybride utilisant le filtrage collaboratif et basé sur le contenu pour des recommandations d'assurance personnalisées et précises chez Zimnat.
        </p>

        <div class="action-row">
          <a href="projects/zimnat.html" class="btn-expert btn-cyan-glow">
            <span data-i18n="project_learn_more">En savoir plus</span> <i data-feather="external-link" style="width: 18px;"></i>
          </a>
          
          <div class="project-techs-expert">
            <span class="tech-badge-expert">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" />
                Python
            </span>
            <span class="tech-badge-expert">
                <img src="https://raw.githubusercontent.com/catboost/catboost/master/logo/catboost_logo.svg" alt="CatBoost" style="filter: brightness(0) invert(1);" /> 
                CatBoost
            </span>
            <span class="tech-badge-expert">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" alt="Streamlit" />
                Streamlit
            </span>
          </div>
        </div>

        <div class="action-divider"></div>

        <div class="action-row">
          <a href="https://insurance-product-recommender.onrender.com/" target="_blank" rel="noopener noreferrer"
            class="btn-expert btn-green-glow">
            <span data-i18n="btn_live_demo">Live Demo</span> <i data-feather="play" style="width: 18px;"></i>
          </a>
          <a href="https://github.com/BeediGoua/Insurance_product_recommender" target="_blank" rel="noopener noreferrer"
            class="btn-expert btn-purple-glow">
            <span data-i18n="btn_github_repo">View on GitHub</span> <i data-feather="github" style="width: 18px;"></i>
          </a>
        </div>
      </div>

      <!-- Project 1 : ReviewGuardian -->
      <div class="project-item project-card expert-mode reveal-up" data-category="nlp">
        <div class="browser-header">
          <span class="browser-dot dot-red"></span>
          <span class="browser-dot dot-yellow"></span>
          <span class="browser-dot dot-green"></span>
        </div>
        
        <div class="project-title-row">
          <i data-feather="shield" style="color: #fff; width: 32px; height: 32px;"></i>
          <h3 data-i18n="project1_title">ReviewGuardian – Safe Review Pipeline</h3>
        </div>

        <p class="project-desc" data-i18n="project1_desc">
          Système de modération IA local pour détecter la toxicité et expliquer les décisions en temps réel, garantissant une confidentialité totale des données.
        </p>

        <div class="action-row">
          <a href="projects/reviewguardian.html" class="btn-expert btn-cyan-glow">
            <span data-i18n="project_learn_more">En savoir plus</span> <i data-feather="external-link" style="width: 18px;"></i>
          </a>
          
          <div class="project-techs-expert">
            <span class="tech-badge-expert">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" />
              Python
            </span>
            <span class="tech-badge-expert">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg" alt="scikit-learn" />
              scikit-learn
            </span>
            <span class="tech-badge-expert">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" alt="FastAPI" />
              FastAPI
            </span>
          </div>
        </div>

        <div class="action-divider"></div>

        <div class="action-row">
          <a href="https://reviewguardian.onrender.com/" target="_blank" rel="noopener noreferrer"
            class="btn-expert btn-green-glow">
            <span data-i18n="btn_live_demo">Live Demo</span> <i data-feather="play" style="width: 18px;"></i>
          </a>
          <a href="https://github.com/BeediGoua/ReviewGuardian" target="_blank" rel="noopener noreferrer"
            class="btn-expert btn-purple-glow">
            <span data-i18n="btn_github_repo">View on GitHub</span> <i data-feather="github" style="width: 18px;"></i>
          </a>
        </div>
      </div>

      <!-- Project 2 : Hybrid Music Recommender -->
      <div class="project-item project-card expert-mode reveal-up" data-category="ml nlp">
        <div class="browser-header">
          <span class="browser-dot dot-red"></span>
          <span class="browser-dot dot-yellow"></span>
          <span class="browser-dot dot-green"></span>
        </div>
        
        <div class="project-title-row">
          <i data-feather="headphones" style="color: #fff; width: 32px; height: 32px;"></i>
          <h3 data-i18n="project2_title">Hybrid Music Recommender</h3>
        </div>

        <p class="project-desc" data-i18n="project2_desc">
          Système de recommandation intelligent alliant Word2Vec et embeddings NLP pour une exploration musicale basée sur l'humeur, le genre et l'époque.
        </p>

        <div class="action-row">
          <a href="projects/music-recommender.html" class="btn-expert btn-cyan-glow">
            <span data-i18n="project_learn_more">En savoir plus</span> <i data-feather="external-link" style="width: 18px;"></i>
          </a>
          
          <div class="project-techs-expert">
            <span class="tech-badge-expert">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" />
              Python
            </span>
            <span class="tech-badge-expert">
              <i data-feather="activity" style="width: 14px; color: #38bdf8;"></i>
              Word2Vec
            </span>
            <span class="tech-badge-expert">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" alt="Streamlit" />
              Streamlit
            </span>
          </div>
        </div>

        <div class="action-divider"></div>

        <div class="action-row">
          <a href="https://music-recommender-hybrid.onrender.com" target="_blank" rel="noopener noreferrer"
            class="btn-expert btn-green-glow">
            <span data-i18n="btn_live_demo">Live Demo</span> <i data-feather="play" style="width: 18px;"></i>
          </a>
          <a href="https://github.com/BeediGoua/music-recommender-hybrid" target="_blank" rel="noopener noreferrer"
            class="btn-expert btn-purple-glow">
            <span data-i18n="btn_github_repo">View on GitHub</span> <i data-feather="github" style="width: 18px;"></i>
          </a>
        </div>
      </div>
    """

modified_content = pattern.sub(rf'\1\n{new_grid_content}\n    \3', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(modified_content)

print("Update complete")
