# Publish the reading pages

The repository contains a complete static site. It needs no server, build step, API key, or database.

In this repository on GitHub, open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **main** and **/(root)**, then save. GitHub will show the published site address once deployment finishes. The included `.nojekyll` file keeps the prebuilt HTML unchanged.

[GitHub: configure a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

The reading pages work on a phone. Download the notebooks to a computer and follow Module 0 to run them.

To regenerate the reading pages after editing the Markdown or notebooks, install the maintainer dependency `markdown` and run `python build_handbook.py`. Commit the changed HTML files along with the source files. Do not run `build_notebooks.py` over completed personal exercises: it overwrites notebooks.
