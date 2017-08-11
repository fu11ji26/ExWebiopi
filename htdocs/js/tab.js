function FocusTab(tabname,tabcolor,colorbar) {
	// タブの色
	// 全部グレイに
	document.getElementById('tabA').style.backgroundColor = 'gray';
	document.getElementById('tabB').style.backgroundColor = 'gray';
	document.getElementById('tabC').style.backgroundColor = 'gray';
	document.getElementById('tabD').style.backgroundColor = 'gray';
	// 指定箇所のみ色を変更
	if(tabname) {
		document.getElementById(tabname).style.backgroundColor = tabcolor;
	}
}

function ChangeTab(tabname) {
// 全部消す
	document.getElementById('tab1').style.display = 'none';
	document.getElementById('tab2').style.display = 'none';
	document.getElementById('tab3').style.display = 'none';
	document.getElementById('tab4').style.display = 'none';
	// 指定箇所のみ表示
	document.getElementById(tabname).style.display = 'block';
}