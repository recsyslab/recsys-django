/**
 * 詳細ページクラス
 */
class DetailPage extends Page {
    /*
     * @override
     */
    constructor(canvas, context) {
        super(canvas, context);

        this.itemDetailComponent = null;   // アイテム詳細コンポーネント

        // 推薦スロット
        this.slot = new Slot(DETAIL_SLOT_LEFT, DETAIL_SLOT_TOP, SLOT_WIDTH, SLOT_HEIGHT, SLOT_SIZE);

        // 「戻る」ボタン
        this.returnButton = new ReturnButton(DETAIL_RETURN_LEFT, DETAIL_RETURN_TOP, DETAIL_RETURN_WIDTH, DETAIL_RETURN_WIDTH);
    }
    /*
     * @override
     */
    onClick(x, y) {
        // アイテム詳細コンポーネント内の星クリックの判定
        let rating = this.itemDetailComponent.starRating.getRatingOn(x, y);
        if (rating > 0) {
            this.postRating(rating);
            return;
        }

        // 推薦スロット内のボタンクリックの判定
        if (this.slot.prevButton.isWithin(x, y)) {
            // 「前へ」ボタン
            this.slot.prev();
            return;
        } else if (this.slot.nextButton.isWithin(x, y)) {
            // 「次へ」ボタン
            this.slot.next();
            return;
        }

        // 推薦スロット内のアイテムクリックの判定
        let itemComponent = this.slot.getItemOn(x, y);
        if (itemComponent != null) {
            this.open(itemComponent.item);
            return;
        }

        // 「戻る」ボタンクリックの判定
        if (this.returnButton.isWithin(x, y)) {
            currentPage = mainPage;
            return;
        }
    }
    /*
     * @override
     */
    onMouseMove(x, y) {
        // 各状態の初期化
        this.itemDetailComponent.starRating.resetTempRating();
        this.slot.prevButton.isActive = false;
        this.slot.nextButton.isActive = false;
        for (let i = 0; i < this.slot.size; i++) {
            let itemComponent = this.slot.itemComponents[i];
            if (itemComponent == null) continue;
            itemComponent.isActive = false;
        }
        this.returnButton.isActive = false;

        // アイテム詳細コンポーネント内の星評価上のマウス移動の判定
        if (this.itemDetailComponent.starRating.isWithin(x, y)) {
            this.canvas.style = 'cursor: pointer';
            let tempRating = this.itemDetailComponent.starRating.getRatingOn(x, y);
            if (tempRating > 0) {
                this.itemDetailComponent.starRating.setTempRating(tempRating);
            }
            return;
        }

        // 推薦スロット内のボタン上のマウス移動の判定
        if (this.slot.prevButton.isWithin(x, y)) {
            this.canvas.style = 'cursor: pointer';
            this.slot.prevButton.isActive = true;
            return;
        } else if (this.slot.nextButton.isWithin(x, y)) {
            this.canvas.style = 'cursor: pointer';
            this.slot.nextButton.isActive = true;
            return;
        }

        // 推薦スロット内のアイテム上のマウス移動の判定
        let itemComponent = this.slot.getItemOn(x, y);
        if (itemComponent != null) {
            this.canvas.style = 'cursor: pointer';
            itemComponent.isActive = true;
            return;
        }

        // 「戻る」ボタン上のマウス移動の判定
        if (this.returnButton.isWithin(x, y)) {
            this.canvas.style = 'cursor: pointer';
            this.returnButton.isActive = true;
            return;
        }
    }
    /*
     * @override
     */
    draw() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // 対象アイテム
        this.itemDetailComponent.draw(this.context);

        // 推薦スロット
        this.slot.draw(this.context);

        // 「戻る」ボタン
        this.returnButton.draw(this.context);
    }
    /**
     * 対象アイテムをセットする。
     * @param item  対象アイテム
     */
    setItem(item) {
        this.itemDetailComponent = new ItemDetailComponent(DETAIL_ITEM_LEFT, DETAIL_ITEM_TOP, DETAIL_ITEM_WIDTH, DETAIL_ITEM_HEIGHT, item);
    }
    /**
     * 対象アイテムの詳細ページを開く。
     * @param item  対象アイテム
     */
    open(item) {
        this.setItem(item);
        this.getRating();
        this.getSimilarityBasedRecommendations(item.id);
    }
    /**
     * 対象アイテムをベースとした類似度ベース推薦システムによる推薦リストを取得する。
     */
    getSimilarityBasedRecommendations() {
        let thisPage = this;
        $.ajax({
            url: this.itemDetailComponent.item.id.toString() + '/similarity/',
            method: 'GET',
            data: {
            },
            timeout: 10000,
            dataType: "json",
        }).done(function(response) {
            let description = response.description;
            let reclist = response.reclist;
            thisPage.slot.isActive = true;
            thisPage.slot.setRecList(description, reclist);
            thisPage.draw();
        }).fail(function(response) {
            window.alert('DetailPage::getSimilarityBasedRecommendations() : failed');
        });
    }
    /*
     * アクティブユーザの対象アイテムに対する評価値を取得する。
     */
    getRating() {
        let thisPage = this;
        $.ajax({
            url: this.itemDetailComponent.item.id.toString() + '/rating/',
            method: 'GET',
            data: {
            },
            timeout: 10000,
            dataType: "json",
        }).done(function(response) {
            let rating = response.rating;
            thisPage.itemDetailComponent.starRating.setRating(rating);
            thisPage.draw();
        }).fail(function(response) {
            window.alert('DetailPage::getRating() : failed');
        });
    }
    /*
     * アクティブユーザの対象アイテムへの評価値を更新する。
     * @param rating    評価値
     */
    postRating(rating) {
        let thisPage = this;
        $.ajax({
            url: this.itemDetailComponent.item.id.toString() + '/rating/',
            method: 'POST',
            data: {
                'rating': rating,
            },
            timeout: 10000,
            dataType: "json",
        }).done(function(response) {
            thisPage.itemDetailComponent.starRating.setRating(rating);
            thisPage.draw();
        }).fail(function(response) {
            window.alert('DetailPage::postRating() : failed');
        });
    }
}