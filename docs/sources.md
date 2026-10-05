# 資料來源

## Bridge World Standard 2017

完整的制度原文在 <https://www.bridgeworld.com/pages/readingroom/bws/bwscompletesystem.html>，一頁大約 90 KB 的 HTML。用 curl 抓的時候要帶瀏覽器的 User-Agent。舊的 `indexphp.php?page=...` 和 `default.asp?...` 網址都是 404（2026-10-04 查過）。

制度上的事實要對照原文再寫進書裡，不要憑記憶。一個容易踩的坑：BWS 2017 的 1NT - 2NT 是轉換到方塊，不是自然的邀請；邀請要走 2♠ 問範圍，或是 Stayman 之後再叫 2NT。

本書和 BWS 不同的地方，見[點數範圍](ranges.md)和[強牌 2♣](strong-2c.md)。

## 二蓋一的各家打法

[二蓋一的風格](two-over-one.md)用到的資料：

- Max Hardy 的制度摘要：<https://bridge-tips.co.il/wp-content/uploads/2016/09/2_1-Hardy-Max.pdf>。
- Kokish–Kraft 的制度筆記（2008）：<https://bridgewithdan.com/wp-content/uploads/2019/07/WEAK-NOTRUMP-SYSTEM-Kokish-Kraft-Jan-2008.pdf>。
- Larry Cohen 的文章：<https://www.larryco.com/bridge-articles/unifying-21-gf>。
- Bridge Winners 在 2018 年的 BW 2/1 投票系列：<https://bridgewinners.com/article/series/bridge-winners-standard-21/>。定案在 `bw-21-final-conclusions`，其中的表格是一張圖。
- kwbridge 的整理：<https://kwbridge.com/2over1.htm>。

Bridge Winners 的得票率要登入才看得到。留言不必登入：文章的 HTML 裡有 `pk: <數字>`，留言在 `/bwcomments/list/Article/<pk>/`，回傳 JSON。

Lawrence 和 Bergen 的打法目前只查到二手的整理，沒有對照原書。

## 雙夢家統計

作者自己的雙夢家統計（大約一億副牌）寫在 `../pons/docs/`：

| 檔案 | 主題 |
|---|---|
| `notrump-game-threshold.md` | 3NT 的門檻 |
| `major-game-threshold.md` | 高花成局的門檻 |
| `minor-game-threshold.md` | 低花成局的門檻 |
| `notrump-slam.md` | 無王滿貫 |
| `suit-slam.md` | 王牌滿貫 |
| `nltc.md`、`zar.md`、`binky-points.md` | 其他的牌力評估法 |

每一篇都按牌力尺度（大牌點、只有夢家算支持點、兩手都算支持點）和王牌張數，列出損益兩平的點數。

書裡的統計說法，例如成局或滿貫要幾點、一張王牌或一個短門值多少，先查這些文件再引用；文件沒有涵蓋的問題才另外模擬。這些研究用的尺度和書裡的表格略有不同，例如短門一律算 3、2、1 點，兩門合計十張以上再加 1 點，所以引用時要說明是哪一種尺度。
