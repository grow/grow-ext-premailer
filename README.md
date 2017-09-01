# grow-ext-premailer

[Premailer](https://github.com/peterbe/premailer) extension for Grow.

Exposes a filter called `premailer` that will take externally linked CSS and
inline it into all the matching selectors.

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-premailer`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
extensions:
  preprocessors:
  - extensions.premailer_ext.PremailerFilter
```
