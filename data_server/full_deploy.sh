APP_DIR="/Dash"

aws ec2 run-instances --image-id ami-0d5d9d301c853a04a --count 1 --instance-type t2.micro --key-name unidea --security-groups mydefault

INSTANCE_DNS=$(aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro,Name=instance-state-code,Values=16" --query "Reservations[].Instances[].PublicDnsName" | jq -r '.[0]')
REMOTE_CON="ubuntu@"$INSTANCE_DNS

# aws ec2 terminate-instances --instance-ids i-5203422c

# scp -i unidea.pem -rp "./Dash" $REMOTE_CON:='/home/ubuntu/' | y 

ssh -oStrictHostKeyChecking=no -i ~/.mycreds/unidea.pem $REMOTE_CON
git clone https://cerebrock:Mgmgmg77-@github.com/Cerebrock/realtime-nlp.git
mkdir ./App
mv realtime-nlp/Dash/* App
yes | rm -r realtime-nlp/

sudo apt update && apt upgrade
sudo snap install docker
sudo groupadd docker && sudo gpasswd -a $USER docker

#sudo systemctl daemon-reload
#snap restart docker
#sudo systemctl restart docker
#su - $USER

cd $APP_DIR
docker build -t app_docker .
docker docker run --name app_container -v $(pwd)/app:/app -v $(pwd)/data:/data -p 80:80 app_docker     
