class TestJsonSerialize:
    """pycksonでserializeするためにコンストラクタの引数名とインスタンス変数名を合わせる必要がある
    """
    def __init__(self, var1: str, var2: str):
        self.var1 = var1
        self.var2 = var2
