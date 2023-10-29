import pandas as pd
import numpy as np

from django.db import connection

from online.models import Item, ReclistPopularity
from .base_recommender import BaseRecommender
from .dataset import Dataset


class PopularityRecommender(BaseRecommender):
    """人気ベース推薦システム
    """

    def recommend(self, dataset: Dataset, top_n: int, **kwargs):
        """人気ベース推薦システムによる推薦リストを作成し、推薦リストテーブルを更新する。

        Parameters
        ----------
        dataset : Dataset
            データセット
        top_n : int
            上位top_n件

        Other Parameters
        ----------------
        minimum_num_rating : int, optional
            評価数のしきい値
        """
        # 評価数のしきい値
        minimum_num_rating = kwargs.get('minimum_num_rating', 0)

        # データの取得
        R, _, I, _, _, _, _ = dataset.load()

        # 評価数のしきい値以上のアイテムを取得する。
        I2 = I[np.count_nonzero(~np.isnan(R), axis=0) >= minimum_num_rating]
        # 各アイテムに対する平均評価値を取得する。
        ri_mean = np.nanmean(R, axis=0)

        # 推薦リストの作成
        # 各アイテムに対する平均評価値をスコアとする。
        reclist_df = pd.DataFrame({
            'item_id': dataset.item_ids[I2],
            'score': ri_mean[I2],
        })

        # スコアの降順に順位を付けてソートし、上位top_n件を残す。
        reclist_df.loc[:, 'rank'] = reclist_df['score'].rank(ascending=False, method='first')
        reclist_df = reclist_df.sort_values(['rank'])
        reclist_df = reclist_df.head(top_n)

        # 推薦リストテーブルの更新
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE reclist_popularity RESTART IDENTITY")
        for tuple_ in reclist_df.itertuples():
            rank = tuple_.rank
            item = Item.objects.get(pk=tuple_.item_id)
            score = tuple_.score
            rec = ReclistPopularity(rank=rank, item=item, score=score)
            rec.save()
