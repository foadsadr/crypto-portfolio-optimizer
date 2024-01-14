from config import *
from crypto_portfolio_optimizer import CrytoPortfolioOptimizer


if __name__ == "__main__":
	portfolio_optimizer = CrytoPortfolioOptimizer(start_wallet_size_usd=START_WALLET_SIZE_USD, candidate_coins=CANDIDATE_COINS, simulation_start_date=SIMULATION_START_DATE, simulation_end_date=SIMULATION_END_DATE, weights_step_precision_percent=WEIGHTS_STEP_PRECISION_PERCENT)
	portfolio_optimizer.find_best_portfolio()
