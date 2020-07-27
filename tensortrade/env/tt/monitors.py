

from tensortrade.env.generic import Monitor


class TensorTradeMonitor(Monitor):

    def __init__(self):
        super().__init__()

    def info(self, env):
        return {
            'step': self.clock.step,
            'portfolio': env.action_scheme.portfolio,
            'broker': env.action_scheme.broker,
            'net_worth': env.action_scheme.portfolio.net_worth
        }