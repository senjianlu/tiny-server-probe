cd /root/GitHub/tiny-server-probe/main
screen -S tiny-server-probe -X quit
screen -wipe
screen -dmS tiny-server-probe
sleep 1s
screen -S tiny-server-probe -X stuff 'uvicorn main:app --port 57191 --host 0.0.0.0\n'