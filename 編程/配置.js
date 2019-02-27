(function(){
"use strict";
function ՐՏ_Iterable(iterable) {
    var tmp;
    if (iterable.constructor === [].constructor || iterable.constructor === "".constructor || (tmp = Array.prototype.slice.call(iterable)).length) {
        return tmp || iterable;
    }
    if (Set && iterable.constructor === Set) {
        return Array.from(iterable);
    }
    return Object.keys(iterable);
}

(function(){

    var __name__ = "__main__";

    var 確率調整, 確率範圍, 缓冲区大小, 隨機種子;
    確率調整 = .7;
    確率範圍 = [ .2, 5 ];
    缓冲区大小 = 80;
    隨機種子 = 9.1;
})();
})();
