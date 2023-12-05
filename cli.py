import logging
import pandas as pd
from sklearn.linear_model import LinearRegression
from logic import Game, Human, Bot, write_to_csv

DATABASE_FILE = 'logs/game_results.csv'
LOG_FILE = 'logs/infos.log'

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(levelname)s %(asctime)s %(message)s',
)

if __name__ == '__main__':
    import random
    
    for _ in range(30):
        player_mode = random.choice(['human', 'bot'])
        if player_mode == 'human':
            game = Game(Human('X'), Human('O'))
        else:
            game = Game(Human('X'), Bot('O'))
        game.run()
        
    df = pd.read_csv(DATABASE_FILE)
    print("Descriptive Statistics:")
    print(df.describe())
    
    X = df['First_Player_Moves'].values.reshape(-1, 1)
    y = df['Winner'].apply(lambda x: 1 if x == 'X' else 0).values

    model = LinearRegression()
    model.fit(X, y)

    print("\nLinear Regression Model:")
    print(f"Coefficient: {model.coef_[0]}")
    print(f"Intercept: {model.intercept_}")
    
    
    positions = [[0], [1], [2]]  # Assuming 0: Corner, 1: Center, 2: Middle
    likelihoods = model.predict(positions)

    print("\nLikelihood of Winning from Each Game Position:")
    for pos, likelihood in zip(positions, likelihoods):
        print(f"Position {pos[0]}: {likelihood * 100:.2f}%")
