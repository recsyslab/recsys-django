/**
 * 「次へ」ボタンクラス
 */
class NextButton extends Component {
    /**
     * @param direction 矢印の向き
     */
    constructor(left, top, width, height, direction) {
        super(left, top, width, height);

        this.direction = direction;     // 矢印の向き
    }
    /**
     * @override
     */
    draw(context) {
        // ボタン枠
        context.save();
        context.fillStyle = this.isActive == true ? '#C0C0C0' : '#E0E0E0';
        context.fillRect(this.left, this.top, this.width, this.height);
        context.restore();

        // 矢印
        context.save();
        context.strokeStyle = '#434343';
        context.lineWidth = 4;
        context.beginPath();
        context.moveTo(this.left + this.width / 2 - 5 * this.direction, this.top + this.height / 2 - 10);
        context.lineTo(this.left + this.width / 2 + 5 * this.direction, this.top + this.height / 2);
        context.lineTo(this.left + this.width / 2 - 5 * this.direction, this.top + this.height / 2 + 10);
        context.stroke();
        context.restore();
    }
}