/* pythonで作ったプログラムと同期させる */
/* 動作検証するため、LEDを左ボタンで点灯させる */
webiopi().ready(function() {
	/*散水and首ふり開始信号を出す*/
	var Run_it = webiopi().createButton("Run_it", "RUN", function(){
		webiopi().callMacro("run");
	});
	/*散水and首ふり停止を出す*/
	var Stop_it = webiopi().createButton("Stop_it", "STOP", function(){
		webiopi().callMacro("stop");
	});
	/*オフセット機能*/
	/*原点復帰*/
	var Defalut = webiopi().createButton("Defalut", "初期位置", function(){
		webiopi().callMacro("defPosition");
	});
	/*-10°*/
	var CCW_ten = webiopi().createButton("CCW_ten", "-10°", function(){
		webiopi().callMacro("CCW10");
	});
	/*-5°*/
	var CCW_fiv = webiopi().createButton("CCW_fiv", "-5°", function(){
		webiopi().callMacro("CCW5");
	});
	/*-1°*/
	var CCW_one = webiopi().createButton("CCW_one", "-1°", function(){
		webiopi().callMacro("CCW1");
	});
	/*+1°*/
	var CW_one = webiopi().createButton("CW_one", "+1°", function(){
		webiopi().callMacro("CW1");
	});
	/*+5°*/
	var CW_fiv = webiopi().createButton("CW_fiv", "+5°", function(){
		webiopi().callMacro("CW5");
	});
	/*+10°*/
	var CW_ten = webiopi().createButton("CW_ten", "+10°", function(){
		webiopi().callMacro("CW10");
	});

	$("#pos0").append(Defalut);
	$("#ccw10").append(CCW_ten);
	$("#ccw5").append(CCW_fiv);
	$("#ccw1").append(CCW_one);
	$("#cw1").append(CW_one);
	$("#cw5").append(CW_fiv);
	$("#cw10").append(CW_ten);
	
	$("#RUN").append(Run_it);
	$("#STOP").append(Stop_it);
});