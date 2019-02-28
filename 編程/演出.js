(function(){
"use strict";
function ՐՏ_extends(child, parent) {
    child.prototype = Object.create(parent.prototype);
    child.prototype.__base__ = parent;
    child.prototype.constructor = child;
}
function ՐՏ_in(val, arr) {
    if (typeof arr.indexOf === "function") {
        return arr.indexOf(val) !== -1;
    } else if (typeof arr.has === "function") {
        return arr.has(val);
    }
    return arr.hasOwnProperty(val);
}
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
function len(obj) {
    var tmp;
    if (obj.constructor === [].constructor || obj.constructor === "".constructor || (tmp = Array.prototype.slice.call(obj)).length) {
        return (tmp || obj).length;
    }
    if (Set && obj.constructor === Set) {
        return obj.size;
    }
    return Object.keys(obj).length;
}
function max(a) {
    return Math.max.apply(null, Array.isArray(a) ? a : arguments);
}
function min(a) {
    return Math.min.apply(null, Array.isArray(a) ? a : arguments);
}
function ՐՏ_print() {
    if (typeof console === "object") {
        console.log.apply(console, arguments);
    }
}
function range(start, stop, step) {
    var length, idx, range;
    if (arguments.length <= 1) {
        stop = start || 0;
        start = 0;
    }
    step = arguments[2] || 1;
    length = Math.max(Math.ceil((stop - start) / step), 0);
    idx = 0;
    range = new Array(length);
    while (idx < length) {
        range[idx++] = start;
        start += step;
    }
    return range;
}
function sum(arr, start=0) {
    return arr.reduce(function(prev, cur) {
        return prev + cur;
    }, start);
}
function ՐՏ_type(obj) {
    return obj && obj.constructor && obj.constructor.name ? obj.constructor.name : Object.prototype.toString.call(obj).slice(8, -1);
}
function ՐՏ_eq(a, b) {
    var ՐՏitr6, ՐՏidx6;
    var i;
    if (a === b) {
        return true;
    }
    if (a.constructor !== b.constructor) {
        return false;
    }
    if (Array.isArray(a)) {
        if (a.length !== b.length) {
            return false;
        }
        for (i = 0; i < a.length; i++) {
            if (!ՐՏ_eq(a[i], b[i])) {
                return false;
            }
        }
        return true;
    } else if (a.constructor === Object) {
        if (Object.keys(a).length !== Object.keys(b).length) {
            return false;
        }
        ՐՏitr6 = ՐՏ_Iterable(a);
        for (ՐՏidx6 = 0; ՐՏidx6 < ՐՏitr6.length; ՐՏidx6++) {
            i = ՐՏitr6[ՐՏidx6];
            if (!ՐՏ_eq(a[i], b[i])) {
                return false;
            }
        }
        return true;
    } else if (Set && a.constructor === Set || Map && a.constructor === Map) {
        if (a.size !== b.size) {
            return false;
        }
        for (i of a) {
            if (!b.has(i)) {
                return false;
            }
        }
        return true;
    } else if (a.constructor === Date) {
        return a.getTime() === b.getTime();
    } else if (typeof a.__eq__ === "function") {
        return a.__eq__(b);
    }
    return false;
}
class IndexError extends Error {
    constructor (message) {
        super();
        var self = this;
        self.name = "IndexError";
        self.message = message;
    }
}
class TypeError extends Error {
    constructor (message) {
        super();
        var self = this;
        self.name = "TypeError";
        self.message = message;
    }
}
var ՐՏ_modules = {};
ՐՏ_modules["random"] = {};
ՐՏ_modules["re"] = {};
ՐՏ_modules["配置"] = {};
ՐՏ_modules["數據"] = {};

(function(){
    var __name__ = "random";
    var _$rapyd$_seed_state, _$rapyd$_get_random_byte;
    _$rapyd$_seed_state = {
        key: [],
        key_i: 0,
        key_j: 0
    };
    _$rapyd$_get_random_byte = function() {
        _$rapyd$_seed_state.key_i = (_$rapyd$_seed_state.key_i + 1) % 256;
        _$rapyd$_seed_state.key_j = (_$rapyd$_seed_state.key_j + _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i]) % 256;
        [_$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i], _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_j]] = [ _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_j], _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i] ];
        return _$rapyd$_seed_state.key[(_$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i] + _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_j]) % 256];
    };
    function seed(x=new Date().getTime()) {
        var i, j;
        if (typeof x === "number") {
            x = x.toString();
        } else if (typeof x !== "string") {
            throw new TypeError("unhashable type: '" + typeof x + "'");
        }
        for (i = 0; i < 256; i++) {
            _$rapyd$_seed_state.key[i] = i;
        }
        j = 0;
        for (i = 0; i < 256; i++) {
            j = (j + _$rapyd$_seed_state.key[i] + x.charCodeAt(i % x.length)) % 256;
            [_$rapyd$_seed_state.key[i], _$rapyd$_seed_state.key[j]] = [ _$rapyd$_seed_state.key[j], _$rapyd$_seed_state.key[i] ];
        }
    }
    seed();
    function random() {
        var n, m, i;
        n = 0;
        m = 1;
        for (i = 0; i < 8; i++) {
            n += _$rapyd$_get_random_byte() * m;
            m *= 256;
        }
        return n / 0x10000000000000000;
    }
    function randrange() {
        return choice(range.apply(this, arguments));
    }
    function randint(a, b) {
        return parseInt(random() * (b - a + 1) + a);
    }
    function uniform(a, b) {
        return random() * (b - a) + a;
    }
    function choice(seq) {
        if (seq.length > 0) {
            return seq[Math.floor(random() * seq.length)];
        } else {
            throw new IndexError();
        }
    }
    function shuffle(x, random_f=random) {
        var i, j;
        for (i = 0; i < x.length; i++) {
            j = Math.floor(random_f() * (i + 1));
            [x[i], x[j]] = [ x[j], x[i] ];
        }
        return x;
    }
    function sample(population, k) {
        var ՐՏitr1, ՐՏidx1;
        var x, i, j;
        x = population.slice();
        ՐՏitr1 = ՐՏ_Iterable(range(population.length - 1, population.length - k - 1, -1));
        for (ՐՏidx1 = 0; ՐՏidx1 < ՐՏitr1.length; ՐՏidx1++) {
            i = ՐՏitr1[ՐՏidx1];
            j = Math.floor(random() * (i + 1));
            [x[i], x[j]] = [ x[j], x[i] ];
        }
        return x.slice(population.length - k);
    }
    ՐՏ_modules["random"]["_$rapyd$_seed_state"] = _$rapyd$_seed_state;

    ՐՏ_modules["random"]["_$rapyd$_get_random_byte"] = _$rapyd$_get_random_byte;

    ՐՏ_modules["random"]["seed"] = seed;

    ՐՏ_modules["random"]["random"] = random;

    ՐՏ_modules["random"]["randrange"] = randrange;

    ՐՏ_modules["random"]["randint"] = randint;

    ՐՏ_modules["random"]["uniform"] = uniform;

    ՐՏ_modules["random"]["choice"] = choice;

    ՐՏ_modules["random"]["shuffle"] = shuffle;

    ՐՏ_modules["random"]["sample"] = sample;
})();

