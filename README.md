# WDS-Translation-Csv

World Dai Star(世界大明星) 中文/zh-cn 翻译仓库

## 提交说明

~~原始Csv文件存放在`EpisodeCsv`，找到你需要翻译的文件，并将其复制到`tmp`文件夹，翻译完成后提交PR。~~  
~~提交通过的翻译文件会被移动到`TranslationCsv`文件夹中。~~  
~~如果要修改翻译文件，请直接在`TranslationCsv`文件夹中修改。~~  
本仓库储存基于AI翻译后调整的翻译文件，默认不接受提交，如果你需要翻译，请向上游仓库提交。

## [网页剧情播放器](https://github.com/Cpk0521/WDS_Adv_Player)

## [网页剧情播放器分支版本](https://github.com/huang207/WDS_Adv_Player)

### 本地部署教程

```bash
yarn install
npm run build
npm run preview
```

部署完成后可以访问`http://127.0.0.1:4173`播放。  
后带参数可以指定章节、自动播放以及翻译语言示例：  
`http://127.0.0.1:4173/?id=1010110&at=true&tl=zhcn`  
`id`即为剧情章节id，`tl`为翻译语言，简体中文就是`zhcn`，`at`为自动播放，请自行修改。

### 硬件加速

如果网页播放不流畅，可以尝试打开浏览器的硬件加速功能。  
以下为Chrome的步骤，其他浏览器请自行查阅。  
浏览器网址栏访问`chrome://settings/system`，开启`使用图形加速功能（如果可用）`。

### 渲染器（仅 pixi-v8 branch）

`PixiJS V8`播放器默认会在支持`WebGPU`的浏览器上使用`WebGPU`渲染器，在不支持的浏览器上会使用`WebGL`渲染器。通常来说`WebGPU`渲染器性能更好。倘若出现性能或兼容性问题，可以尝试通过指定`renderer`参数（`webgl`或`webgpu`）切换渲染器。

### Demo

[Online Demo](https://cpk0521.github.io/WDS_Adv_Player/)
[Online Demo (fork)](https://wds-adv-player.207studio.top/)

## 感谢

WDS剧情播放器：[Cpk0521/WDS_Adv_Player](https://github.com/Cpk0521/WDS_Adv_Player)  

## ★[字幕组人手绝赞募集中](https://b23.tv/vFWvqQ8)★

也许有人能看到呢？
