class Metrics:
	def __init__(self):
		pass

	@staticmethod
	def calculate_return_percent(data_points):
		return 100 * (data_points[-1] - data_points[0]) / data_points[0]
	
	@staticmethod
	def calculate_max_drawdown_percent(data_points):
		max_val = -1
		max_drawdown_percent = -1
		for i in range(len(data_points)):
			max_val = max(max_val, data_points[i])
			max_drawdown_percent = max(max_drawdown_percent, 100 * (max_val - data_points[i]) / max_val)
		return -max_drawdown_percent
