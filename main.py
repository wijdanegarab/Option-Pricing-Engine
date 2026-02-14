from option import Option # type: ignore
import matplotlib.pyplot as plt
import numpy as np

call_option = Option(price=150, strike=155, time=0.25, rate=0.05, volatility=0.20, option_type='call')
put_option = Option(price=150, strike=155, time=0.25, rate=0.05, volatility=0.20, option_type='put')


prices = np.linspace(135, 175, 100)


delta_values = []
call_prices = []
put_prices = []

for price in prices:
    opt_call = Option(price=price, strike=155, time=0.25, rate=0.05, volatility=0.20, option_type='call')
    opt_put = Option(price=price, strike=155, time=0.25, rate=0.05, volatility=0.20, option_type='put')
    
    delta_values.append(opt_call.get_greeks()['delta'])
    call_prices.append(opt_call.get_price())
    put_prices.append(opt_put.get_price())


temps = np.linspace(0.25, 0.01, 100)
call_temps = []

for t in temps:
    opt = Option(price=150, strike=155, time=t, rate=0.05, volatility=0.20, option_type='call')
    call_temps.append(opt.get_price())



fig, axes = plt.subplots(1, 3, figsize=(18, 5))


axes[0].plot(prices, delta_values, label='DELTA', color='red', linewidth=2)
axes[0].set_xlabel('Stock Price (euros)', fontsize=11)
axes[0].set_ylabel('Delta Value', fontsize=11)
axes[0].set_title('Delta: Price Sensitivity', fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(True, alpha=0.3)


axes[1].plot(prices, call_prices, label='CALL', color='green', linewidth=2)
axes[1].plot(prices, put_prices, label='PUT', color='red', linewidth=2)
axes[1].set_xlabel('Stock Price (euros)', fontsize=11)
axes[1].set_ylabel('Option Value (euros)', fontsize=11)
axes[1].set_title('CALL and PUT Value', fontsize=12, fontweight='bold')
axes[1].legend(fontsize=10)
axes[1].grid(True, alpha=0.3)


axes[2].plot(temps, call_temps, label='CALL', color='blue', linewidth=2)
axes[2].set_xlabel('Time to Expiration (years)', fontsize=11)
axes[2].set_ylabel('CALL Value (euros)', fontsize=11)
axes[2].set_title('Time Decay Effect', fontsize=12, fontweight='bold')
axes[2].legend(fontsize=10)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