(function(){
    var __name__ = "re";
    var IGNORECASE, I, MULTILINE, M, DOTALL, D;
    I = IGNORECASE = 1;
    M = MULTILINE = 2;
    D = DOTALL = 4;
    class MatchObject {
        constructor (regex, match) {
            var self = this;
            var offset, remainder, i, loc;
            self.re = regex;
            self.string = match.input;
            self._groups = match;
            self._start = [];
            self._end = [];
            offset = 0;
            remainder = match.input;
            i = 0;
            while (typeof match[i] !== "undefined") {
                loc = remainder.search(match[i]);
                self._start.push(loc + offset);
                self._end.push(loc + offset + match[i].length - 1);
                remainder = remainder.slice(loc);
                ++i;
            }
        }
        groups () {
            var self = this;
            return self._groups.slice(0);
        }
        group (g=0) {
            var self = this;
            return self._groups[g];
        }
        start (g=0) {
            var self = this;
            return self._start[g];
        }
        end (g=0) {
            var self = this;
            return self._end[g];
        }
    }
    class RegexObject {
        constructor (pattern, flags) {
            var self = this;
            var modifiers;
            if (pattern instanceof RegexObject) {
                self.pattern = pattern.pattern;
                self.flags = pattern.flags | flags;
            } else {
                self.pattern = pattern;
                self.flags = flags;
            }
            modifiers = "";
            if (self.flags & IGNORECASE) {
                modifiers += "i";
            }
            if (self.flags & MULTILINE) {
                modifiers += "m";
            }
            if (self.flags & DOTALL) {
                pattern = pattern.replace(new RegExp("\\.", "g"), "[\\s\\S]");
            }
            self._modifiers = modifiers;
            self._pattern = new RegExp(pattern, modifiers);
        }
        search (string) {
            var self = this;
            var n;
            n = string.match(self._pattern);
            if (n === null) {
                return null;
            }
            return new MatchObject(self, n);
        }
        match (string) {
            var self = this;
            var n;
            n = string.match(new RegExp("^" + self.pattern, self._modifiers));
            if (n === null) {
                return null;
            }
            return new MatchObject(self, n);
        }
        split (string, maxsplit=null) {
            var self = this;
            if (maxsplit !== null) {
                return string.split(self._pattern, maxsplit);
            } else {
                return string.split(self._pattern);
            }
        }
        findall (string) {
            var self = this;
            var matches, i, ret;
            matches = string.match(new RegExp(self.pattern, self._modifiers + "g"));
            i = 0;
            ret = [];
            while (typeof matches[i] !== "undefined") {
                ret.push(matches[i]);
                ++i;
            }
            return ret;
        }
        sub (repl, string, count=0) {
            var self = this;
            var i;
            if (count === 0) {
                return string.replace(new RegExp(self.pattern, self._modifiers + "g"), repl);
            }
            for (i = 0; i < count; i++) {
                string = string.replace(self._pattern, repl);
            }
            return string;
        }
        subn (repl, string, count=0) {
            var self = this;
            var n, new_string;
            n = 0;
            if (count === 0) {
                count = Number.MAX_VALUE;
            }
            new_string = string;
            do {
                string = new_string;
                new_string = string.replace(self._pattern, repl);
                if ((new_string !== string && (typeof new_string !== "object" || !ՐՏ_eq(new_string, string)))) {
                    ++n;
                    --count;
                }
            } while ((new_string !== string && (typeof new_string !== "object" || !ՐՏ_eq(new_string, string))) && count > 0);
            return [string, n];
        }
    }
    function compile(pattern, flags=0) {
        return new RegexObject(pattern, flags);
    }
    function search(pattern, string, flags=0) {
        return new RegexObject(pattern, flags).search(string);
    }
    function match(pattern, string, flags=0) {
        return new RegexObject(pattern, flags).match(string);
    }
    function split(pattern, string, maxsplit=0, flags=0) {
        return new RegexObject(pattern, flags).split(string);
    }
    function findall(pattern, string, flags=0) {
        return new RegexObject(pattern, flags).findall(string);
    }
    function sub(pattern, repl, string, count=0, flags=0) {
        return new RegexObject(pattern, flags).sub(repl, string, count);
    }
    function subn(pattern, repl, string, count=0, flags=0) {
        return new RegexObject(pattern, flags).subn(repl, string, count);
    }
    ՐՏ_modules["re"]["IGNORECASE"] = IGNORECASE;

    ՐՏ_modules["re"]["I"] = I;

    ՐՏ_modules["re"]["MULTILINE"] = MULTILINE;

    ՐՏ_modules["re"]["M"] = M;

    ՐՏ_modules["re"]["DOTALL"] = DOTALL;

    ՐՏ_modules["re"]["D"] = D;

    ՐՏ_modules["re"]["MatchObject"] = MatchObject;

    ՐՏ_modules["re"]["RegexObject"] = RegexObject;

    ՐՏ_modules["re"]["compile"] = compile;

    ՐՏ_modules["re"]["search"] = search;

    ՐՏ_modules["re"]["match"] = match;

    ՐՏ_modules["re"]["split"] = split;

    ՐՏ_modules["re"]["findall"] = findall;

    ՐՏ_modules["re"]["sub"] = sub;

    ՐՏ_modules["re"]["subn"] = subn;
})();

