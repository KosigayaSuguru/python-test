def error(ex):
    """例外に対して、固有のメッセージ（error_handle_test）と
    レスポンスコード（500）を設定
    flaskインスタンス(__init__.pyのapp)に対して、register_error_handlerを使って登録するパターン
    """
    print(ex)
    return "error_handle_test", 500


def error_badrequest(ex):
    """ハンドラが受け取った例外を return すると
    例外（ex）に設定された内容がレスポンスになる
    """
    return ex
