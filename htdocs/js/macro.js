function run(){
	webiopi().callMacro("Do");
}
function pause(){
	webiopi().callMacro("Pause");
}
function stop(){
	webiopi().callMacro("End");
}
//水平
function T_offsetAngle_n10(){
	webiopi().callMacro("onChangeAnglePan",-10);
}
function T_offsetAngle_n5(){
	webiopi().callMacro("onChangeAnglePan",-5);
}
function T_offsetAngle_n1(){
	webiopi().callMacro("onChangeAnglePan",-1);
}
/*function T_offsetAngle_0(){
	webiopi().callMacro("onChangeAngleTilt",0);
}*/
function T_offsetAngle_p1(){
	webiopi().callMacro("onChangeAnglePan",1);
}
function T_offsetAngle_p5(){
	webiopi().callMacro("onChangeAnglePan",5);
}
function T_offsetAngle_p10(){
	webiopi().callMacro("onChangeAnglePan",10);
}
//垂直
function P_offsetAngle_n10(){
	webiopi().callMacro("onChangeAngleTilt",-10);
}
function P_offsetAngle_n5(){
	webiopi().callMacro("onChangeAngleTilt",-5);
}
function P_offsetAngle_n1(){
	webiopi().callMacro("onChangeAngleTilt",-1);
}
/*function P_offsetAngle_0(){
	webiopi().callMacro("onChangeAnglePan",0);
}*/
function P_offsetAngle_p1(){
	webiopi().callMacro("onChangeAngleTilt",1);
}
function P_offsetAngle_p5(){
	webiopi().callMacro("onChangeAngleTilt",5);
}
function P_offsetAngle_p10(){
	webiopi().callMacro("onChangeAngleTilt",10);
}

function TimeoutFn(){
	document.getElementById("status").innerHTML = "停止";
	document.getElementById("status").style.color = "red";
}
/*実行ボタンのステータス表示*/
function btnStatus(sts){
	if(sts==0){
		document.getElementById("status").innerHTML = "実行中";
		document.getElementById("status").style.color = "#32CD32";
		setTimeout(TimeoutFn,600000);	//第一引数：コールバック関数、第二引数：時間指定（ミリ秒）
	}
	else if(sts==1){
		document.getElementById("status").innerHTML = "一時停止";
		document.getElementById("status").style.color = "red";
	}
	else if(sts==2){
		document.getElementById("status").innerHTML = "停止";
		document.getElementById("status").style.color = "red";
	}
}
/*数値の計算*/
//垂直
Total1 = 0;
Work1 = 0;
MaxVal1 = 40;
MinVal1 = -40;
function buttonValue1(value){
	Work1 = Total1+value;
	Total1 = eval(Work1);
	if(Total1>MaxVal1){
		document.myForm1.myLine1.value = MaxVal1;
		Total1 = MaxVal1;
	}
	else if(Total1<MinVal1){
		document.myForm1.myLine1.value = MinVal1;
		Total1 = MinVal1;
	}
	else{
		document.myForm1.myLine1.value = Total1
	}
}
function clearValue1(){
	Total1 = 0;
	Work1 = 0;
	document.myForm1.myLine1.value = Total1;
}
//水平
Total2 = 0;
Work2 = 0;
MaxVal2 = 40;
MinVal2 = -40;
function buttonValue2(value){
	Work2 = Total2+value;
	Total2 = eval(Work2);
	if(Total2>MaxVal2){
		document.myForm2.myLine2.value = MaxVal2;
		Total2 = MaxVal2;
	}
	else if(Total2<MinVal2){
		document.myForm2.myLine2.value = MinVal2;
		Total2 = MinVal2;
	}
	else{
		document.myForm2.myLine2.value = Total2
	}
}
function clearValue2(){
	Total2 = 0;
	Work2 = 0;
	document.myForm2.myLine2.value = Total2;
}