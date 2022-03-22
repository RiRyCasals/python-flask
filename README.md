# Flaskメモ

- テンプレートファイルは `tenplates/` に保存する
- `render_template()` でテンプレートエンジンにテンプレートファイルデータを渡す
- 静的ファイルは `static/` に保存する
- テンプレートファイルのcss読み込みはhrefに `{{ url_for('フォルダ名', filename='ファイル名.css') }}` を指定する
- テンプレートファイル内での条件分岐は `{{% if 条件式 %}}` で始め `{{% endif %}}` で終わる
- テンプレートファイル内でのループは `{{% for ~ in ~ %}}` で始め `{{% endfor %}}` で終わる
- `{% extends "ファイル名.html" %}` でテンプレートファイルの継承ができる
- `{% block ブロック名 %}` でブロックを作ることができる
- GETメソッドの値は `request.args.get()` で受け取れる
- POSTメソッドの値は `@app.route()` に `methods=['POST']` を指定し `request.form.get()` で受け取れる
