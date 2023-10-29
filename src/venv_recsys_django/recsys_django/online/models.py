from django.db import models


class User(models.Model):
    """ユーザモデル

    Attributes
    ----------
    user_id : IntegerField
        ユーザID
    name : TextField
        ユーザ名
    age : IntegerField
        年齢
    sex : CharField
        性別
    """
    user_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return '{}:{}'.format(self.user_id, self.name)


class Item(models.Model):
    """アイテムモデル

    Attributes
    ----------
    item_id : IntegerField
        アイテムID
    name : TextField
        アイテム名
    red : IntegerField
        赤身の特徴量
    white : IntegerField
        白身の特徴量
    shining : IntegerField
        光物の特徴量
    """
    item_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    red = models.IntegerField(blank=True, null=True)
    white = models.IntegerField(blank=True, null=True)
    shining = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'

    def __str__(self):
        return '{}:{}'.format(self.item_id, self.name)


class Rating(models.Model):
    """評価値モデル

    Attributes
    ----------
    user : ForeignKey[User]
        対象ユーザ
    item : ForeignKey[Item]
        対象アイテム
    rating : IntegerField
        評価値
    """
    user = models.ForeignKey(User, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ratings'

    def __str__(self):
        return '{}:{}:{}'.format(self.user_id, self.item_id, self.rating)


class ReclistPopularity(models.Model):
    """人気ベース推薦リストモデル

    Attributes
    ----------
    rank : FloatField
        推薦順位
    item : ForeignKey[Item]
        推薦アイテム
    score : FloatField
        推薦スコア
    """
    rank = models.FloatField()
    item = models.ForeignKey(Item, models.CASCADE)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'reclist_popularity'

    def __str__(self):
        return '{}:{}:{}'.format(self.rank, self.item, self.score)


class ReclistSimilarity(models.Model):
    """アイテム類似度ベース推薦リストモデル

    Attributes
    ----------
    base_item : ForeignKey[Item]
        ベースアイテム
    rank : FloatField
        推薦順位
    item : ForeignKey[Item]
        推薦アイテム
    score : FloatField
        推薦スコア
    """
    base_item = models.ForeignKey(Item, models.CASCADE, related_name='base_item')
    rank = models.FloatField()
    item = models.ForeignKey(Item, models.CASCADE)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'reclist_similarity'

    def __str__(self):
        return '{}:{}:{}:{}'.format(self.base_item, self.rank, self.item, self.score)


class ReclistItemcf(models.Model):
    """アイテムベース協調フィルタリングに基づく推薦リストモデル

    Attributes
    ----------
    user : ForeignKey[User]
        対象ユーザ
    rank : FloatField
        推薦順位
    item : ForeignKey[Item]
        推薦アイテム
    score : FloatField
        推薦スコア
    """
    user = models.ForeignKey(User, models.CASCADE)
    rank = models.FloatField()
    item = models.ForeignKey(Item, models.CASCADE)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'reclist_itemcf'

    def __str__(self):
        return '{}:{}:{}:{}'.format(self.user, self.rank, self.item, self.score)
