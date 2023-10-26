#!/bin/bash
# This is the autorun script for our standard 6 merchant regression test
echo "Autorun script for regression library has started. Please monitor Slack for progress"
echo "Running default data path tests"
echo "Running REI..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=REI.com > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1 
echo "Running Black Diamond..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=black_diamond_equipment > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1 
echo "Running Carousel Checks..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=Carousel_Checks > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1 
echo "Running Palmetto..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=Palmetto_State_Armory > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1
echo "Running RTIC..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=RTIC_Outdoors > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1 
echo "Running A Life Plus..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=A_Life_Plus > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1 
echo "Running Redshift data path tests"
echo "Running REI..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=REI.com --source=fact_redshift > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1
echo "Running Black Diamond..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=black_diamond_equipment --source=fact_redshift > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1
echo "Running Carousel Checks..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=Carousel_Checks --source=fact_redshift > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1
echo "Running Palmetto..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=Palmetto_State_Armory --source=fact_redshift > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1
echo "Running RTIC..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=RTIC_Outdoors --source=fact_redshift > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1
echo "Running A Life Plus..."
python3.8 /home/ubuntu/ds-data_validation/deploy.py --merchant=A_Life_Plus --source=fact_redshift > /home/ubuntu/ds-data_validation/logs/data_validation.log 2>&1
echo "Done!"
