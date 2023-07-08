# tellopyというライブラリとdjitellopyのライブラリの違い


tellopyとdjitellopyは、どちらもPythonでTelloを制御するためのライブラリですが、機能や使い方に違いがあります。

tellopyは、Telloとの通信を行うためのライブラリであり、Telloの基本的な機能を制御することができます。tellopyの機能としては、Telloの離陸、着陸、上下左右の移動、回転、カメラ映像の取得などがあります。

一方、djitellopyは、tellopyを拡張したライブラリであり、より高度な機能を提供しています。djitellopyの機能としては、Telloの姿勢制御、フライトログの取得、複数のTelloの同時制御などがあります。

また、djitellopyは、OpenCVとNumPyというライブラリを使用しているため、画像処理やデータ解析にも利用することができます。

簡単にまとめると、tellopyは基本的な制御機能を提供し、djitellopyはより高度な制御機能と画像処理機能を提供しています。