## Requests 库的使用

requests 是 Python 的一个第三方Http库，它比Python自带的 urllib 更加的简单方便和人性化，可以让Python实现访问网页并获取源代码。

```
## 使用requests获取源代码
import requests
source = requests.get('http://www.baidu.com').content
```

### 安装

`pip install requests`

### 基本使用

对于大多数直接在浏览器输入网址就能访问的网页，使用requests的get方法就能获取到网页的源代码：

```
import requests
html = requests.get('网址').content
```

请注意，这里需要使用`.content`来显示网页的源代码。如果不加`.content`, 则得到的只会是网页访问的状态码，类似于下面这样：

    <Response [200]>

对于不能直接在浏览器中输入网址访问的页面，就需要使用requests的post方法来获取源代码。

post方法的格式如下：

```
import requests
data = {'key1': 'value1',
        'key2': 'value2'}
html = requests.post('网址', data=data).content
```

其中data这个字典的内容和项数需要根据实际情况做修改，key和value在不同的网站，是肯定不一样的。而我们做爬虫，构造这个字典是任务之一。

还有一些网址，提交的内容需要是json格式，因此我们的post方法的参数可以做一些修改：

html = requests.post('网址', json=data).content
这样写以后，requests可以自动将我们的字典转换为json字符串。

下面我通过视频，分别看下具体的 get 和 post 的应用举例。
