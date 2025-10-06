# Adding Your Own Hack

Thank you for allowing your ROM hack to be hosted on **Team Aqua Rom Patchers** website!  

To add your patching page, you can **fork the repository, create and make edits in your patcher's own folder, and open a pull request**. Once your PR is reviewed by a maintainer, your patcher may be added to the homepage. **None of the necessary edits require HTML knowledge and are all contained within your patcher folder** — no changes to other parts of the site are required.

---

## ROM Patching Page
Firstly we'll create your very own patching page, allowing information about your ROM hack to be displayed, external sites to be linked, and of course your patches downloaded or applied to a ROM.
```diff
└── template
+   ├── patches
+       └── *
    ├── color.css
    ├── config.js
    ├── index.html
    ├── info.md
    ├── patches.info
+   └── patches.zip
```
### Visuals
1. Duplicate the `hacks/template` folder and rename it to match the name of your game, **with no spaces**.
    > Note: This will also be part of the pages URL.
2. Inside your new folder, open `config.js` and edit it with your hack’s `title` and the ROM `base:` used for your patches.
3. Within this same file, the `discord:`, `github:`, `pokécommunity:` and/or `reddit:` fields can be filled with links in order to display buttons for each on your patching page.
4. Add a high-resolution logo for your hack to your folder, named `logo.png`. This will appear at the top of your hack’s page.
5. Open `info.md`. When adding more information such as screenshots, features, credits, etc. to this file, it will display the content on your hack page.
6. Open `color.css`. Changing the value of `--page-bg-color` will change the background colour of the patching page.

### Patches & Info
1. Create a subfolder called `patches` within your patching page directory.
2. Place your patch files inside it.
    | Only `.bps`, `.ups` and `.xdelta` patches are able to be used.
3. Open the `patches.info` file, which contains details about each patch.
    ```
    "patches": [
      {
        "file": "patchfile.bps",
        "name": "ROM Hack v1.0",
        "description": "",
        "outputName": "ROM Hack"
      }
    ]
    ```
    Edit the field shown above.
    - `"file":` is the patch file
    - `"name":` is the name displayed by the patcher
    - `"description":` is the description displayed by the patcher
    - `"outputName":` is the name of the patched ROM that is downloaded
4. Create a `patches.zip` file in your patching page directory containing all of the patches.
    > Note:
    > This `patch.zip` file cannot exceed GitHub's 100MB maximum file size.
    > If this zip file is too large, errors may occur with the patcher, although the exact file size that causes this is unknown.
    > If either of these occur, try reducing the number of patches hosted.
    
    The python script `patch_zipper.py` in the root directory of this repo is provided to help generate a properly formatted `.zip` file from your patch folder. It can by run while parsing an argument containing the directory of your patching page directory, eg. `python3 patch_zipper.py hacks/template`

---

## Optional Extras
### Other Images
Additional images can be added to your patching page, or any other place on the site, but this may require manual edits to HTML. A maintainer may assist if needed.

### Patch Creator (*Coming Soon*)
A GitHub Action automatically generates a patch file from the base **pokeemerald** ROM. The process usually takes around **15 minutes**.
