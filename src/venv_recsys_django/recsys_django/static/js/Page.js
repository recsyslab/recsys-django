/**
 * ページクラス
 */
class Page {
    /**
     * @param canvas    キャンバス要素
     * @param context   描画コンテキスト
     */
    constructor(canvas, context) {
        this.canvas = canvas;
        this.context = context;
    }
    /*
     * ページのクリックイベント
     * @param x x座標
     * @param y y座標
     */
    onClick(x, y) {
    }
    /*
     * ページのマウス移動イベント
     * @param x x座標
     * @param y y座標
     */
    onMouseMove(x, y) {
    }
    /*
     * ページの描画
     */
    draw() {
    }
}