(function(){
    var __name__ = "配置";
    var 確率調整, 確率範圍, 缓冲区大小, 隨機種子;
    確率調整 = .7;
    確率範圍 = [ .2, 5 ];
    缓冲区大小 = 80;
    隨機種子 = 9.1;
    ՐՏ_modules["配置"]["確率調整"] = 確率調整;

    ՐՏ_modules["配置"]["確率範圍"] = 確率範圍;

    ՐՏ_modules["配置"]["缓冲区大小"] = 缓冲区大小;

    ՐՏ_modules["配置"]["隨機種子"] = 隨機種子;
})();

(function(){
    var __name__ = "數據";
    var rd, data, i, q;
    var random = ՐՏ_modules["random"];
    
    rd = random.randint;
    var re = ՐՏ_modules["re"];
    
    var 配置 = ՐՏ_modules["配置"];
    
    function 加权抽取(li, wei) {
        var total_weight, p, i;
        total_weight = sum(wei);
        p = random.uniform(0, total_weight);
        for (i = 0; i < len(li); i++) {
            p -= wei[i];
            if (p < 0) {
                return li[i];
            }
        }
    }
    class set extends Array {
        add (x) {
            var self = this;
            self.push(x);
        }
    }
    class Data {
        constructor () {
            var ՐՏitr2, ՐՏidx2, ՐՏitr3, ՐՏidx3;
            var self = this;
            var R, x, i;
            self.單詞表 = n1單詞;
            self.例句字典 = 例句;
            R = 配置.隨機種子;
            x = 0;
            ՐՏitr2 = ՐՏ_Iterable(self.單詞表);
            for (ՐՏidx2 = 0; ՐՏidx2 < ՐՏitr2.length; ՐՏidx2++) {
                i = ՐՏitr2[ՐՏidx2];
                x += .45;
                R = (R * 1.23 + x) % 7;
                i["特徵"] = R;
            }
            function _(a, b) {
                return a["特徵"] - b["特徵"];
            }
            self.單詞表.sort(_);
            self.切過的詞 = {};
            self.緩衝區 = new set();
            self.緩衝區尾 = 0;
            self.填滿緩衝區();
            ՐՏitr3 = ՐՏ_Iterable(self.單詞表);
            for (ՐՏidx3 = 0; ՐՏidx3 < ՐՏitr3.length; ՐՏidx3++) {
                i = ՐՏitr3[ՐՏidx3];
                i["权"] = 1;
            }
        }
        填滿緩衝區 () {
            var self = this;
            while (len(self.緩衝區) < 配置.缓冲区大小 && self.緩衝區尾 < len(self.單詞表)) {
                if (!self.切過了(self.緩衝區尾)) {
                    self.緩衝區.add(self.緩衝區尾);
                }
                ++self.緩衝區尾;
            }
        }
        前切 () {
            var self = this;
            var 前詞;
            前詞 = self.單詞表[self.之前詞位置];
            self.切過的詞[前詞["假名"] + " " + 前詞["寫法"]] = 1;
            self.緩衝區.remove(self.之前詞位置);
            self.填滿緩衝區();
        }
        切詞存檔 () {
            var self = this;
            ՐՏ_print("當然不能存檔");
        }
        切詞同步 () {
            var self = this;
            ՐՏ_print("當然不能同步");
        }
        处理例句 (句) {
            var self = this;
            var pattern, a, b;
            if (ՐՏ_type(句) === "String") {
                pattern = re.compile("^.*?[^<]/");
                a = pattern.findall(句);
                if (a) {
                    a = a[0];
                } else {
                    return;
                }
                b = 句.slice(len(a), -1);
                句 = [ "", "" ];
                句[0] = a.slice(0, -1);
                句[1] = b;
            }
            if (ՐՏ_type(句) === "Array") {
                return 句[0] + '<br/><span class="例句中文">' + 句[1] + "</span>";
            }
        }
        生成問題 () {
            var ՐՏ_1, ՐՏ_2;
            var self = this;
            var 組, li, i, the_spell, 例句;
            組 = {};
            try {
                self.之前詞位置 = self.當前詞位置;
            } catch (ՐՏ_Exception) {
                self.之前詞位置 = -1;
            }
            while (true) {
                li = self.緩衝區;
                self.當前詞位置 = 加权抽取(li, (function() {
                    var ՐՏidx4, ՐՏitr4 = ՐՏ_Iterable(li), ՐՏres = [], i;
                    for (ՐՏidx4 = 0; ՐՏidx4 < ՐՏitr4.length; ՐՏidx4++) {
                        i = ՐՏitr4[ՐՏidx4];
                        ՐՏres.push(self.單詞表[i]["权"]);
                    }
                    return ՐՏres;
                })());
                if (len(self.緩衝區) === 1) {
                    break;
                }
                if (((ՐՏ_1 = self.當前詞位置) !== (ՐՏ_2 = self.之前詞位置) && (typeof ՐՏ_1 !== "object" || !ՐՏ_eq(ՐՏ_1, ՐՏ_2)))) {
                    break;
                }
            }
            self.單詞表[self.當前詞位置]["权"] *= 配置.確率調整;
            self.單詞表[self.當前詞位置]["权"] = min(max(self.單詞表[self.當前詞位置]["权"], 配置.確率範圍[0]), 配置.確率範圍[1]);
            組["正解"] = self.單詞表[self.當前詞位置];
            the_spell = 組["正解"]["寫法"];
            if (ՐՏ_in(the_spell, self.例句字典) && len(self.例句字典[the_spell]) > 0) {
                例句 = self.处理例句(random.choice(self.例句字典[the_spell]));
            } else {
                例句 = "没抓到2333";
            }
            組["例句"] = 例句;
            for (i = 0; i < 3; i++) {
                組[i] = self.單詞表[rd(0, len(self.單詞表) - 1)];
            }
            return 組;
        }
        生成背景詞 () {
            var ՐՏitr5, ՐՏidx5;
            var self = this;
            var 詞列, s, i;
            詞列 = [];
            s = new set();
            for (i = 1; i < 100; i++) {
                s.add(rd(0, len(self.單詞表) - 1));
            }
            ՐՏitr5 = ՐՏ_Iterable(s);
            for (ՐՏidx5 = 0; ՐՏidx5 < ՐՏitr5.length; ՐՏidx5++) {
                i = ՐՏitr5[ՐՏidx5];
                詞列.append({
                    "字": self.單詞表[i]["寫法"],
                    "top": rd(-100, 800),
                    "left": rd(-100, 1400),
                    "透明度": rd(5, 20) / 100,
                    "字號": rd(13, 30)
                });
            }
            return 詞列;
        }
        切過了 (x) {
            var self = this;
            return ՐՏ_in(self.單詞表[x]["假名"] + " " + self.單詞表[x]["寫法"], self.切過的詞);
        }
    }
    if (__name__ === "__main__") {
        data = new Data();
        ՐՏ_print(data.單詞表[1]);
        for (i = 0; i < 160; i++) {
            q = data.生成問題();
            if (i % 100 === 99) {
                ՐՏ_print("已经处理", i, "个。");
            }
        }
    }
    ՐՏ_modules["數據"]["rd"] = rd;

    ՐՏ_modules["數據"]["data"] = data;

    ՐՏ_modules["數據"]["i"] = i;

    ՐՏ_modules["數據"]["q"] = q;

    ՐՏ_modules["數據"]["加权抽取"] = 加权抽取;

    ՐՏ_modules["數據"]["set"] = set;

    ՐՏ_modules["數據"]["Data"] = Data;
})();

