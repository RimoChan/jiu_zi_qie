var a;
a=new QWebChannel(qt.webChannelTransport, function (channel) {
	window.handler = channel.objects.handler;;
	send=function(str){window.handler.rec(str);};
});

test_mode=0;
單詞表名=0;
背景=0;

$(function(){
    setTimeout(function(){send('初始化')}, 300);
})

function 准备(){
	for(var i in 背景){
        var i=背景[i]
        var t=$("<div>")
        t.html(i['字'])
        t.addClass('背景詞')
        t.css('top',i['top'])
        t.css('left',i['left'])
        t.css('opacity',i['透明度'])
        t.css('font_size',i['字號'])
        $('#背景').append(t)
        t.fadeIn(3000)
    }    
    $("#單詞表名").html(單詞表名)
    send('go')
}


var data,pos;
function set_data(rec_data){
	data= rec_data
	pos = Math.ceil(Math.random() * 4)
	//alert(JSON.stringify(data))
	for(i=1;i<=4;i++){
		if(i<pos){
			$('#'+i).html(data[String(i-1)]['中文']);
			$('#c'+i).html(data[String(i-1)]['寫法'])
		}
		if(i==pos)
			$('#'+i).html(data['正解']['中文']);
		if(i>pos){
			$('#'+i).html(data[String(i-2)]['中文']);
			$('#c'+i).html(data[String(i-2)]['寫法'])
		}
	}
	$('#单词').html(data['正解']['假名']);
	
	$('#单词').fadeIn(600);
	$('#認識').slideDown(500);
}

function select(x){
	if(x==pos){
		回收()
		清屏更新()
	} else {
        $('#c'+x).stop()
        $('#c'+x).stop()
		$('#c'+x).fadeIn(300)
		$('#c'+x).fadeOut(1500)
	}
}

function 更新切数(all_kiri){
	$('#切数').html(all_kiri);
}
function know(){
	$('#認識').fadeOut(300);
	$('#選擇單詞').fadeIn(300);
}
function not_know(){
	回收(false);
	if(test_mode)
		清屏更新(0);
	else
		清屏更新(1000);
}
function 回收(pass=true){
		$('.完成').hide(250);
		pre_data=data
		setTimeout(function(){
								$('#上个单词').html(pre_data['正解']['假名']);
								$('#上个拼写').html(pre_data['正解']['寫法']);
								if(pre_data['正解']['詞性'])
									$('#上个词性').html('【'+pre_data['正解']['詞性']+'】');
								$('#上个解释').html(pre_data['正解']['中文']);
								$('#上个例句').html(pre_data['例句']);
								if(pass)
									$('#kiri').show(0)
								else 
									$('#kiri').hide(0)
								$('.完成').show(200)
								}
		, 250);
}
function 清屏更新(delay=0){
	$('#選擇單詞').slideUp(150);
	$('#单词').fadeOut(150);
	setTimeout(function(){send('go')}, delay+150);
}

function kiri(){
	send('切');
	$('.完成').hide(250);
}