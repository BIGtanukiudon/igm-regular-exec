# IGM-regular-exec

情報収集管理アプリケーションの拡張アプリ。
情報収集を定期的に行い、LINE Notify により通知するスクリプト。

# 本番環境

cron により、定期実行。

## イメージビルド＆実行

```bash
docker-compose -f docker-compose.prod.yaml build
docker-compose -f docker-compose.prod.yaml up -d
```

# 開発環境

## イメージビルド＆実行

```bash
docker-compose -f docker-compose.dev.yaml build
docker-compose -f docker-compose.dev.yaml up -d
```

# 環境変数

環境変数は`.env`にて記述する。
`.env.template`からコピーする。

```.env
URL_ENDPOINT=hoge // APIのエンドポイント
LOGIN_ID=hoge
LOGIN_PW=hoge
NOTIFY_TOKEN=hoge // LINE Notifyのアクセストークン
```
