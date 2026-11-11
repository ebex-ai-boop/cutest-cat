# Cutest Cat — make.fun entry (cutest-cat-01)

One picture of a cat: a tiny grey-and-white kitten with huge blue eyes,
a cute head tilt and a curled tail, looking straight at the camera.

`main.py` (Python 3.13, standard library only) copies the picture held in
this repository (`entry.png`, 1024×1024 JPEG, 146,149 bytes) to
`/output/entry.png`. The program is deterministic: running it twice writes
byte-identical output.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
