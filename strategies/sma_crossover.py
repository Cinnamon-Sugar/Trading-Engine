import pandas as pd
from strategies.base_strategy import BaseStrategy

class SMACrossoverStrategy(BaseStrategy):
    def __init__(self, short_window=50, long_window=200):
        super().__init__()
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate buy/sell signals based on SMA crossover strategy.
        
        :param data: DataFrame with 'close' prices.
        :return: DataFrame with signals.
        """
        data['short_sma'] = data['close'].rolling(window=self.short_window).mean()
        data['long_sma'] = data['close'].rolling(window=self.long_window).mean()
        
        data['signal'] = 0
        data['signal'][self.short_window:] = \
            (data['short_sma'][self.short_window:] > data['long_sma'][self.short_window:]).astype(int)
        
        data['position'] = data['signal'].diff()
        
        return data[['close', 'short_sma', 'long_sma', 'signal', 'position']]