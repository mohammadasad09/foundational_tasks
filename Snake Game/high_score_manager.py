class HighScoreManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_high_scores(self):
        try:
            with open(self.file_path, 'r') as file:
                scores = [int(line.strip()) for line in file if line.strip()]
            return scores
        except FileNotFoundError:
            return []

    def get_max_score(self):
        scores = self.read_high_scores()
        return max(scores) if scores else 0
