//・webiopi()を呼び出すことで、WebIOPiオブジェクトのインスタンスを取得できます。
//・インスタンスの準備ができたときに呼び出す処理をwebiopi().ready(callback)で
// 指定できます。callbackへは関数を指定します。
//・マクロを呼び出すボタンは、 webiopi().createMacroButton()を使って作ることが
// できます。パラメータには、HTML要素のID、ラベル、マクロ関数名、マクロ関数へのパラ
// メータ値を指定します。
webiopi().ready(function() {
  var content, button;
  content = $("#content");
  button = webiopi().createMacroButton("btn_forward", "forward", "begin_forwoard");
  content.append(button);
  button = webiopi().createMacroButton("btn_back", "back", "begin_back");
  content.append(button);
  button = webiopi().createMacroButton("btn_stop", "stop", "stop");
  content.append(button);
  webiopi().refreshGPIO(true);
});

