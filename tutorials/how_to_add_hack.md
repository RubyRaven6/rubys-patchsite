# Adding Your Own Hack

Thank you for allowing your ROM hack to be hosted on **Team Aqua Rom Patchers** website!  

To add your patching page, you can **fork the repository's `patchless` (default) branch, create and make edits in your patcher's own folder, and open a pull request to the master branch**. Once your PR is reviewed by a maintainer, your patcher may be added to the homepage. **None of the necessary edits require HTML knowledge and are all contained within your patching page folder** — no changes to other parts of the site are required.

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
1. First, you must create your ROM Patching folder. This can be done two ways:
    - In the root of your fork, use the python script `python3 scripts/new_hack.py name` where `name` is your hack name **with no spaces**.
    - Duplicate the `hacks/template` folder and rename it to match the name of your game, **with no spaces**.
    > Note: Your hack name will also be part of the pages URL.
2. Inside your new folder, open `config.js` and edit it with your hack’s `title:` and the ROM `base:` used for your patches.
3. Within this same file, the `discord:`, `github:`, `pokécommunity:` and/or `reddit:` fields can be filled with links in order to display buttons for each on your patching page.
4. Add a high-resolution logo for your hack to your folder, named `logo.png`. This will appear at the top of your hack’s page.
5. Open `info.md`. When adding more information such as screenshots, features, credits, etc. to this file, it will display the content on your hack page.
6. Open `color.css`. Changing the colours within this will change parts of the patching page.
    - `--page-title-color` will edit the title colour
    - `--page-bg-color` will change the background colour
    - `--page-rom-patcher-link-color` will change the link colour below the rom patcher from the default if defined

### Patches & Info
1. If it doesn't already exist, create a subfolder called `patches` within your patching page directory.
2. Place your patch files inside it.
    > Only `.bps`, `.ups` and `.xdelta` patches are able to be used.
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
4. Create a `patches.zip` file in your patching page directory containing all of the patches. It is recommended this is done by following the below instructions, but it can also be done manually, ~~or by making sure the PR starts with the name `[ZIP PATCHES]`~~ (*coming soon*).
    > Note:
    > This `patch.zip` file cannot exceed GitHub's 100MB maximum file size.
    > If this zip file is too large, errors may occur with the patcher, although the exact file size that causes this is unknown.
    > If either of these occur, try reducing the number of patches hosted.
    
    The python script `patch_zip.py` in the `scripts` folder is provided to help generate a properly formatted `.zip` file from your patch folder. It can by run while parsing an argument containing the directory of your patching page directory, eg. `python3 scripts/patch_zip.py hacks/template`.

---

## Optional Extras
### Other Images
Additional images can be added to your patching page, or any other place on the site, but this may require manual edits to HTML. A maintainer may assist if needed.

### Automatic Patch Creator (*Coming Soon*)
While a patch can easily be created on the [RomPatcher.js](https://www.marcrobledo.com/RomPatcher.js/) website, legally obtaining a Pokémon Emerald, Pokémon FireRed or Pokémon LeafGreen ROM may not be possible for everyone. To help with this, there is a GitHub Action that automatically generates a patch file using **pokeemerald** or **pokefirered** when you create a release of your ROM hack on GitHub. This bypasses the need to obtain the ROM yourself, with the process usually taking around **15 minutes**.

