# wsum
Scartch3.0�Ń��b�Z�[�W�Ƃ�����g�p���Ă���X�v���C�g�𒲍�����R�}���h

## Usage

wsum.exe sb3_project [csv]

Scratch3.0�̃v���W�F�N�g��n���ƁA���b�Z�[�W�Ƃ�����g�p���Ă���X�v���C�g�̃��X�g�����L��json�`���ŏo�͂��܂��B  
>{'�ϐ���1': ['�X�v���C�g1', '�X�v���C�g2'...], '�ϐ���2': ['�X�v���C�g1', '�X�v���C�g3'...] ... }

csv�I�v�V������t�����csv�`���ŏo�͂��܂��B  
>�ϐ���1, �X�v���C�g1, �X�v���C�g2  
�ϐ���2, �X�v���C�g1, �X�v���C�g3  
...

## Example


���L����_�E�����[�h�����v���W�F�N�g("Dear Lisa.sb3")�ɑ΂��Ď��s�������ʂł��B  

https://scratch.mit.edu/projects/314166329/editor/


```
wsuv.exe "Dear Lisa.sb3"
```

{'End Intro': ['Stage', 'Open Text', 'CB'], 'open card': ['Control', 'CB'], 'next': ['Stage', 'Open Text', 'Control', 'CB', 'Zinnea', 'mres', 'me_win', 'me_win2', 'Champ99', 'Lilyland', 'Khanning', 'KayOh', 'carmelo', 'Eric1', 'Eric2', 'Eric3', 'Me', 'ChrisG', 'Shruit', 'End Text', 'Thumbnail'], 'end': ['Open Text', 'Control', 'Shruit'], 'change intro slide': ['Stage', 'Open Text'], 'me_win_final': ['me_win', 'me_win2'], 'Make Art!': ['KayOh'], 'Eric': ['Eric1', 'Eric2', 'Eric3'], 'shruti': ['Shruit'], 'end-2': ['Open Text', 'End Text']}

```
wsuv.exe "Dear Lisa.sb3" csv
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

