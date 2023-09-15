# Template Website

This is the source code for a website.
At a high level, the website works as follows:

- `mkdocs` is used to generate a static website from the markdown files in `docs` and the CSS theme in `victor_theme`.
- the generated website is located in `site`
- `deploy.sh` pushes the content in `site` to a branch called `gh-pages`


## To develop

First, install dependencies and start a development server:

```
pip install -r requirements.txt
mkdocs serve
```

If you need to only modify data: change the corresponding entries in `data/*.yaml`.
If you need to modify non-data content: edit the files in `docs` to your liking.
As you make changes, the local development server should reflect those changes in real time.
Finally, deploy your changes via `bash deploy.sh`.
This command will build the static website in `site` and then push it to the correct branch.

### On modifying the template
You should rare need to modify `victor_theme`.
But in the event that you do need to modify the HTML files,
the HTML variant we use is [PugJS](https://pugjs.org/) - it makes our source files a lot smaller.
The PugJS source files `*.pug` is compiled into HTML.
Therefore, when modifying, do **not** modify HTML files directly.
Instead, modify the `*.pug` files and your changes will be compiled into HTML.
