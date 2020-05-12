# wsum
Scartch3.0でメッセージとそれを使用しているスプライトを調査するコマンド

## Usage

wsum.exe sb3_project [csv]

Scratch3.0のプロジェクトを渡すと、メッセージとそれを使用しているスプライトのリストを下記のjson形式で出力します。  
>{'変数名1': ['スプライト1', 'スプライト2'...], '変数名2': ['スプライト1', 'スプライト3'...] ... }

csvオプションを付けるとcsv形式で出力します。  
>変数名1, スプライト1, スプライト2  
変数名2, スプライト1, スプライト3  
...

## Example


下記からダウンロードしたプロジェクト("Dear Lisa.sb3")に対して実行した結果です。  

https://scratch.mit.edu/projects/314166329/editor/


```
wsum.exe "Dear Lisa.sb3"
```

{'End Intro': ['Stage', 'Open Text', 'CB'], 'open card': ['Control', 'CB'], 'next': ['Stage', 'Open Text', 'Control', 'CB', 'Zinnea', 'mres', 'me_win', 'me_win2', 'Champ99', 'Lilyland', 'Khanning', 'KayOh', 'carmelo', 'Eric1', 'Eric2', 'Eric3', 'Me', 'ChrisG', 'Shruit', 'End Text', 'Thumbnail'], 'end': ['Open Text', 'Control', 'Shruit'], 'change intro slide': ['Stage', 'Open Text'], 'me_win_final': ['me_win', 'me_win2'], 'Make Art!': ['KayOh'], 'Eric': ['Eric1', 'Eric2', 'Eric3'], 'shruti': ['Shruit'], 'end-2': ['Open Text', 'End Text']}

```
wsum.exe "Dear Lisa.sb3" csv
```

End Intro,Stage,Open Text,CB,
open card,Control,CB,
next,Stage,Open Text,Control,CB,Zinnea,mres,me_win,me_win2,Champ99,Lilyland,Khanning,KayOh,carmelo,Eric1,Eric2,Eric3,Me,ChrisG,Shruit,End Text,Thumbnail,
end,Open Text,Control,Shruit,
change intro slide,Stage,Open Text,
me_win_final,me_win,me_win2,
Make Art!,KayOh,
Eric,Eric1,Eric2,Eric3,
shruti,Shruit,
end-2,Open Text,End Text,

