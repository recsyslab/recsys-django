import pandas as pd

from django.db import connection

from online.models import Item, ReclistSimilarity
from .base_recommender import BaseRecommender
from .dataset import Dataset


class ItemSimilarityRecommender(BaseRecommender):
    """アイテム類似度ベース推薦システム
    """

    def recommend(self, dataset: Dataset, top_n: int, **kwargs):
        """アイテム類似度ベース推薦システムによる推薦リストを作成し、推薦リストテーブルを更新する。

        Parameters
        ----------
        dataset : Dataset
            データセット
        top_n : int
            上位top_n件

        Other Parameters
        ----------------
        minimum_similarity : float, optional
            類似度のしきい値
        """
        # 類似度のしきい値
        minimum_similarity = kwargs.get('minimum_similarity', 0.0)

        # データの取得
        _, _, _, _, _, _, S = dataset.load()
        S_df = pd.DataFrame(S, index=dataset.item_ids, columns=dataset.item_ids)

        # 推薦リストの作成
        # ベースアイテムとのアイテム類似度をスコアとする。
        reclist_df = S_df.stack()
        reclist_df = reclist_df.reset_index()
        reclist_df = reclist_df.rename(columns={
            'level_0': 'base_item_id',
            'level_1': 'item_id',
            0: 'score',
        })

        # ベースアイテムと同一のアイテムおよびアイテム類似度がしきい値未満のアイテムとを除外する。
        reclist_df = reclist_df.query('base_item_id != item_id & score >= @minimum_similarity').copy()

        # ベースアイテムごとにスコアの降順に順位を付けて、ソートする。
        # reclist_df.loc[:, 'rank'] = reclist_df.groupby(['base_item_id'])['score'].rank(ascending=False, method='first')
        reclist_df['rank'] = reclist_df.groupby(['base_item_id'])['score'].rank(ascending=False, method='first')
        reclist_df = reclist_df.sort_values(['base_item_id', 'rank'])
        # ベースアイテムごとに上位top_n件を残す。
        reclist_df = reclist_df.groupby('base_item_id')
        reclist_df = reclist_df.head(top_n)

        # 推薦リストテーブルの更新
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE reclist_similarity RESTART IDENTITY")
        for tuple_ in reclist_df.itertuples():
            base_item = Item.objects.get(pk=tuple_.base_item_id)
            rank = tuple_.rank
            item = Item.objects.get(pk=tuple_.item_id)
            score = tuple_.score
            rec = ReclistSimilarity(base_item=base_item, rank=rank, item=item, score=score)
            rec.save()
