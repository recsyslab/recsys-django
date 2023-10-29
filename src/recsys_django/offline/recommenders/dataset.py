import numpy as np
import pandas as pd


class Dataset:
    """データセットクラス

    Attributes
    ----------
    users_df : DataFrame
        ユーザデータフレーム
    items_df : DataFrame
        アイテムデータフレーム
    ratings_df : DataFrame
        評価値データフレーム
    rating_matrix_df : DataFrame
        評価値行列データフレーム
    item_similarity_matrix_df : DataFrame
        アイテム-アイテム類似度行列データフレーム
    user_ids : ndarray
        ユーザID配列
    item_ids : ndarray
        アイテムID配列
    """

    def __init__(self, users_csv: str, items_csv: str, ratings_csv: str):
        """コンストラクタ

        Parameters
        ----------
        users_csv : str
            ユーザデータのCSVファイル名
        items_csv : str
            アイテムデータのCSVファイル名
        ratings_csv : str
            評価値データのCSVファイル名
        """
        # データセットを読み込む。
        self.users_df = pd.read_csv(users_csv, index_col=None, header=0, sep='\t')
        self.items_df = pd.read_csv(items_csv, index_col=None, header=0, sep='\t')
        self.ratings_df = pd.read_csv(ratings_csv, index_col=None, header=0, sep='\t')
        self.rating_matrix_df = None
        self.item_similarity_matrix_df = None

        # ユーザID配列、アイテムID配列を取得する。
        self.user_ids = np.array(self.users_df['user_id'].drop_duplicates())
        self.item_ids = np.array(self.items_df['item_id'].drop_duplicates())

    def to_rating_matrix(self, rating_matrix_csv: str):
        """データセットを基に評価値行列を作成する。

        Parameters
        ----------
        rating_matrix_csv : str
            評価値行列の出力先CSVファイル名
        """
        # 評価値行列を作成する。
        self.rating_matrix_df = pd.DataFrame(index=self.user_ids, columns=self.item_ids)

        # 評価値行列の要素を入力する。
        for tpl in self.ratings_df.itertuples():
            user_id = tpl.user_id
            item_id = tpl.item_id
            rating = tpl.rating
            self.rating_matrix_df.loc[user_id, item_id] = rating

        # 評価値行列をcsvで出力する。
        self.rating_matrix_df.to_csv(rating_matrix_csv, index=True, header=True, sep='\t')
        self.rating_matrix_df = pd.read_csv(rating_matrix_csv, index_col=0, header=0, sep='\t')

    def to_item_similarity_matrix(self, item_similarity_matrix_csv: str):
        """データセットを基にアイテム-アイテム類似度行列を作成する。

        Parameters
        ----------
        item_similarity_matrix_csv : str
            アイテム-アイテム類似度行列の出力先CSVファイル名
        """
        def adjusted_cos(i: int, j: int) -> float:
            """評価値行列R2におけるアイテムiとアイテムjの調整コサイン類似度を返す。

            Parameters
            ----------
            i : int
                アイテムiのID
            j : int
                アイテムjのID

            Returns
            -------
            cosine : float
                調整コサイン類似度
            """
            Uij = np.intersect1d(Ui[i], Ui[j])
            if Uij.size <= 0: return 0.0

            num = np.sum([R2[u, i] * R2[u, j] for u in Uij])
            den_i = np.sqrt(np.sum([R2[u, i] ** 2 for u in Uij]))
            den_j = np.sqrt(np.sum([R2[u, j] ** 2 for u in Uij]))
            cosine = num / (den_i * den_j)
            return cosine

        def sim(i: int, j: int) -> float:
            """アイテム類似度関数：アイテムiとアイテムjのアイテム類似度を返す。

            Parameters
            ----------
            i : int
                アイテムiのID
            j : int
                アイテムjのID

            Returns
            -------
            float
                アイテム類似度
            """
            return adjusted_cos(i, j)

        _, _, I, Ui, _, R2, _ = self.load()
        S = np.array([[sim(i, j) for j in I] for i in I])
        self.item_similarity_matrix_df = pd.DataFrame(S, index=self.item_ids, columns=self.item_ids)
        self.item_similarity_matrix_df.to_csv(item_similarity_matrix_csv, index=True, header=True, sep='\t')
        self.item_similarity_matrix_df = pd.read_csv(item_similarity_matrix_csv, index_col=0, header=0, sep='\t')

    def load(self) -> tuple:
        """各データを変数として返す。

        Returns
        -------
        ndarray
            評価値行列
        ndarray
            ユーザ配列
        ndarray
            アイテム配列
        list[ndarray]
            アイテムiを評価済みのユーザ配列のリスト
        list[ndarray]
            ユーザuが評価済みのアイテム配列のリスト
        ndarray
            平均中心化評価値行列
        ndarray
            アイテム-アイテム類似度行列
        """
        R = np.array(self.rating_matrix_df)
        U = np.arange(R.shape[0])
        I = np.arange(R.shape[1])
        Ui = [U[~np.isnan(R)[:, i]] for i in I]
        Iu = [I[~np.isnan(R)[u, :]] for u in U]
        ru_mean = np.nanmean(R, axis=1)
        # ri_mean = np.nanmean(R, axis=0)
        R2 = R - ru_mean.reshape((ru_mean.size, 1))
        S = np.array(self.item_similarity_matrix_df)
        return R, U, I, Ui, Iu, R2, S
