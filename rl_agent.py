import numpy as np

class ThompsonSamplingAgent:
    def __init__(self, n_difficulties=3):
        self.n = n_difficulties
        # Beta prior: alpha=2, beta=2 (optimistic but balanced)
        self.alpha = np.ones(n_difficulties) * 2
        self.beta = np.ones(n_difficulties) * 2

    def choose_difficulty(self):
        samples = np.random.beta(self.alpha, self.beta)
        return int(np.argmax(samples) + 1)

    def update(self, difficulty, correct, time_taken):
        d = difficulty - 1
        if correct:
            if time_taken >= 3.0:      # Optimal zone: challenged but correct
                self.alpha[d] += 3
            else:                       # Too easy
                self.alpha[d] += 1
        else:
            self.beta[d] += 3           # Strong negative signal

    def get_stats(self):
        total = self.alpha + self.beta
        return {
            "estimated_mastery": (self.alpha / total).tolist(),
            "confidence": total.tolist()
        }