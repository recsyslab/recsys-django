import time

from recommenders.dataset import Dataset
from recommenders.popularity import PopularityRecommender
from recommenders.item_similarity import ItemSimilarityRecommender
from recommenders.itemcf import ItemCFRecommender


start = time.time()

# �f�[�^�Z�b�g��CSV�t�@�C������e�f�[�^�Z�b�g����������B
dataset = Dataset('data/users.csv', 'data/items.csv', 'data/ratings.csv')
dataset.to_rating_matrix('data/rating_matrix.csv')
dataset.to_item_similarity_matrix('data/item_similarity_matrix.csv')

# �e���E�V�X�e�������s���A���E���X�g��CSV�t�@�C���ɏo�͂���B
recommender = PopularityRecommender()
recommender.recommend(dataset, top_n=3, reclist_csv='data/reclist_popularity.csv', minimum_num_rating=3)
recommender = ItemSimilarityRecommender()
recommender.recommend(dataset, top_n=3, reclist_csv='data/reclist_similarity.csv', minimum_similarity=0.0)
recommender = ItemCFRecommender()
recommender.recommend(dataset, top_n=3, reclist_csv='data/reclist_itemcf.csv', minimum_similarity=0.0)

elapsed_time = time.time() - start
print("elapsed_time:{:.3f}".format(elapsed_time) + "[sec]")
