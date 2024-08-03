# WDS-Translation-Csv
World Dai Star(世界大明星) 中文翻译zh-cn仓库

## 提交说明
原始Csv文件存放在`EpisodeCsv`，找到你需要翻译的文件，将其复制到`tmp`文件夹，翻译完成后提交PR  
提交通过的翻译文件会被移动到`TranslationCsv`文件夹中。  
如果要修改翻译文件，请直接在`TranslationCsv`文件夹中修改

## 剧情网页播放器（[Cpk0521/WDS_Adv_Player](https://github.com/Cpk0521/WDS_Adv_Player)）
### 本地部署教程
```
yarn install
npm run build
npm run preview
```
部署完成后可以访问`http://127.0.0.1:4173`播放。  
后带参数可以指定章节以及翻译语言示例：  
`http://127.0.0.1:4173/?id=1010110&tl=zhcn`  
`id`即为剧情章节id，`tl`为翻译语言,简体中文就是`zhcn`，请自行修改

### 硬件加速
如果网页播放不流畅，可以尝试打开浏览器的硬件加速功能，以下的Chrome的步骤，其他浏览器请自行查阅。  
浏览器网址栏访问`chrome://settings/system`，开启`使用图形加速功能（如果可用）`

### Demo
[Online Demo](https://cpk0521.github.io/WDS_Adv_Player/)

## 感谢
WDS剧情播放器：[Cpk0521/WDS_Adv_Player](https://github.com/Cpk0521/WDS_Adv_Player)  