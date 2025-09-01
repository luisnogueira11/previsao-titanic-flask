# 🚢 Previsão de Sobrevivência no Titanic

![Prévia do Site](assets/preview.png) Uma aplicação web construída com Flask e Scikit-learn que utiliza um modelo de Machine Learning para prever se um passageiro teria sobrevivido ao desastre do Titanic com base em suas características.

**Visite a aplicação online:** [https://SEU-SITE.onrender.com](https://titanic-predictor-09r5.onrender.com)

---

## ✨ Funcionalidades Principais

* **Interface Interativa:** Formulário web simples e responsivo para que o usuário insira seus dados.
* **Previsão em Tempo Real:** O modelo de Machine Learning processa os dados e retorna a previsão de sobrevivência instantaneamente.
* **Análise de Dados Completa:** O projeto inclui um notebook Jupyter (`.ipynb`) com toda a análise exploratória dos dados, limpeza, treinamento e avaliação do modelo.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Back-end:**
    * ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    * ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
* **Front-end:**
    * ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    * ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
    * ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
* **Ciência de Dados:**
    * ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
    * ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
    * ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white)
* **Deploy:**
    * ![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

---

## 🚀 Como Executar o Projeto Localmente

Para rodar este projeto no seu próprio computador, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Flask:**
    ```bash
    flask run
    ```

5.  Abra seu navegador e acesse `http://127.0.0.1:5000`.

---

## 📂 Estrutura do Projeto

/projeto_titanic
|
|-- .gitignore
|-- app.py                    # Lógica do back-end (Flask)
|-- requirements.txt          # Dependências do projeto
|-- titanic_survival_model.pkl  # Modelo de ML treinado
|-- README.md                 # Documentação do projeto
|
|-- /data/
|   |-- train.csv
|
|-- /notebook/
|   |-- AnaliseExploratoriaTitanic.ipynb
|
|-- /static/                  # Arquivos estáticos (CSS, imagens)
|   |-- style.css
|
|-- /templates/               # Arquivos HTML do front-end
|   |-- index.html
