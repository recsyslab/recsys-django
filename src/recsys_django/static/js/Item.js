/**
 * アイテムクラス
 */
class Item {
    /**
     * @param id        アイテムID
     * @param name      アイテム名
     * @param score     スコア
     */
    constructor(id, name, red, white, shining, score) {
        this.id = id;           // アイテムID
        this.name = name;       // アイテム名
        this.red = red;         // 赤身
        this.white = white;     // 白身
        this.shining = shining; // 光物
        this.score = score;     // スコア

        // アイテム画像
        this.image = new Image();
        this.image.src = 'media/items/item' + ('00' + this.id).slice(-2) + '.png';
        let src = this.image.src;
        this.image.onload = function() {
            console.log(src + " : load completed");
        }
    }
}