# 🥗 AI Diet Planner

A simple Streamlit application that asks the user whether they want to **gain weight** or **lose weight**, then uses **Gemini 3.6 Flash** through **LangChain** to generate a practical one-day diet plan.

## Features

- Simple Streamlit interface
- Gain weight or lose weight goal selection
- AI-generated breakfast, snacks, lunch, and dinner
- Approximate calories and protein for each meal
- Total daily calories and protein
- Gemini API key kept outside the GitHub repository
- Ready for local development with `uv`
- Can be deployed on Streamlit Community Cloud

## Project structure

```text
ai_diet_planner/
├── app.py
├── pyproject.toml
├── .python-version
├── .env.example
├── .gitignore
└── README.md
```

## 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd ai_diet_planner
```

## 2. Install dependencies with uv

This project is configured for Python 3.14.

```bash
uv python install 3.14
uv python pin 3.14
uv sync
```

`uv sync` will create the project virtual environment and generate `uv.lock`. Commit `uv.lock` to GitHub so Streamlit Community Cloud can use uv for dependency installation.

You do not need to manually activate `.venv` when using `uv run`.

Check the Python version:

```bash
uv run python --version
```

## 3. Add your Gemini API key locally

Create a file named `.env` in the project root.

```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

Do **not** upload `.env` to GitHub. It is already included in `.gitignore`.

You can use `.env.example` as a template.

## 4. Run the Streamlit app

```bash
uv run streamlit run app.py
```

Streamlit will show a local URL, normally similar to:

```text
http://localhost:8501
```

Open it in your browser.

## 5. Publish the project to GitHub

Create an empty repository on GitHub and run:

```bash
git init
git add .
# Make sure uv.lock is included after running uv sync
git commit -m "Initial AI diet planner app"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main
```

Before pushing, confirm that `.env` is not included:

```bash
git status
```

Your API key should never appear in the GitHub repository.

## 6. Deploy on Streamlit Community Cloud

1. Push this project to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app and select your GitHub repository.
4. Set the entrypoint file to `app.py`.
5. In **Advanced settings**, select Python 3.14 if available for your deployment.
6. Add your API key to **Secrets**:

```toml
GOOGLE_API_KEY = "your_actual_gemini_api_key_here"
```

7. Save the settings and deploy the app.

Do not commit `.streamlit/secrets.toml` or `.env` to GitHub.

## Main technologies

- Python
- Streamlit
- LangChain
- `langchain-google-genai`
- Google Gemini 3.6 Flash
- `python-dotenv`
- uv

## Example workflow

```text
User opens app
      ↓
Chooses Gain Weight or Lose Weight
      ↓
Clicks Generate Diet Plan
      ↓
Prompt is created using the selected goal
      ↓
Gemini 3.6 Flash generates the response
      ↓
Diet plan is displayed in Streamlit
```

## Important note

This project is intended as an educational/demo application. AI-generated nutrition information should not be treated as personalised medical advice. People with medical conditions, allergies, pregnancy, eating-disorder concerns, or clinical nutrition needs should consult an appropriately qualified healthcare professional.

## Future improvements

You can extend the app with inputs for:

- Age
- Height and weight
- Activity level
- Vegetarian, vegan, or non-vegetarian preference
- Allergies
- Number of meals
- Country or cuisine preference
- Multi-day meal plans
- Downloadable diet-plan reports
