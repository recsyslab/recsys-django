import json

from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

from .models import Item, Rating, ReclistPopularity, ReclistSimilarity, ReclistItemcf
from .mappers import RecRandomMapper, RecPopularityMapper, RecSimilarityMapper, RecItemcfMapper


class IndexView(View):
    """インデックスビュー

    Attributes
    ----------
    context: dict
        コンテキスト
    """

    def __init__(self):
        self.context = {}

    def get(self, request, *args, **kwargs):
        """index.htmlをレンダリングしたレスポンスを取得する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト

        Returns
        -------
        HttpResponse
            index.htmlをレンダリングしたレスポンスを返す。
        """
        return render(request, 'index.html', self.context)


class RandomView(View):
    """ランダム推薦ビュー
    """

    def get(self, request, *args, **kwargs):
        """ランダム推薦リストを取得する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト

        Returns
        -------
        HttpResponse
            推薦説明と推薦リストをJSON形式で返す。
        """
        # オブジェクトの取得
        reclist = list(Item.objects.order_by('?'))
        recs = [RecRandomMapper(rec).as_dict() for rec in reclist]

        # レスポンスの生成
        description = '本日のおすすめ'
        response = {
            'description': description,
            'reclist': recs,
        }
        response_json = json.dumps(response)

        # レスポンスの返却
        return HttpResponse(response_json, content_type='application/json')


class PopularityView(View):
    """人気ベース推薦ビュー
    """

    def get(self, request, *args, **kwargs):
        """人気ベース推薦リストを取得する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト

        Returns
        -------
        HttpResponse
            推薦説明と推薦リストをJSON形式で返す。
        """
        # オブジェクトの取得
        reclist = ReclistPopularity.objects.all()
        recs = [RecPopularityMapper(rec).as_dict() for rec in reclist]

        # レスポンスの生成
        description = '人気の寿司'
        response = {
            'description': description,
            'reclist': recs,
        }
        response_json = json.dumps(response)

        # レスポンスの返却
        return HttpResponse(response_json, content_type='application/json')


class SimilarityView(View):
    """アイテム類似度ベース推薦ビュー
    """

    def get(self, request, item_id, *args, **kwargs):
        """アイテム類似度ベース推薦リストを取得する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト
        item_id : int
            ベースアイテムのアイテムID

        Returns
        -------
        HttpResponse
            推薦説明と推薦リストをJSON形式で返す。
        """
        # オブジェクトの取得
        base_item = Item.objects.get(pk=item_id)
        reclist = ReclistSimilarity.objects.filter(base_item_id=item_id)
        recs = [RecSimilarityMapper(rec).as_dict() for rec in reclist]

        # レスポンスの生成
        description = base_item.name + 'が好きな人はこんな寿司も好きです。'
        response = {
            'description': description,
            'reclist': recs,
        }
        response_json = json.dumps(response)

        # レスポンスの返却
        return HttpResponse(response_json, content_type='application/json')


class ItemcfView(View):
    """アイテムベース協調フィルタリングビュー
    """

    def get(self, request, *args, **kwargs):
        """アイテムベース協調フィルタリングによる推薦リストを取得する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト

        Returns
        -------
        HttpResponse
            推薦説明と推薦リストをJSON形式で返す。
        """
        if not request.user.is_authenticated:
            # 対象ユーザがログイン状態でない場合
            response = {
                'description': None,
            }
            response_json = json.dumps(response)
            return HttpResponse(response_json, content_type='application/json')

        # オブジェクトの取得
        user = request.user.user
        # オブジェクトの取得
        reclist = ReclistItemcf.objects.filter(user_id=user.user_id)
        recs = [RecItemcfMapper(rec).as_dict() for rec in reclist]

        # レスポンスの生成
        description = user.name + 'さんにおすすめ'
        response = {
            'description': description,
            'reclist': recs,
        }
        response_json = json.dumps(response)

        # レスポンスの返却
        return HttpResponse(response_json, content_type='application/json')


class RatingView(View):
    """評価値ビュー
    """

    def get(self, request, item_id, *args, **kwargs):
        """対象ユーザの対象アイテムの評価値を取得する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト
        item_id : int
            対象アイテムのアイテムID

        Returns
        -------
        HttpResponse
            対象ユーザの対象アイテムの評価値をJSON形式で返す。
            対象ユーザがログイン状態でなければ{'rating': -1}を返す。
            対象ユーザが対象アイテムに対して未評価の場合、{'rating': 0}を返す。
        """
        if not request.user.is_authenticated:
            # 対象ユーザがログイン状態でない場合
            response = {
                'rating': -1,
            }
            response_json = json.dumps(response)
            return HttpResponse(response_json, content_type='application/json')

        # オブジェクトの取得
        user = request.user.user
        item = Item.objects.get(pk=item_id)
        rating_model = Rating.objects.filter(user=user, item=item).first()
        rating = rating_model.rating if rating_model is not None else 0

        # レスポンスの生成
        response = {
            'rating': rating,
        }
        response_json = json.dumps(response)

        # レスポンスの返却
        return HttpResponse(response_json, content_type='application/json')

    def post(self, request, item_id, *args, **kwargs):
        """対象ユーザの対象アイテムに対する評価値を登録する。

        Parameters
        ----------
        request : WSGIRequest
            リクエスト
        item_id : int
            対象アイテムのアイテムID

        Returns
        -------
        HttpResponse
            対象ユーザがログイン状態でなければ{'rating': -1}を返す。
            対象ユーザが対象アイテムに対して未評価の場合、{'rating': 0}を返す。
        """
        if not request.user.is_authenticated:
            # 対象ユーザがログイン状態でない場合
            response = {
                'user_id': None,
            }
            response_json = json.dumps(response)
            return HttpResponse(response_json, content_type='application/json')

        # リクエストの取得
        rating = request.POST.get('rating')

        # オブジェクトの取得
        user = request.user.user
        item = Item.objects.get(pk=item_id)

        # モデルの更新
        rating_model = Rating.objects.filter(user=user, item=item).first()
        # データの追加，更新
        if rating_model is not None:
            rating_model.rating = rating
            rating_model.save()
        else:
            rating_model = Rating(user=user, item=item, rating=rating)
            rating_model.save()

        # レスポンスの生成
        response = {
        }
        response_json = json.dumps(response)

        # レスポンスの返却
        return HttpResponse(response_json, content_type='application/json')