(function(){

    var __name__ = "__main__";

    var j, a;
    var random = ՐՏ_modules["random"];
    
    var 數據 = ՐՏ_modules["數據"];
    
    ՐՏ_print("你好！");
    j = new Proxy({}, {
        "get": function f(target, name) {
            return $("#" + name);
        }
    });
    class 演出 {
        constructor () {
            var self = this;
            self.正解位置 = null;
            self.問題 = null;
            self.data = null;
            self.t = 0;
        }
        回收 () {
            var self = this;
            j.上板.fadeOut(200);
            setTimeout(function f() {
                j.中文.html(self.問題.正解.中文);
                j.假名.html(self.問題.正解.假名);
                j.寫法.html(self.問題.正解.寫法);
                j.詞性.html(self.問題.正解.詞性);
                j.例句.html(self.問題.例句);
                j.上板.fadeIn();
            }, 200);
            j.單詞.fadeOut(500);
            j.意思.fadeOut(500);
            setTimeout(function() {
                self.出題();
            }, 500);
        }
        出題 () {
            var self = this;
            var i;
            j.自覺.fadeIn(300);
            j.單詞.fadeIn(500);
            self.問題 = self.data.生成問題();
            self.正解位置 = random.randint(0, 3);
            for (i = 0; i < self.正解位置; i++) {
                $("#" + i + " .選項").html(self.問題[i].中文);
            }
            for (i = self.正解位置 + 1; i < 4; i++) {
                $("#" + i + " .選項").html(self.問題[i - 1].中文);
            }
            $("#" + self.正解位置 + " .選項").html(self.問題.正解.中文);
            j.單詞.html(self.問題.正解.假名);
            ՐՏ_print(self);
        }
        選擇 (x) {
            var ՐՏ_3;
            var self = this;
            if ((x === (ՐՏ_3 = self.正解位置) || typeof x === "object" && ՐՏ_eq(x, ՐՏ_3))) {
                self.回收();
            }
        }
        加載 () {
            var self = this;
            self.data = new 數據.Data();
            self.出題();
            ՐՏ_print("加載好了");
        }
        初始化 (x) {
            var self = this;
            ՐՏ_print("初始化");
            $.getScript("./編程/數據/例句.js", function f() {
                ++self.t;
                if (self.t === 2) {
                    self.加載();
                }
            });
            $.getScript("./編程/數據/n1單詞.js", function f() {
                ++self.t;
                if (self.t === 2) {
                    self.加載();
                }
            });
            j.上板.hide(0);
            j.意思.hide(0);
            $("#意思 .選項按鈕").click(function(x) {
                self.選擇(parseInt(x.currentTarget.id));
            });
            $("#認識").click(function(x) {
                j.自覺.fadeOut(100);
                setTimeout(function f() {
                    j.意思.fadeIn(200);
                }, 100);
                self.選擇(parseInt(x.currentTarget.id));
            });
            $("#不認識").click(function(x) {
                j.自覺.fadeOut(100);
                self.回收();
            });
        }
    }
    a = new 演出();
    function _() {
        a.初始化();
    }
    $(_);
})();
})();
