/**
 * 「戻る」ボタンクラス
 */
class ReturnButton extends Component {
    /**
     *
     */
    constructor(left, top, width, height) {
        super(left, top, width, height);
    }
    /**
     * @override
     */
    draw(context) {
        context.save();
        if (this.isActive) {
            context.drawImage(returnImage, this.left - MARGIN / 2, this.top - MARGIN / 2, this.width + MARGIN, this.height + MARGIN);
        } else {
            context.drawImage(returnImage, this.left, this.top, this.width, this.height);
        }
        context.restore();
    }
}