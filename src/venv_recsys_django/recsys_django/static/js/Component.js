/**
 * コンポーネントクラス
 */
class Component {
    /**
     * @param left      コンポーネントの左端のx座標
     * @param top       コンポーネントの上端のy座標
     * @param width     コンポーネントの幅
     * @param height    コンポーネントの高さ
     */
    constructor(left, top, width, height) {
        this.left = left;           // コンポーネントの左端のx座標
        this.top = top;             // コンポーネントの上端のx座標
        this.width = width;         // コンポーネントの幅
        this.height = height;       // コンポーネントの高さ

        this.isActive = false;      // コンポーネントがアクティブか
    }
    /**
     * x, y座標がコンポーネントの範囲内か判定する。
     * @param x x座標
     * @param y y座標
     * @return  範囲内であればtrue、範囲外であればfalseを返す。
     */
    isWithin(x, y) {
        if (x < this.left || this.left + this.width < x) return false;
        if (y < this.top || this.top + this.height < y) return false;
        return true;
    }
    /**
     * コンポーネントを描画する。
     * @param context   描画コンテキスト
     */
    draw(context) {
    }
}