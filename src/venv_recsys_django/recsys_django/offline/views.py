import pandas as pd

from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse

from online.models import User, Item, Rating
from .recommenders.dataset import Dataset
from .recommenders.popularity import PopularityRecommender
from .recommenders.item_similarity import ItemSimilarityRecommender
from .recommenders.itemcf import ItemCFRecommender


class UpdateView(View):
    """更新ビュー
    """

    def post(self, request, *args, **kwargs):
        """推薦リストを更新する。

        Returns
        -------
        HttpResponse
            recommender:indexにリダイレクトする。
        """
        users_df = pd.DataFrame(list(User.objects.all().values()))
        items_df = pd.DataFrame(list(Item.objects.all().values()))
        ratings_df = pd.DataFrame(list(Rating.objects.all().values()))
        users_df.to_csv('offline/data/users.csv', index=True, header=True, sep='\t')
        items_df.to_csv('offline/data/items.csv', index=True, header=True, sep='\t')
        ratings_df.to_csv('offline/data/ratings.csv', index=True, header=True, sep='\t')

        # データセットのCSVファイルから各データセットを準備する。
        dataset = Dataset('offline/data/users.csv', 'offline/data/items.csv', 'offline/data/ratings.csv')
        dataset.to_rating_matrix('offline/data/rating_matrix.csv')
        dataset.to_item_similarity_matrix('offline/data/item_similarity_matrix.csv')

        # 各推薦システムを実行し、推薦リストをCSVファイルに出力する。
        recommender = PopularityRecommender()
        recommender.recommend(dataset, top_n=3, minimum_num_rating=3)
        recommender = ItemSimilarityRecommender()
        recommender.recommend(dataset, top_n=3, minimum_similarity=0.0)
        recommender = ItemCFRecommender()
        recommender.recommend(dataset, top_n=3, minimum_similarity=0.0)

        return redirect(reverse('online:index'))
