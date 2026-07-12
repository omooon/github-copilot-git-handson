# GitHub と GitHub Copilot のハンズオン README

## 1. 目的
この README は、GitHub を使った開発フローを学びながら、GitHub Copilot を活用するハンズオン形式のガイドです。

- Git の基本操作を体験する
- GitHub のリモート連携を学ぶ
- ブランチとプルリクエストの流れを理解する
- GitHub Copilot で作業をサポートする方法を知る

## 2. 準備
### 2.1 必要なもの
- Git がインストールされていること
- GitHub アカウント
- VS Code（または GitHub Copilot対応のエディタ）
- GitHub Copilot の利用権限

### 2.2 VS Code の準備
1. VS Code を開く
2. `GitHub Copilot` 拡張機能をインストールするGitHubで公開することを前提にREADME.mdを作成してください。

目的は「GitHub Copilotを活用しながらGit/GitHubによる開発フローを学ぶ」ことです。

含めてほしい内容
- プロジェクト概要
- 前提条件
- 開発環境
- ハンズオン全体の流れ
- ステップ一覧
  - Repository作成
  - Clone
  - README作成
  - Commit
  - Branch
  - Push
  - Pull Request
  - Merge
  - Conflict解消
  - Release
- 学習後にできるようになること
- ライセンス

見やすいMarkdownで作成してください。GitHubで公開することを前提にREADME.mdを作成してください。

目的は「GitHub Copilotを活用しながらGit/GitHubによる開発フローを学ぶ」ことです。

含めてほしい内容
- プロジェクト概要
- 前提条件
- 開発環境
- ハンズオン全体の流れ
- ステップ一覧
  - Repository作成
  - Clone
  - README作成
  - Commit
  - Branch
  - Push
  - Pull Request
  - Merge
  - Conflict解消
  - Release
- 学習後にできるようになること
- ライセンス

見やすいMarkdownで作成してください。GitHubで公開することを前提にREADME.mdを作成してください。

目的は「GitHub Copilotを活用しながらGit/GitHubによる開発フローを学ぶ」ことです。

含めてほしい内容
- プロジェクト概要
- 前提条件
- 開発環境
- ハンズオン全体の流れ
- ステップ一覧
  - Repository作成
  - Clone
  - README作成
  - Commit
  - Branch
  - Push
  - Pull Request
  - Merge
  - Conflict解消
  - Release
- 学習後にできるようになること
- ライセンス

見やすいMarkdownで作成してください。GitHubで公開することを前提にREADME.mdを作成してください。

目的は「GitHub Copilotを活用しながらGit/GitHubによる開発フローを学ぶ」ことです。

含めてほしい内容
- プロジェクト概要
- 前提条件
- 開発環境
- ハンズオン全体の流れ
- ステップ一覧
  - Repository作成
  - Clone
  - README作成
  - Commit
  - Branch
  - Push
  - Pull Request
  - Merge
  - Conflict解消
  - Release
- 学習後にできるようになること
- ライセンス

見やすいMarkdownで作成してください。
3. GitHub にサインインし、Copilot を有効にする

## 3. GitHub Copilot を使うハンズオン
このセクションでは、実際に GitHub Copilot を使いながら GitHub 連携を体験します。

### 3.1 ステップ 1: リポジトリを準備する
```bash
git init
```
- すでに GitHub で作成したリポジトリがあれば、`git clone <URL>` でも OK

### 3.2 ステップ 2: GitHub Copilot で README を補完する
1. VS Code で `README.md` を開く
2. コメントや見出しを入力する
3. Copilot の提案を確認し、`Tab` で受け入れる

例:
```markdown
# プロジェクト名

## 目的
<!-- Copilot にこのプロジェクトの目的を補完させる -->
```

### 3.3 ステップ 3: 変更をステージしてコミットする
```bash
git status
git add README.md
git commit -m "README を作成"
```
- Copilot はコミットメッセージの候補を提案できるので、参考にすると早い

### 3.4 ステップ 4: GitHub にプッシュする
```bash
git remote add origin <GitHub リポジトリ URL>
git push -u origin main
```

### 3.5 ステップ 5: ブランチを作成して機能追加する
```bash
git switch -c feature/copilot-handson
```

1. `main.py` や `README.md` などを編集する
2. Copilot に「この関数を実装してください」などのコメントを書く
3. Copilot がコード候補を出したら受け入れる

例:
```python
# ユーザー名を表示する関数を実装してください
```

### 3.6 ステップ 6: 変更をコミットしてプッシュ
```bash
git add .
git commit -m "GitHub Copilot ハンズオン機能を追加"
git push -u origin feature/copilot-handson
```

### 3.7 ステップ 7: プルリクエストを作成する
1. GitHub のリポジトリページを開く
2. `Compare & pull request` をクリック
3. タイトルと詳細を書き、PR を作成する

> ここでも Copilot は PR の説明文やレビューコメントを書く際に役立ちます。

### 3.8 ステップ 8: PR をレビューしてマージする
- 自分でレビューするか、共同開発者にレビューしてもらう
- 必要に応じて修正を行い、再度コミット・プッシュする
- 問題なければ `Merge pull request` でマージする

## 4. Git と GitHub の基本操作
### 4.1 状態確認
```bash
git status
```

### 4.2 変更追加
```bash
git add <ファイル名>
# すべて追加する場合
git add .
```

### 4.3 コミット
```bash
git commit -m "メッセージ"
```

### 4.4 履歴確認
```bash
git log --oneline --graph --decorate
```

## 5. GitHub 連携の基本
### 5.1 リモート確認
```bash
git remote -v
```

### 5.2 プッシュ
```bash
git push origin <branch>
```

### 5.3 プル
```bash
git pull origin <branch>
```

## 6. ブランチ運用のおすすめ
- `main` は常に安定を保つ
- 機能ごとに `feature/` ブランチを作る
- バグ修正は `fix/` ブランチを使う
- Copilot 提案はレビュー前に必ず自分で確認する

## 7. GitHub Copilot の使いどころ
- README やドキュメントの文章補完
- 設定やコードのひな型生成
- 関数実装の提案
- コミットメッセージや PR の説明文作成

## 8. 実践のポイント
- 小さい単位でこまめにコミットする
- 変更内容をわかりやすくメッセージにする
- Copilot の提案は必ず自分の理解で検証する
- GitHub PR の流れを一度通してみる

## 9. 参考リンク
- https://github.com/features/copilot
- https://docs.github.com/ja
- https://git-scm.com/book/ja/v2
