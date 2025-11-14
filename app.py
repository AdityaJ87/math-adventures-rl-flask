from flask import Flask, render_template, request, jsonify, session
from rl_agent import ThompsonSamplingAgent
from puzzle_generator import generate_puzzle
import secrets
import time

app = Flask(__name__)
app.secret_key = "super-secret-math-key-2025"

# In-memory sessions (use Redis in production)
active_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_session():
    data = request.json
    name = data.get('name', 'Player').strip() or 'Player'
    init_diff = int(data.get('difficulty', 2))

    session_id = secrets.token_hex(8)
    agent = ThompsonSamplingAgent()

    question, answer = generate_puzzle(init_diff)

    active_sessions[session_id] = {
        'name': name,
        'agent': agent,
        'stats': {'correct': 0, 'total': 0, 'times': []},
        'current_question': question,
        'current_answer': answer,
        'current_difficulty': init_diff,
        'start_time': time.time()
    }

    return jsonify({
        'session_id': session_id,
        'question': question,
        'difficulty': init_diff,
        'message': f"Welcome {name}! Let's start!"
    })

@app.route('/submit', methods=['POST'])
def submit_answer():
    data = request.json
    sid = data.get('session_id')
    if sid not in active_sessions:
        return jsonify({'error': 'Session expired. Please restart.'}), 404

    sess = active_sessions[sid]
    agent = sess['agent']
    stats = sess['stats']
    user_answer = int(data['answer'])
    time_taken = float(data['time_taken'])

    correct = user_answer == sess['current_answer']
    stats['total'] += 1
    if correct:
        stats['correct'] += 1
    stats['times'].append(time_taken)

    # Update RL agent
    agent.update(sess['current_difficulty'], correct, time_taken)

    # Choose next difficulty
    next_diff = agent.choose_difficulty()
    next_q, next_ans = generate_puzzle(next_diff)

    # Update session
    sess['current_question'] = next_q
    sess['current_answer'] = next_ans
    sess['current_difficulty'] = next_diff

    accuracy = (stats['correct'] / stats['total']) * 100
    avg_time = sum(stats['times']) / len(stats['times']) if stats['times'] else 0

    return jsonify({
        'correct': correct,
        'correct_answer': sess['current_answer'],
        'next_question': next_q,
        'next_difficulty': next_diff,
        'accuracy': round(accuracy, 1),
        'avg_time': round(avg_time, 2),
        'total_questions': stats['total']
    })

if __name__ == '__main__':
    print("Math Adventures RL + Flask Server Running!")
    print("http://127.0.0.1:5000")
    app.run(debug=True, port=5000)