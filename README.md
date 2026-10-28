# ainative-deck

<!-- aim-public-links:start -->
[AI Mindset labs](https://aimindset.org/?utm_source=website&utm_medium=article&utm_campaign=start&utm_content=github-ainative-deck#learning) · [Knowledge base](https://base.aimindset.org/?utm_source=website&utm_medium=article&utm_campaign=start&utm_content=github-ainative-deck)
<!-- aim-public-links:end -->

## World graph updates

When changing notes in `ain3-starter-pack/world/` or the manifest generator, run:

```sh
python3 tools/build-world-manifest.py
python3 tools/build-world-manifest.py --check
```

Commit `ain3-starter-pack/data/world-manifest.json` together with the source
changes in the same pull request. CI checks that the committed manifest matches
the notes; `--check` never writes files. Rebuilding unchanged content preserves
the existing update date. The manifest workflow has read-only permissions and
creates no commits or direct pushes to protected `main`. The source and its
generated manifest pass the normal PR review and `privacy` check together.
