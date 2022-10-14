import pandas as pd
import numpy as np

from .base_recommender import BaseRecommender
from .dataset import Dataset


class ItemCFRecommender(BaseRecommender):
    """アイテムベース協調フィルタリング
    """

    def recommend(self, dataset: Dataset, top_n: int, reclist_csv: str, **kwargs):
        """アイテムベース協調フィルタリングによる推薦リストを作成し、CSVファイルに出力する。

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
        k_items : int, optional
            近傍アイテム数
        minimum_similarity : float, optional
            類似度のしきい値
        """
        # 近傍アイテム数
        k_items = kwargs.get('k_items', 3)
        # 類似度のしきい値
        minimum_similarity = kwargs.get('minimum_similarity', 0.0)

        def predict(u: int, i: int) -> float:
            """予測関数：ユーザuのアイテムiに対する予測評価値を返す。

            Parameters
            ----------
            u : int
                ユーザuのID
            i : int
                アイテムiのID

            Returns
            -------
            float
                ユーザuのアイテムiに対する予測評価値
            """
            # アイテムiの類似アイテム集合の中でユーザuが評価値を与えているアイテム集合
            Iiu = np.intersect1d(Ii[i], Iu[u])

            # ユーザuのアイテムiに対する予測評価値
            ru_mean = np.nanmean(R, axis=1)
            if Iiu.size <= 0: return ru_mean[u]

            num = np.sum([(S[i, j] * R[u, j]) for j in Iiu])
            den = np.sum([np.abs(S[i, j]) for j in Iiu])
            rui_pred = num / den if den > 0 else 0.0

            return rui_pred

        # データの取得
        R, U, I, _, Iu, _, S = dataset.load()

        # アイテム-アイテム類似度行列から対象アイテムを除外した辞書を作成する。
        Ii = {i: {j: S[i, j] for j in I if i != j} for i in I}
        Ii = {i: dict(sorted(Ii[i].items(), key=lambda x: x[1], reverse=True)[:k_items]) for i in I}
        Ii = {i: {j: s for j, s in Ii[i].items() if s >= minimum_similarity} for i in I}
        Ii = {i: np.array(list(Ii[i].keys())) for i in I}

        # 評価値行列の欠損値を予測評価値で補完する。
        R3 = np.array([[predict(u, i) if np.isnan(R[u, i]) else np.nan for i in I] for u in U])
        R3_df = pd.DataFrame(R3, index=dataset.user_ids, columns=dataset.item_ids)

        # 推薦リストの作成
        reclist_df = R3_df.stack()
        reclist_df = reclist_df.reset_index()
        reclist_df = reclist_df.rename(columns={
            'level_0': 'user_id',
            'level_1': 'item_id',
            0: 'score',
        })

        # アイテム類似度がしきい値未満のアイテムとを除外する。
        reclist_df = reclist_df.query('score >= @minimum_similarity')

        # 対象ユーザごとにスコアの降順に順位を付けて、ソートする。
        reclist_df.loc[:, 'rank'] = reclist_df.groupby(['user_id'])['score'].rank(ascending=False, method='first')
        reclist_df = reclist_df.sort_values(['user_id', 'rank'])
        # 対象ユーザごとに上位top_n件を残す。
        reclist_df = reclist_df.groupby('user_id')
        reclist_df = reclist_df.head(top_n)
        # idを連番で付与し、列を並べ替える。
        reclist_df['id'] = pd.RangeIndex(start=1, stop=len(reclist_df.index) + 1, step=1)
        reclist_df = reclist_df[['id', 'user_id', 'rank', 'item_id', 'score']]

        # 推薦リストをCSVファイルに出力する。
        reclist_df.to_csv(reclist_csv, index=False, header=True, sep='\t')
