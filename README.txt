#download plotstar directory#

wget

#Make a virtual environment#

python3 -m venv plotstar/

#change directories and activate the environment#

cd plotstar
source bin/activate

#install requirements#

pip install -r requirements.txt


#example plot command#
python plotstar.py --i run_data.star --color rlnClassNumber --z
