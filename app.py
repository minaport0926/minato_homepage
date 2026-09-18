from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>みなとのホームページ</title>
        <style>
            /* ★ フォントファイルの読み込み設定 */
            @font-face {
                font-family: 'KeiFont';
                src: url('/static/keifont.ttf') format('truetype');
            }

            /* ★ 見出し（h1, h3）に「けいふぉんと」を適用 */
            h1, h3 {
                font-family: 'KeiFont', sans-serif;
                font-weight: normal;
            }

            /* ★ メインタイトル（みなとのホームページ）を大きく設定 */
            h1 {
                font-size: 40px;
                margin-bottom: 10px;
            }

            /* ★ h3（プロフィール・おすすめ動画・ブログ）のサイズ */
            h3 {
                font-size: 24px;
            }

            /* ★ 青色の立体ボタンのスタイル */
            .yt-button {
                display: inline-block;
                background-color: #1976d2;
                color: white !important;
                padding: 12px 24px;
                font-weight: bold;
                text-decoration: none;
                border-radius: 30px;
                box-shadow: 0 4px 0 #1565c0;
                transition: all 0.1s ease;
                margin-top: 10px;
            }
            /* ボタンを押したときの動き */
            .yt-button:active {
                transform: translateY(4px);
                box-shadow: none;
            }

            /* ★ ブログ記事カードのスタイル */
            .blog-card {
                background-color: white;
                max-width: 800px;
                margin: 20px auto 0;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                text-align: left;
                box-sizing: border-box;
            }
            .blog-item {
                border-bottom: 1px dashed #ccc;
                padding: 12px 0;
            }
            .blog-item:last-child {
                border-bottom: none;
            }
            .blog-date {
                font-size: 14px;
                color: #666;
                margin-right: 10px;
            }
            .blog-title {
                font-weight: bold;
                color: #333;
                text-decoration: none;
            }
            .blog-title:hover {
                color: #1976d2;
            }
        </style>
    </head>
    <body>
        <div style='text-align: center; background-color: #f0f8ff; min-height: 100vh; padding: 20px; box-sizing: border-box;'>
            <!-- タイトル見出し -->
            <h1 style='color: #d32f2f;'>みなとのホームページ</h1>
            
            <p>
                どうも、「みなと」といいます！<br>
                youtubeで「みなとch[ゆっくり実況]」という名前で活動しています！<br>
                主に「太鼓の達人」や「スイカゲーム」などのゆっくり実況を投稿しています！<br><br>
                <!-- 青いボタン -->
                <a href="https://www.youtube.com/@%E3%81%BF%E3%81%AA%E3%81%A8ch_Yukkuri" class="yt-button" target="_blank">▶ YouTubeチャンネルはこちら！</a>
            </p>

            <div style='display: flex; justify-content: center; align-items: center; gap: 30px; flex-wrap: wrap; margin: 20px auto; max-width: 1000px;'>
                
                <div style='background-color: white; width: 100%; max-width: 450px; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: left; box-sizing: border-box;'>
                    <h3 style='margin-top: 0; color: #d32f2f; text-align: center;'>プロフィール</h3>
                    <ul style='line-height: 1.8; margin-bottom: 0;'>
                        <li><strong>好きな食べ物：</strong> じゃがいも、りんご</li>
                        <li><strong>趣味：</strong> ゲーム、昆虫採集</li>
                        <li><strong>好きなゲーム：</strong> 太鼓の達人、スイカゲーム、フォートナイト、アンダーテールなど</li>
                        <li><strong>一言：</strong> チャンネル登録よろしくお願いします！</li>
                    </ul>
                </div>

                <div style='background-color: white; padding: 15px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                    <h3 style='margin-top: 0; color: #d32f2f; text-align: center;'>おすすめ動画</h3>
                    <iframe width="320" height="180" src="https://www.youtube.com/embed/hcundTaALEw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius: 8px; max-width: 100%;"></iframe>
                </div>

            </div>
            
            <!-- 立ち絵エリア -->
            <div style='display: flex; justify-content: center; align-items: flex-end; gap: 40px; margin-top: 20px;'>
                
                <div style='display: flex; flex-direction: column; align-items: center;'>
                    <img src='/static/通常.png' style='width: 300px;'>
                    <p style='font-weight: bold; font-size: 20px; margin-top: 10px; color: #333;'>みなと</p>
                </div>

                <div style='display: flex; flex-direction: column; align-items: center;'>
                    <img src='/static/いも.png' style='width: 270px; transform: translateY(-25px);'>
                    <p style='font-weight: bold; font-size: 20px; margin-top: 10px; color: #333;'>じゃがいもくん</p>
                </div>

            </div>

            <!-- ★ 追加：ブログゾーン -->
            <div class='blog-card'>
                <h3 style='margin-top: 0; color: #d32f2f; text-align: center;'>ブログ</h3>
                
                <div class='blog-item'>
                    <span class='blog-date'>2026.09.18</span>
                    <span class='blog-title'>ホームページを開設しました！</span>
                    <p style='margin: 5px 0 0; font-size: 14px; color: #555;'>
                        みなとの公式ホームページへようこそ！これから動画の更新情報や日常のことを書いていくので、ぜひチェックしてね！
                    </p>
                </div>

                <!-- 記事が増えたらここに追加できます -->
            </div>

        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=False)