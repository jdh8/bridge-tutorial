# 橋牌入門：從規則到二蓋一

給台大橋藝社新生的橋牌叫牌教材，零基礎也能讀。全書從規則和計分出發推導叫牌策略，最後帶出二蓋一架構，細節以 [Bridge World Standard 2017](https://www.bridgeworld.com/pages/readingroom/bws/bwscompletesystem.html) 為準。

**[線上閱讀](https://jdh8.github.io/bridge-tutorial/)**

目前第一部（規則）和第二部（從規則到策略）已經寫好，第三部之後還在寫。

## 本機建置

```sh
cargo install mdbook mdbook-replace
mdbook serve --open
```

推上 `main` 之後，GitHub Actions 會自動部署到 GitHub Pages。

## 寫作慣例

中西文排版規則寫在 [CLAUDE.md](CLAUDE.md)。原始檔一段一行；寫作時斷了行，就跑 `python3 cjk.py src/*.md` 把換行接起來，再檢查 diff。

## 授權

[MIT](LICENSE)
