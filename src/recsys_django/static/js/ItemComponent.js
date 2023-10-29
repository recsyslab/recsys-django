/**
 * アイテムコンポーネントクラス
 */
class ItemComponent extends Component {
    /**
     * @param item      アイテム
     */
    constructor(left, top, width, height, item) {
        super(left, top, width, height);

        this.item = item;       // アイテム
    }
    /**
     * @override
     */
    draw(context) {
        // アイテム枠
        context.save();
        context.fillStyle = this.isActive == true ? '#B7FFDB' : '#E0FFEF';
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
        context.font = '28px メイリオ';
        context.fillStyle = '#434343';
        context.strokeStyle = '#434343';
        context.textBaseline = 'bottom';
        context.textAlign = 'center';
        context.fillText(this.item.name, this.left + this.width / 2, this.top + this.height);
        context.strokeText(this.item.name, this.left + this.width / 2, this.top + this.height);
        context.restore();
    }
}