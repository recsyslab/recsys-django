/**
 * メインページクラス
 */
class MainPage extends Page {
    /*
     * @override
     */
    constructor(canvas, context) {
        super(canvas, context);

        // 推薦スロット配列
        this.slots = new Array(MAIN_SLOT_COUNT);
        for (let i = 0; i < this.slots.length; i++) {
            this.slots[i] = new Slot(MAIN_SLOT_LEFT, MAIN_SLOT_TOP + (SLOT_HEIGHT + MARGIN) * i, SLOT_WIDTH, SLOT_HEIGHT, SLOT_SIZE);
        }
    }
    /*
     * @override
     */
    onClick(x, y) {
        // 各推薦スロット内のボタンクリックの判定
        for (let i = 0; i < this.slots.length; i++) {
            if (this.slots[i].prevButton.isWithin(x, y)) {
                // 「前へ」ボタン
                this.slots[i].prev();
                return;
            } else if (this.slots[i].nextButton.isWithin(x, y)) {
                // 「次へ」ボタン
                this.slots[i].next();
                return;
            }
        }

        // 各推薦スロット内のアイテムクリックの判定
        for (let i = 0; i < this.slots.length; i++) {
            let itemComponent = this.slots[i].getItemOn(x, y);
            if (itemComponent == null) continue;
            currentPage = detailPage;
            detailPage.open(itemComponent.item);
            return;
        }
    }
    /*
     * @override
     */
    onMouseMove(x, y) {
        // 各状態の初期化
        for (let i = 0; i < this.slots.length; i++) {
            this.slots[i].prevButton.isActive = false;
            this.slots[i].nextButton.isActive = false;

            for (let j = 0; j < this.slots[i].size; j++) {
                if (!this.slots[i].isActive) continue;
                let itemComponent = this.slots[i].itemComponents[j];
                itemComponent.isActive = false;
            }
        }

        // 各推薦スロット内のボタン上のマウス移動の判定
        for (let i = 0; i < this.slots.length; i++) {
            if (this.slots[i].prevButton.isWithin(x, y)) {
                this.canvas.style = 'cursor: pointer';
                this.slots[i].prevButton.isActive = true;
                return;
            } else if (this.slots[i].nextButton.isWithin(x, y)) {
                this.canvas.style = 'cursor: pointer';
                this.slots[i].nextButton.isActive = true;
                return;
            }
        }

        // 各推薦スロット内のアイテム上のマウス移動の判定
        for (let i = 0; i < this.slots.length; i++) {
            if (!this.slots[i].isActive) continue;
            let itemComponent = this.slots[i].getItemOn(x, y);
            if (itemComponent != null) {
                this.canvas.style = 'cursor: pointer';
                itemComponent.isActive = true;
                return;
            }
        }
    }
    /*
     * @override
     */
    draw() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // 推薦スロット配列
        for (let i = 0; i < this.slots.length; i++) {
            this.slots[i].draw(this.context);
        }
    }
    /**
     * ランダム推薦システムによる推薦リストを取得する。
     */
    getRandomRecommendations() {
        let thisPage = this;
        $.ajax({
            url: 'random/',
            method: 'GET',
            data: {
            },
            timeout: 10000,
            dataType: 'json',
        }).done(function(response) {
            let description = response.description;
            let reclist = response.reclist;
            thisPage.slots[MAIN_SLOT_RANDOM].isActive = true;
            thisPage.slots[MAIN_SLOT_RANDOM].setRecList(description, reclist);
            thisPage.draw();
        }).fail(function(response) {
            window.alert('MainPage::getRandomRecommendations() : failed');
        });
    }
    /**
     * 人気ベース推薦システムによる推薦リストを取得する。
     */
    getPopularityBasedRecommendations() {
        let thisPage = this;
        $.ajax({
            url: 'popularity/',
            method: 'GET',
            data: {
            },
            timeout: 10000,
            dataType: "json",
        }).done(function(response) {
            let description = response.description;
            let reclist = response.reclist;
            thisPage.slots[MAIN_SLOT_POPULARITY].isActive = true;
            thisPage.slots[MAIN_SLOT_POPULARITY].setRecList(description, reclist);
            thisPage.draw();
        }).fail(function(response) {
            window.alert('MainPage::getPopularityBasedRecommendations() : failed');
        });
    }
    /**
     * アイテムベース協調フィルタリングによる推薦リストを取得する。
     */
    getItemcfBasedRecommendations() {
        let thisPage = this;
        $.ajax({
            url: 'itemcf/',
            method: 'GET',
            data: {
            },
            timeout: 10000,
            dataType: "json",
        }).done(function(response) {
            let description = response.description;
            let reclist = response.reclist;
            if (reclist == null) return;
            if (reclist.length <= 0) return;
            thisPage.slots[MAIN_SLOT_ITEMCF].isActive = true;
            thisPage.slots[MAIN_SLOT_ITEMCF].setRecList(description, reclist);
            thisPage.draw();
        }).fail(function(response) {
            window.alert('MainPage::getItemcfBasedRecommendations() : failed');
        });
    }
}