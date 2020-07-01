# PythonLibrary cheetsheet

cheetsheet

## 読み込み書き込み
### csv を読み込む
<details><summary> ###Qiita(キータ)は、プログラマのための技術情報共有サービスです。</summary>プログラミングに関することをどんどん投稿して、知識を記録、共有しましょう。
Qiitaに投稿すると、自分のコードやノウハウを見やすい形で残すことができます。
技術情報はテキストファイルへのメモではなく、タグを付けた文章、シンタックスハイライトされたコードで保存することで初めて再利用可能な知識になる、そうQiitaでは考えています。</details>


```
import re 
import csv

with open(csvfile,encoding="UTF-8") as f:
    for line in csv.reader(fr):
        x = list(line)
```

### csv を書き込む
```
with open(csvfile, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["year", "80s","90s","00s","10s"])
```

### ファイルを読み込む

```
with open(file,encoding="UTF-8") as f:
    for line in f:
        x = re.split('[,\n()]',line)
```

### ファイルを書き込む
```
with open(file, 'w') as f:
    f.write("\n")
```
