# Color Summarizer

[demo](https://jpcolor.netlify.app/)

Color Summarizer can analyze thousands of color palettes of images and generate a 3D color model corresponding to these color palettes.

Even if you are not familiar with programming, you can use Color Summarizer with some simple configurations.

Color Summarizer supports images in `jpg`, `png`, `jpeg` formats.

## How to use in macOS

### 1. [Download](https://github.com/Itsukay/Color-Summarizer/archive/master.zip) Color Summarizer

After downloading, double click to unzip, you should see a folder named `Color-Summarizer-master`.

### 2. Download and install [Anaconda Installer](https://www.anaconda.com/products/individual)

There are two download options, using Graphical Installer makes the installation easier.

### 3. Open `Terminal` in the folder where Color Summarizer is located

Right-click on the folder (`Color-Summarizer-master`) and select **_Services > New Terminal at Folder_** to open `Terminal`.

### 4. Install `colorgram.py` and `plotly`.

Copy the following command, paste it into `Terminal`, and press ENTER.

```bash
pip3 install colorgram.py
```

You should see something is successfully installed.

Then copy the following command to install `plotly`

```bash
pip3 install plotly
```

### 5. Now try to run Color Summarizer!

Copy the following command, paste it into `Terminal`, and press ENTER.

```bash
python3 run.py
```

You should see the following output

```bash
Please enter the name of the folder you want to analyse:
```

Type `img` and press ENTER.

You should see a message that Color Summarizer ran successfully, and a webpage presents the results.

### 6. Now try with your images!

Create a new folder (e.g., `my-images`) in the folder where Color Summarizer is located and copy the your images into that folder. Then copy the following command and press the ENTER keyboard.

```bash
python3 run.py
```

Enter the folder name (in this case `my-images`) and press ENTER. Color Summarizer will tell you the estimated time of completion and will automatically display the results when it is done.

Results are store with name `[img-folder-name]_result.html`.

That's it!

****
<br>

# Color Summarizer（中文说明）

[演示](https://jpcolor.netlify.app/)

Color Summarizer 可以分析成千上万张图像的调色板，并生成与这些调色板对应的 3D 色彩模型。

即使你不熟悉编程，你也可以通过一些简单的配置来使用 Color Summarizer。

Color Summarizer 支持`jpg`、`png`、`jpeg`格式的图像。

## 如何在 macOS 中使用

### 1. [下载](https://github.com/Itsukay/Color-Summarizer/archive/master.zip)Color Summarizer

下载后，双击解压，你应该会看到一个名为 `Color-Summarizer-master`的文件夹。

### 2. 下载并安装 [Anaconda Installer](https://www.anaconda.com/products/individual)

有两种下载方式，使用 Graphical Installer 安装更容易。

### 3. 在 Color Summarizer 所在的文件夹中打开`终端`。

右击文件夹(`Color-Summarizer-master`)，选择**服务 > 新建位于文件夹位置的终端窗口**打开`终端`。

### 4. 安装`colorgram.py`和`plotly`。

复制下面的命令，粘贴到`终端`中，并按回车键。

```bash
pip3 install colorgram.py
```

你应该看到一些东西被成功安装。

然后再使用下面的命令，安装`plotly`

```bash
pip3 install plotly
```

### 5. 现在尝试运行 Color Summarizer!

复制下面的命令，粘贴到`终端`，然后按 ENTER 键。

```bash
python3 run.py
```

你应该看到以下输出

```bash
Please enter the name of the folder you want to analyse:
```

输入`img`，然后按 ENTER 键。

你应该会看到一条消息，说 Color Summarizer 运行成功，并在网页上显示结果。

### 6. 现在试试你的图像

在 Color Summarizer 所在的文件夹中创建一个新的文件夹(例如，`my-images`)，并将你的图片复制到该文件夹中。然后复制下面的命令，按 ENTER 键。

```bash
python3 run.py
```

输入文件夹名称（本例中为`my-images`），按ENTER键。Color Summarizer会告诉你完成的预计时间，并在完成后自动显示结果。

分析结果会以`[图片所在的文件夹名]_result.html`的名称存储。

就这样!

<br>
<img src="tips.jpg" width=315 ></img>