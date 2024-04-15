# vol_tst
This was to illustrate an example of mapping *part* of a directory structure.
If you look at `docker-compose.yml`:

```
services:
  python:
    build: .
    volumes:
      - /app/msg
      - .:/app
```

The second volume instruction `- .:/app` is saying that `/app` in the container should point to the `cwd` in the host.

But the previous volume instruction `- /app/msg` has no `:` so it is essentially saying *leave the `/app/msg`* folder alone.

You can see this in the code. If you run `docker-compose up` you will be using `main.py` from the host but `one.py` and `two.py` from the container.

As long as you don't rebuild the image (don't run `docker-compose up --build`) then any changes you make in `main.py` will be reflected (in the output log messages) but changes to `one.py` and `two.py` will not, since the container is using its own internal copies thanks to the `- /app/msg` volume instruction.