import numpy as np
from option import Option 

class MonteCarlo:
        def __init__(self, price, strike, time, rate, volatility, option_type):
            if time <=0:
                raise ValueError("Time must be >0")
            if price <=0:
                raise ValueError("Price must be >0")
            if strike <= 0:
                raise ValueError("Strike must be > 0")
            if volatility <= 0:
                raise ValueError("Volatility must be > 0")
            if option_type not in ['call', 'put']:
                raise ValueError("option_type must be 'call' or 'put'")
            self.s = price 
            self.k = strike 
            self.t = time 
            self.r = rate
            self.sigma = volatility
            self.type = option_type


        def generate_paths(self, simul=10000, step=100):
            dt = self.t / step
            Z = np.random.standard_normal((simul, step))
            paths = np.zeros((simul, step + 1))
            paths[:, 0] = self.s  
            for i in range(step):
                drift = self.r * paths[:, i] * dt
                diffusion = self.sigma * paths[:, i] * np.sqrt(dt) * Z[:, i]
                paths[:, i + 1] = paths[:, i] + drift + diffusion
            return paths
        
        def gain(self, final_price):
            if self.type == 'call':
                gain = np.maximum(final_price - self.k, 0)
            else:
                gain = np.maximum(self.k - final_price, 0)
            return gain
        
        def prix(self):
            paths= self.generate_paths(simul=1000, step = 100)
            prix_finaux=paths[:,-1]
            gains=self.gain(prix_finaux)
            mean_prix= np.exp(-self.r*self.t)*np.mean(gains)
            error = np.exp(-self.r*self.t)*np.std(gains)/np.sqrt(1000)
            lower = mean_prix - 1.96* error
            upper = mean_prix + 1.96 *error 
            return {'prix' : mean_prix, 'erreur' : error, 'lower' : lower, 'upper' : upper }


        def compare_with_bs(self, simul):
            paths = self.generate_paths(50000, 100)
            prix_finaux = paths[:, -1]
            gains = self.gain(prix_finaux)
            mc_price = np.exp(-self.r * self.t) * np.mean(gains)
            opt_bs = Option(self.s, self.k, self.t, self.r, self.sigma, self.type)
            bs_price = opt_bs.get_price()
            difference = abs(mc_price - bs_price)
            relative_error = (difference / bs_price) * 100
            return {'mc_price': mc_price, 'bs_price': bs_price, 'difference': difference, 'relative_error': relative_error }
        

