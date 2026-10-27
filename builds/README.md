# Builds

The module asks for a build every two weeks that the client can run, plus a folder of experimental builds that shows progression. Builds are **git tags** on `main` (`build-01`, `build-02`, …). Each one gets an entry in [CHANGELOG.md](CHANGELOG.md) written from [templates/build-notes.md](../templates/build-notes.md). Prototype 1 (Dec), Prototype 2 (Feb) and the final release (`v1.0.0`) are marked in the changelog.

Check out any build with `git checkout build-NN`. Don't commit binaries here. If a build produces a package or container, attach it to a GitHub Release for that tag.
