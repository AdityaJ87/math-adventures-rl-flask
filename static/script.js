let sessionId = null;
let startTime = 0;

async function startGame() {
    const name = document.getElementById('name').value || "Player";
    const difficulty = document.getElementById('difficulty').value;

    const res = await fetch('/start', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, difficulty})
    });

    const data = await res.json();
    sessionId = data.session_id;

    document.getElementById('start-screen').style.display = 'none';
    document.getElementById('game-screen').style.display = 'block';
    document.getElementById('question').textContent = data.question;
    document.getElementById('level').textContent = data.difficulty;
    startTime = performance.now();
}

async function submitAnswer() {
    const answer = parseInt(document.getElementById('answer').value);
    if (isNaN(answer)) return alert("Please enter a number!");

    const timeTaken = (performance.now() - startTime) / 1000;

    const res = await fetch('/submit', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            session_id: sessionId,
            answer: answer,
            time_taken: timeTaken
        })
    });

    const data = await res.json();

    const feedback = document.getElementById('feedback');
    feedback.textContent = data.correct ? "Correct!" : `Wrong! Answer: ${data.correct_answer}`;
    feedback.className = data.correct ? 'correct' : 'incorrect';

    document.getElementById('acc').textContent = data.accuracy + "%";
    document.getElementById('time').textContent = data.avg_time + "s";
    document.getElementById('level').textContent = data.next_difficulty;

    setTimeout(() => {
        document.getElementById('question').textContent = data.next_question;
        document.getElementById('answer').value = '';
        feedback.textContent = '';
        startTime = performance.now();
    }, 1500);
}

// Enter key to submit
document.getElementById('answer').addEventListener('keypress', e => {
    if (e.key === 'Enter') submitAnswer();
});