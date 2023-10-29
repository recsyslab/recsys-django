/**
 * アイテム詳細コンポーネントクラス
 */
class ItemDetailComponent extends Component {
    /**
     * @param item  対象アイテム
     */
    constructor(left, top, width, height, item) {
        super(left, top, width, height);

        this.item = item;       // 対象アイテム

        // 星評価
        this.starRating = new StarRating(this.left + this.width, this.top + 98, DETAIL_STAR_WIDTH * MAX_RATING, DETAIL_STAR_WIDTH, MAX_RATING);
    }
    /**
     * @override
     */
    draw(context) {
        // アイテム枠
        context.save();
        context.fillStyle = '#E0FFEF';
        context.fillRect(this.left, this.top, this.width, this.height);
        context.restore();

        // アイテム画像
        context.save();
        let scale = this.width / this.item.image.width;
        let w = this.width;
        let h = this.item.image.height * scale;
        context.drawImage(this.item.image, this.left, this.top, w, h);
        context.restore();

        // アイテム名
        context.save();
        context.font = '42px メイリオ';
        context.fillStyle = '#434343';
        context.strokeStyle = '#434343';
        context.textBaseline = 'top';
        context.textAlign = 'left';
        context.fillText(this.item.name, this.left + this.width, this.top);
        context.strokeText(this.item.name, this.left + this.width, this.top);
        context.restore();

        // アイテムのカテゴリ
        context.save();
        context.font = '36px メイリオ';
        context.fillStyle = '#838383';
        context.strokeStyle = '#838383';
        context.textBaseline = 'top';
        context.textAlign = 'left';
        let category = null;
        category = this.item.red == 1 ? '赤身' : category;
        category = this.item.white == 1 ? '白身' : category;
        category = this.item.shining == 1 ? '光物' : category;
        context.fillText(category, this.left + this.width, this.top + 52);
        context.strokeText(category, this.left + this.width, this.top + 52);
        context.restore();

        // 星評価
        this.starRating.draw(context);
    }
}