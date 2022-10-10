import pandas as pd
import numpy as np

from .base_recommender import BaseRecommender
from .dataset import Dataset


class PopularityRecommender(BaseRecommender):
    """人気ベース推薦システム
    """

    def recommend(self, dataset: Dataset, top_n: int, reclist_csv: str, **kwargs):
        """人気ベース推薦システムによる推薦リストを作成し、CSVファイルに出力する。

        Parameters
        ----------
        dataset : Dataset
            データセット
        top_n : int
            上位top_n件
        reclist_csv : str
            推薦リストの出力先CSVファイル名

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
        # idを連番で付与し、列を並べ替える。
        reclist_df['id'] = pd.RangeIndex(start=1, stop=len(reclist_df.index) + 1, step=1)
        reclist_df = reclist_df[['id', 'rank', 'item_id', 'score']]

        # 推薦リストをCSVファイルに出力する。
        reclist_df.to_csv(reclist_csv, index=False, header=True, sep='\t')
