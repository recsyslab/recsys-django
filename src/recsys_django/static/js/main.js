/**
 * **** **** **** **** **** **** **** ****
 * 定数
 * **** **** **** **** **** **** **** ****
 */
MARGIN = 10;

ITEM_COUNT = 9;
ITEM_WIDTH = 200;
ITEM_HEIGHT = 200;

NEXT_BUTTON_WIDTH = 40;
NEXT_BUTTON_HEIGHT = ITEM_HEIGHT;

SLOT_SIZE = 3;
SLOT_WIDTH = NEXT_BUTTON_WIDTH + MARGIN + (ITEM_WIDTH + MARGIN) * SLOT_SIZE + NEXT_BUTTON_WIDTH;
SLOT_HEIGHT = MARGIN * 4 + ITEM_HEIGHT;

MAIN_SLOT_COUNT = 3;
MAIN_SLOT_LEFT = 0;
MAIN_SLOT_TOP = 0;
MAIN_SLOT_RANDOM = 0;
MAIN_SLOT_POPULARITY = 1;
MAIN_SLOT_ITEMCF = 2;

MAX_RATING = 5;

DETAIL_ENLARGE = 1.5;

DETAIL_ITEM_LEFT = 0;
DETAIL_ITEM_TOP = 0;
DETAIL_ITEM_WIDTH = ITEM_WIDTH * DETAIL_ENLARGE;
DETAIL_ITEM_HEIGHT = ITEM_HEIGHT * DETAIL_ENLARGE;

DETAIL_SLOT_LEFT = 0;
DETAIL_SLOT_TOP = DETAIL_ITEM_TOP + DETAIL_ITEM_HEIGHT + MARGIN;

DETAIL_STAR_WIDTH = 32;

DETAIL_RETURN_WIDTH = 64;
DETAIL_RETURN_LEFT = SLOT_WIDTH - DETAIL_RETURN_WIDTH - MARGIN / 2;
DETAIL_RETURN_TOP = DETAIL_SLOT_TOP + SLOT_HEIGHT + MARGIN;
/**
 * **** **** **** **** **** **** **** ****
 * グローバル変数
 * **** **** **** **** **** **** **** ****
 */
// ページ
let currentPage = null;         // 現在のページ
let mainPage = null;            // メインページ
let detailPage = null;          // 詳細ページ

// Imageオブジェクト
let returnImage = null;         // 「戻る」ボタン画像
let starImages = null;          // 星画像配列
/**
 * **** **** **** **** **** **** **** ****
 * 初期化処理
 * **** **** **** **** **** **** **** ****
 */
/**
 * ページ読込み
 */
$(function() {
    // 全体の初期化処理
    init();
});
/**
 * 全体の初期化処理
 */
function init() {
    // キャンバス要素の取得
    let canvas = $('#main_canvas').get(0);
    // 描画コンテキストの取得
    let context = canvas.getContext("2d");

    // イベントリスナの追加
    canvas.addEventListener('click', onCanvasClick, false);
    canvas.addEventListener('mousemove', onCanvasMouseMove, false);

    // Imageオブジェクトの生成
    returnImage = new Image();
    returnImage.src = returnSrc;
    returnImage.onload = function() {
        console.log(returnImage.src + " : load completed");
    }
    starImages = new Array();
    for (let i = 0; i < starSrcs.length; i++) {
        starImages[i] = new Image();
        starImages[i].src = starSrcs[i];
        starImages[i].onload = function() {
            console.log(starImages[i].src + " : load completed");
        }
    }

    // ページの生成
    mainPage = new MainPage(canvas, context);
    detailPage = new DetailPage(canvas, context);

    // データの初期化
    initData();
}
/**
 * データの初期化
 */
function initData() {
    currentPage = mainPage;

    // 各推薦リストの取得
    mainPage.getRandomRecommendations();
    mainPage.getPopularityBasedRecommendations();
    mainPage.getItemcfBasedRecommendations();

    currentPage.draw();
}
/**
 * **** **** **** **** **** **** **** ****
 * ビュー関連
 * **** **** **** **** **** **** **** ****
 */
/**
 * ウィンドウ座標からキャンバス座標に変換する。
 * @param canvas    キャンバス要素
 * @param wx        ウィンドウ上のx座標
 * @param wy        ウィンドウ上のy座標
 * @return          キャンバス座標
 */
function windowToCanvas(canvas, wx, wy) {
	let bbox = canvas.getBoundingClientRect();
	return {
		x: (wx - bbox.left) * (canvas.width / bbox.width),
		y: (wy - bbox.top)  * (canvas.height / bbox.height)
	};
}
/**
 * キャンバスへのマウスクリック
 */
function onCanvasClick(e) {
    let loc = windowToCanvas(currentPage.canvas, e.clientX, e.clientY);

    if (currentPage == null) return;
    currentPage.onClick(loc.x, loc.y);
    currentPage.draw();
}
/**
 * キャンバス上のマウス移動
 */
function onCanvasMouseMove(e) {
    let loc = windowToCanvas(currentPage.canvas, e.clientX, e.clientY);

    currentPage.canvas.style = 'cursor: default';

    if (currentPage == null) return;
    currentPage.onMouseMove(loc.x, loc.y);
    currentPage.draw();
}