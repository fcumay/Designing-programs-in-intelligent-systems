class Stats():
    """statistics"""
    name=''

    def __init__(self):
        """init statistic"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        '''Change in time'''
        self.guns_left = 2
        self.score = 0
