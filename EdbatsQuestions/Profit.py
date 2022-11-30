class Solution(object):

    @staticmethod
    def total_profit(di):
        cp = di.get('cost_price')
        sp = di.get('sell_price')
        iv = di.get('inventory')

        if cp and sp and iv:
            return (sp - cp) * iv


if __name__ == '__main__':
    dt = {"cost_price": 2.77,
          "sell_price": 7.95,
          "inventory": 8500}
    print(Solution.total_profit(dt))
