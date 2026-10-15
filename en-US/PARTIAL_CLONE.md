# Partial Clone Guide

[Chinese](../PARTIAL_CLONE.md)

The Dress repository contains many images. Using `--depth 1` omits older commits, but it still downloads every image in the current revision. If you only plan to modify your own directory, use a partial clone with sparse checkout. Git will initially download the commit and directory structure, then fetch file contents only for directories you check out.

> Git 2.25 or later is required. Run `git --version` to check your version.

## First Clone

Fork this repository on GitHub, then clone your own fork. Replace the username and directory placeholders with your actual values:

```bash
git clone --filter=blob:none --sparse --depth 1 https://github.com/<your-username>/Dress.git
cd Dress

# Check out only your directory. You may select it before it exists remotely.
git sparse-checkout set '<first-letter>/<your-folder-name>'
```

For example, to use `Y/Yueosa`:

```bash
git sparse-checkout set 'Y/Yueosa'
```

The working tree now contains the root documentation and `Y/Yueosa`, without other contributors' images. If your folder name starts with a number or symbol, use the `#` directory and always quote the path:

```bash
git sparse-checkout set '#/233'
```

You can now create the directory, add photos, and use `git add`, `git commit`, and `git push` normally. See the [Beginner Guide](GUIDE.md) for the complete contribution workflow.

## Manage Checked-Out Directories

List the currently selected directories:

```bash
git sparse-checkout list
```

Add another directory while keeping the existing selections:

```bash
git sparse-checkout add 'A/AnotherName'
```

To replace the current directory list, use `set` again:

```bash
git sparse-checkout set 'F/FirstName' 'S/SecondName'
```

Git downloads files from newly selected directories on demand. Smaller selections generally require less network transfer and disk space.

## Fetch More History

`--depth 1` creates a shallow clone containing only the latest commit. This does not affect the usual photo contribution and PR workflow. To fetch the full commit history, run:

```bash
git fetch --unshallow
```

This fetches the complete commit history while file contents remain available on demand through the partial clone.

## Restore the Full Repository

To place every file from the current revision in your working tree, disable sparse checkout:

```bash
git sparse-checkout disable
```

This command downloads files that have not been fetched yet and may transfer a large amount of data. The repository remains a partial clone, so files from older revisions are still downloaded on demand.

To convert the repository into a full clone containing all history and file contents, continue with:

```bash
git fetch --unshallow --no-filter
git config --unset remote.origin.partialclonefilter
git config --unset remote.origin.promisor
```

If you already ran `git fetch --unshallow`, Git will report that the repository is not shallow. Use `git fetch --no-filter` instead.

## Troubleshooting

### Why are root-level documents still present?

`git clone --sparse` uses cone mode by default. Cone mode keeps files at the repository root so documentation such as `README.md` and `GUIDE.md` remains immediately available.

### Why is the selected directory missing?

Run `git sparse-checkout list` and verify the path, capitalization, and first-letter directory. A new remote directory does not appear until you create it and add a file.

### Does a partial clone affect commits or pull requests?

No. Files outside the sparse checkout are still tracked by Git and are not deleted when you stage or commit changes in your own directory. Only modify your own directory and run `git status` before committing.

## References

- [Discussion about the repository size](https://github.com/orgs/Cute-Dress/discussions/11)
- [Git documentation: Partial Clone](https://git-scm.com/docs/partial-clone)
- [Git documentation: Sparse Checkout](https://git-scm.com/docs/git-sparse-checkout)
