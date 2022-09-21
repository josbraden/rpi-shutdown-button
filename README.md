# rpi-shutdown-button

Mostly copied from: https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

## Setup

1. Place listen-for-shutdown.py under /usr/local/bin/ and mark executable
2. Put listen-for-shutdown.sh in /etc/init.d and make executable
3. Register for runtime at boot: `sudo update-rc.d listen-for-shutdown.sh defaults`
