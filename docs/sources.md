# 資料來源

## Bridge World Standard 2017

完整的制度原文在 <https://www.bridgeworld.com/pages/readingroom/bws/bwscompletesystem.html>，一頁大約 90 KB 的 HTML。用 curl 抓的時候要帶瀏覽器的 User-Agent。舊的 `indexphp.php?page=...` 和 `default.asp?...` 網址都是 404（2026-10-04 查過）。

制度上的事實要對照原文再寫進書裡，不要憑記憶。一個容易踩的坑：BWS 2017 的 1NT - 2NT 是轉換到方塊，不是自然的邀請；邀請要走 2♠ 問範圍，或是 Stayman 之後再叫 2NT。

本書和 BWS 不同的地方，見[點數範圍](ranges.md)和[強牌 2♣](strong-2c.md)。

## 雙夢家統計

作者自己的雙夢家統計（大約一億副牌）寫在 `../pons/docs/`：

| 檔案 | 主題 |
|---|---|
| `notrump-game-threshold.md` | 3NT 的門檻 |
| `major-game-threshold.md` | 高花成局的門檻 |
| `minor-game-threshold.md` | 低花成局的門檻 |
| `notrump-slam.md` | 無王滿貫 |
| `suit-slam.md` | 有王滿貫 |
| `nltc.md`、`zar.md`、`binky-points.md` | 其他的牌力評估法 |

每一篇都按牌力尺度（大牌點、只有夢家算支持點、兩手都算支持點）和王牌張數，列出損益兩平的點數。

書裡的統計說法，例如成局或滿貫要幾點、一張王牌或一個短門值多少，先查這些文件再引用；文件沒有涵蓋的問題才另外模擬。這些研究用的尺度和書裡的表格略有不同，例如短門一律算 3、2、1 點，兩門合計十張以上再加 1 點，所以引用時要說明是哪一種尺度。
