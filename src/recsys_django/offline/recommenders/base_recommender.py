from abc import ABC, abstractmethod

from .dataset import Dataset


class BaseRecommender(ABC):
    """推薦システムの抽象規定クラス
    """

    @abstractmethod
    def recommend(self, dataset: Dataset, top_n: int, **kwargs):
        """推薦リストを作成し、推薦リストテーブルを更新する。

        Parameters
        ----------
        dataset : Dataset
            データセット
        top_n : int
            上位top_n件

        Other Parameters
        ----------------
        推薦システム固有のパラメタ
        """
        pass
