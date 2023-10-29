/**
 * 星評価クラス
 */
class StarRating extends Component {
    /**
     * @param maxRating 最大評価値
     */
    constructor(left, top, width, height, maxRating) {
        super(left, top, width, height);

        this.maxRating = maxRating;     // 最大評価値
        this.tempRating = -1;           // 暫定評価値

        // 星配列
        this.stars = new Array(this.maxRating);
        for (let i = 0; i < this.stars.length; i++) {
            this.stars[i] = new Star(this.left + DETAIL_STAR_WIDTH * i, this.top, DETAIL_STAR_WIDTH, DETAIL_STAR_WIDTH);
        }
    }
    /**
     * @override
     */
    draw(context) {
        context.save();
        for (let i = 0; i < this.stars.length; i++) {
            this.stars[i].draw(context);
        }
        context.restore();
    }
    /**
     * 評価値をセットする。
     * @param rating    評価値
     */
    setRating(rating) {
        this.rating = rating;
        for (let i = 0; i < this.stars.length; i++) {
            this.stars[i].isActive = i < this.rating ? true : false;
        }
    }
    /**
     * 暫定評価値をセットする。
     * @param rating    暫定評価値
     */
    setTempRating(tempRating) {
        this.tempRating = tempRating;
        for (let i = 0; i < this.stars.length; i++) {
            this.stars[i].isTempActive = i < this.tempRating ? true : false;
        }
    }
    /**
     * 暫定評価値をリセットする。
     */
    resetTempRating() {
        this.tempRating = -1;
        for (let i = 0; i < this.stars.length; i++) {
            this.stars[i].isTempActive = false;
        }
    }
    /**
     * 点(x, y)上の評価値を取得する。
     * @param x x座標
     * @param y y座標
     * @return  評価値
     */
    getRatingOn(x, y) {
        if (!this.isWithin(x, y)) return -1;
        for (let i = 0; i < this.stars.length; i++) {
            if (!this.stars[i].isWithin(x, y)) continue;
            return i + 1;
        }
    }
}