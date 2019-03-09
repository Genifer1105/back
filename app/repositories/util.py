class Utils:
    
    @staticmethod   
    def row2dict(row):
        d = {}
        for tup in row.items():
            d = {**d, **{tup[0]: tup[1]}}
        return d