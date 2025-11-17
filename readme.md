Math Adventures AI — Adaptive Learning with Real Reinforcement Learning
A full-stack AI-powered math tutor that automatically adjusts difficulty using Thompson Sampling (a state-of-the-art Bayesian Reinforcement Learning algorithm) to keep children aged 5–10 in their optimal learning zone.
Features

Real Reinforcement Learning (Thompson Sampling) running on the server
Personalized difficulty adaptation based on correctness + response time
Beautiful, child-friendly UI (works perfectly on tablets & phones)
Real-time feedback & statistics
Zero client-side cheating — all logic & answers are server-protected
Pure Flask + Python backend
100% open source & ready to deploy

Tech Stack
LayerTechnologyBackendPython 3.11 + FlaskReinforcement LearningThompson Sampling (Bayesian Bandit)FrontendHTML5 + CSS3 + Vanilla JavaScript

Quick Start (30 seconds)
bash# 1. Clone & enter
git clone https://github.com/AdityaJ87/math-adventures-rl-flask.git
cd math-adventures-rl-flask

# 2. Create conda environment (recommended)
conda env create -f environment.yml
conda activate math-adventures-rl

# 3. Run the server
python app.py
Open your browser → http://127.0.0.1:5000
Start learning! The AI adapts in real time.
Project Structure
textmath-adventures-rl-flask/
├── app.py                  Main Flask app + API endpoints
├── rl_agent.py             Real RL algorithm (Thompson Sampling)
├── puzzle_generator.py     Math puzzle generator (Easy/Medium/Hard)
├── templates/index.html    Frontend UI
├── static/
│   ├── style.css           Child-friendly design
│   └── script.js           Game logic & API calls
├── environment.yml         Conda environment
├── requirements.txt        Pip fallback
└── README.md               This file
How the AI Works (Reinforcement Learning)
The system treats each difficulty level as an "arm" in a multi-armed bandit problem.

Thompson Sampling maintains a Bayesian belief (Beta distribution) about how good each difficulty is for the current child.
After every answer, it updates the belief:
Correct & took ≥3 seconds → strong positive signal (optimal challenge)
Correct but too fast → mild positive (too easy)
Wrong → strong negative signal (too hard)

Next difficulty is chosen by sampling from the posterior — naturally balances exploration & exploitation.

Result: The AI quickly converges to the perfect difficulty and keeps the child in the "Flow Zone".

Future Ideas (We Can Add)

 User accounts + progress saving (SQLite / PostgreSQL)
 Parent dashboard
 Voice mode (Web Speech API)
 Multiplayer classrooms
 Export results as PDF
 Switch to DQN / PPO for even smarter adaptation
