/**
 * 推薦スロットクラス
 */
class Slot extends Component {
    /**
     * @param size      推薦スロットサイズ
     */
    constructor(left, top, width, height, size) {
        super(left, top, width, height);

        this.description = null;    // 説明文
        this.items = null;          // 推薦リストに含まれるアイテム配列
        this.max = -1;              // 推薦リストに含まれるアイテム数

        this.size = size;           // 推薦スロットサイズ（表示されるアイテム数）
        this.itemComponents = null; // 推薦スロットに含まれるアイテムコンポーネント配列
        this.current = 0;           // 推薦スロット内での現在の表示位置

        // 「前へ」ボタン
        this.prevButton = new NextButton(this.left, this.top + MARGIN * 4, NEXT_BUTTON_WIDTH, NEXT_BUTTON_HEIGHT, -1);
        // 「次へ」ボタン
        this.nextButton = new NextButton(this.left + this.width - NEXT_BUTTON_WIDTH, this.top + MARGIN * 4, NEXT_BUTTON_WIDTH, NEXT_BUTTON_HEIGHT, +1);
    }
    /*
     * @override
     */
     draw(context) {
        if (!this.isActive) return;

        // 推薦スロット枠
        context.save();
        context.fillStyle = '#CCFFFF';
        context.strokeStyle = '#7FFFFF';
        context.fillRect(this.left, this.top, this.width, this.height);
        context.strokeRect(this.left, this.top, this.width, this.height);
        context.restore();

        // 推薦スロットの説明文
        context.save();
        context.font = '24px メイリオ';
        context.fillStyle = 'dimgray';
        context.strokeStyle = 'dimgray';
        context.textBaseline = 'top';
        context.textAlign = 'left';
        context.fillText(this.description, this.left + MARGIN, this.top + MARGIN);
        context.strokeText(this.description, this.left + MARGIN, this.top + MARGIN);
        context.restore();

        // 推薦スロット内に表示するアイテム
        for (let i = 0; i < this.size; i++) {
            if (this.itemComponents[i] == null) continue;
            this.itemComponents[i].draw(context);
        }

        // 「前へ」「次へ」ボタン
        this.prevButton.draw(context);
        this.nextButton.draw(context);
    }
    /*
     * 推薦スロット内に表示するアイテムをセットする。
     */
    setItems() {
        this.itemComponents = new Array(this.size);
        for (let i = 0; i < this.size; i++) {
            if (this.items.length < i + 1) break;
            let left = this.left + MARGIN + this.prevButton.width + (ITEM_WIDTH + MARGIN) * i;
            let top = this.top + MARGIN * 4;
            let item = this.items[(this.current + i) % this.max];
            this.itemComponents[i] = new ItemComponent(left, top, ITEM_WIDTH, ITEM_HEIGHT, item);
        }
    }
    /**
     * 推薦スロットに推薦リストをセットする。
     * @param description   説明文
     * @param reclist       推薦リスト
     */
    setRecList(description, reclist) {
        this.description = description;
        this.max = reclist.length;

        // 推薦リストに含まれるアイテム配列
        this.items = new Array(this.max);
        for (let i = 0; i < this.max; i++) {
            let item = reclist[i].item;
            let score = reclist[i].score;
            this.items[i] = new Item(item.item_id, item.name, item.red, item.white, item.shining, score);
        }

        this.setItems();
    }
    /**
     * スロットの表示位置を一つ進める。
     */
    next() {
        this.current += 1;
        if (this.current >= this.max) {
            this.current = 0;
        }
        this.setItems();
    }
    /**
     * スロットの表示位置を一つ戻す。
     */
    prev() {
        this.current -= 1;
        if (this.current < 0) {
            this.current = this.max - 1;
        }
        this.setItems();
    }
    /**
     * 点(x, y)上のアイテムを取得する。
     * @param x x座標
     * @param y y座標
     * @return  アイテム
     */
    getItemOn(x, y) {
        if (super.isWithin(x, y) == false) return null;

        for (let i = 0; i < this.size; i++) {
            if (this.itemComponents[i] == null) continue;
            if (this.itemComponents[i].isWithin(x, y)) {
                return this.itemComponents[i];
            }
        }
        return null;
    }
}