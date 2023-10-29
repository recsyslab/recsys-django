class RecRandomMapper:
    """ランダム推薦マッパー

    Attributes
    ----------
    rec : Item
        推薦オブジェクト
    """

    def __init__(self, rec):
        self.rec = rec

    def as_dict(self):
        """推薦オジェクトを辞書型として取得する。

        Returns
        -------
        dict
            推薦オブジェクトを辞書型にして返す。
        """
        item = self.rec
        return {
            'rank': 1,
            'item': {
                'item_id': item.item_id,
                'name': item.name,
                'red': item.red,
                'white': item.white,
                'shining': item.shining,
            },
            'score': 1,
        }


class RecPopularityMapper:
    """人気ベース推薦マッパー

    Attributes
    ----------
    rec : ReclistPopularity
        推薦オブジェクト
    """

    def __init__(self, rec):
        self.rec = rec

    def as_dict(self):
        """推薦オジェクトを辞書型として取得する。

        Returns
        -------
        dict
            推薦オブジェクトを辞書型にして返す。
        """
        item = self.rec.item
        return {
            'rank': self.rec.rank,
            'item': {
                'item_id': item.item_id,
                'name': item.name,
                'red': item.red,
                'white': item.white,
                'shining': item.shining,
            },
            'score': self.rec.score,
        }


class RecSimilarityMapper:
    """アイテム類似度ベース推薦マッパー

    Attributes
    ----------
    rec : ReclistSimilarity
        推薦オブジェクト
    """

    def __init__(self, obj):
        self.obj = obj

    def as_dict(self):
        """推薦オジェクトを辞書型として取得する。

        Returns
        -------
        dict
            推薦オブジェクトを辞書型にして返す。
        """
        rec = self.obj
        item = rec.item
        return {
            'rank': rec.rank,
            'item': {
                'item_id': item.item_id,
                'name': item.name,
                'red': item.red,
                'white': item.white,
                'shining': item.shining,
            },
            'score': rec.score,
        }


class RecItemcfMapper:
    """アイテムベース協調フィルタリングによる推薦マッパー

    Attributes
    ----------
    rec : ReclistItemcf
        推薦オブジェクト
    """

    def __init__(self, obj):
        self.obj = obj

    def as_dict(self):
        """推薦オジェクトを辞書型として取得する。

        Returns
        -------
        dict
            推薦オブジェクトを辞書型にして返す。
        """
        rec = self.obj
        item = rec.item
        return {
            'rank': rec.rank,
            'item': {
                'item_id': item.item_id,
                'name': item.name,
                'red': item.red,
                'white': item.white,
                'shining': item.shining,
            },
            'score': rec.score,
        }
