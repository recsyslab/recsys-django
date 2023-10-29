/**
 * 星クラス
 */
class Star extends Component {
    /**
     *
     */
    constructor(left, top, width, height) {
        super(left, top, width, height);

        this.isTempActive = false;      // 暫定選択中であるか
    }
    /**
     * @override
     */
    draw(context) {
        context.save();
        let star = this.isTempActive ? 2 : (this.isActive ? 1 : 0);
        context.drawImage(starImages[star], this.left, this.top, this.width, this.height);
        context.restore();
    }
}