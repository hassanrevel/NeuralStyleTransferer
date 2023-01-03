# Neural Style transferer
It's a package which allows you to apply style transfer on any image.

For example

That's my content image

<img alt="Content" src="https://pytorch.org/tutorials/_static/img/neural-style/dancing.jpg">

And I want to apply the following style on it.

<img alt="Style" src="https://pytorch.org/tutorials/_static/img/neural-style/picasso.jpg">

So the output will look more like this.

![Output](Example/Output.png)

## Use of it is fairly straight forward.
1. Change the directory to NeuralStyleTranferer

```commandline
cd NeuralStyleTranferer
```

2. Pip install all the packages

```commandline
pip install -r requirements.txt
```

3. Go back

```commandline
cd ..
```

4. Just run the code

```commandline
python NeuralStyleTransferer/src/Model/run.py \
> --img_url "https://pytorch.org/tutorials/_static/img/neural-style/dancing.jpg" \
> --style_url "https://pytorch.org/tutorials/_static/img/neural-style/picasso.jpg"
```
or if you have your content img and style img stored locally
```commandline
python NeuralStyleTransferer/src/Model/run.py \
> --img_dir "dancing.jpg" \
> --style_dir "style.jpg"
```

Tadda the output

![Ouput](Example/Output_.png)

This code is open source, so it means you can use it however you like.

Also, if you want to see more in it, or you're having trouble using you better let me know

Follow me on

<a href ="https://twitter.com/alihassanrevel">
    <img align="left" alt="Revel Twitter" width="25px" src="https://pbs.twimg.com/profile_images/1488548719062654976/u6qfBBkF_400x400.jpg">
</a>
<a href="https://github.com/alihassanrevel">
    <img alt="Revel's github" width="25px" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
</a>
<a href="https://www.youtube.com/channel/UCqRlg2jIdAhlUkU8GSZ0ixg">
    <img alt="Revel's Youtube" width="110" src="https://www.gstatic.com/youtube/img/branding/youtubelogo/svg/youtubelogo.svg">
</a>