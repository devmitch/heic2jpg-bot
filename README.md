# heic2jpg-bot
A simple Discord bot that looks for attachments with `.heic` or `.heif` extensions,
converts them with `heif-convert` to a JPEG, and then uploads back onto discord. Deployed on Heroku.

I made this because my students on Discord often upload photos from Apple devices which are HEIF files, and
Discord cannot preview these files, so I would either have to use an external program to view them
or convert them manually to a JPEG.

## Setup:

`python3 -m pip install -r requirements.txt`

`sudo apt install libheif-examples`

## Notes
`Procfile`, `Aptfile` and `runtime.txt` are Heroku specific files, you do not need them to run/deploy the bot if you are not using Heroku.
