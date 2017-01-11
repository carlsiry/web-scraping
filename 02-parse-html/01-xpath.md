
## xPath 应用

XPath（XML Path Language）是一种HTML和XML的查询语言，他能在 XML 和 HTML 的树状结构中寻找节点。

在Python中，使用 **lxml** 库来使用XPath 技术

`pip install lxml`

### 基本使用

```
from lxml import html
selector = html.fromstring('网页源代码')
info = selector.xpath('一段XPath语句')
```

其中的网页源代码我们可以使用 **requests** 来获取。

#### XPath语句格式

来获取文本：

> //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/..../text()

获取属性值：

> //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/..../@属性n

其中，[@属性="属性值"]这个不是必需的，它的作用是帮助过滤相同的标签。
在不需要过滤相同标签的情况下，可以省略。

#### 标签的选取

标签可以直接从html这个最外层的标签开始，一层一层往下找，这个时候，我们的XPath语句是这样的：

`/html/body/div[@class="useful"]/ul/li/text()`

当从 html 开头的时候，它前面是单斜线。这样写虽然确实也可以达到目的，但是既然不是必要的，那何必多此一举呢？

如何确定从哪个标签开头？

如果唯一可以直接选取，普通元素需要从大到小指定。

#### 先抓大后抓小的运用‘

```
selector = lxml.html.fromstring(html)
info_list = selector.xpath('//ul[@class="useful"])
msg_list = []
for info in info_list:
    msg = info.xpath('li/text()')
    msg_list.append(msg)
    # print msg
```

