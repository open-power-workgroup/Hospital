## [English translation](README_en.md)

# 这是什么？

本项目的意图是收集汇总与国内一些医疗机构有关的开放数据，供广大寻医问药的患者及家属参考。

本项目由Open Power小组共同维护。Open Power小组是一个由志愿者组成的工作组，我们深知自己的能力有限，因此我们只能分享我们当前所知的信息，确保我们没有捏造信息，并努力提高信息的可信度。至于这些信息应该如何指导行动，我们保持缄默。

本项目所有信息基于[OPW开放数据使用授权协议](open_data_usage_license.md)发布。

请进入[数据发布网站](http://open-power-workgroup.github.io/Hospital)获取医院信息开放数据。

---


# 第一批医院名单

本项目的第一批医院名单来源于[凤凰网医院名单](http://news.ifeng.com/mainland/special/ptxyy/)，后根据社区热心人的贡献汇总而成。进入这份名单的医院符合以下三个条件中的至少一个：

- 曾经投放百度竞价广告
- 曾经被媒体报道过医疗欺诈事件
- 与[莆田系](https://zh.wikipedia.org/wiki/莆田系)存在直接关系

Open Power小组会以这三个入选条件作为指导原则，明确更详细的审核标准和流程。由于信息确认工作十分复杂，工作量很大，希望所有热心人积极提供信息或线索。

本项目也需要更多的热心人、尤其是有技术背景的热心人加入贡献核心架构。如果有兴趣加入，请在Issues里面申请。

# 贡献者指南

提交贡献之前，请先阅读[贡献者指南](guide.md)。

# 开发者指南

1. 开发者如果需要使用本 repo 的数据，可以通过 [`resource/API_resource/`](resource/API_resource) 中的 yaml 和 json 文件来获取数据
  * 如果发现数据不同步，可以 fork 之后用 `python update.py` 来更新 yaml 和 json 文件，并提交 pull request
  * 如果发现 `update.py` 运行过程中有 Warning，或者 json 和 yaml 中有错误，可以通过 `python update.py debug` 来 debug 所有的输出结果。
    程序运行的 log 会写在根目录中的 `debug.log` 中。`debug.log` 不会被 commit。
2. 本项目所有代码遵守 [GPL V3.0 协议](https://opensource.org/licenses/GPL-3.0)
3. 所有基于本项目的其他项目，包括使用源码，和使用 api 的项目必须开源。[原因请看此处](https://github.com/open-power-workgroup/Hospital/issues/224)

# 特别申明
1. 本项目不会有任何商业目的。如果出现不当的情况，请大家及时指出，并随时监督。
1. 本项目收录的信息均来自互联网，仅为资源共享、学习参考之目的。作者对信息的可用性、准确性或可靠性不作任何承诺与保证。
1. 如果您对本项目提供的信息有任何异议，请第一时间在Issues里面提出。如情况属实的，我们会第一时间予以删除，并同时向您表示歉意。
1. 本项目收录的“用户反馈”，同样来自于互联网，也可能存在不实的问题。如果您对这些用户反馈有疑问或异议，也请及时直接通过Issues提交。
1. 本项目最初的维护者@langhua9527，由于个人原因已经退出本项目的维护。目前本项目由Open Power团队负责管理，管理员是@fakeforreg和@xokctah

# 关联项目
1. 基于凤凰网数据的[医院地图](https://github.com/wandergis/hospital-viz) 
1. [饥猪阅读（Piggy Reader）](https://github.com/huntbao/piggyreader)采用本项目数据在用户浏览时加以提示
2. [用于Firefox的浏览器脚本](https://github.com/open-power-workgroup/Hospital/issues/213)，在Firefox中对用户加以提示
1. 一个[有情怀的医院查询插件](https://github.com/fushenghua/GetHosp/)
1. 基于凤凰网莆田医院数据做的[Android原生应用](https://github.com/neuyu/BlackHospital),可以定位到用户所在城市
1. 其他四个浏览器插件[@erichuang199](https://github.com/erichuang1994/PTXNotification)和[@zhangjh](https://github.com/zhangjh/chromeExt)和[@hustcc](https://github.com/hustcc/PTHospital.chrome)和[@Pearyman](https://github.com/open-power-workgroup/Hospital/issues/195)
