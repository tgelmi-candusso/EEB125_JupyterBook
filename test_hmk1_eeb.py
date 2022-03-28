from notebook_helper import importer
import EEB125_Homework_1 as hw
import pandas as pd
import pytest

@pytest.fixture(scope='module', autouse=True)
def load_code():
    importer.run_cells(hw)
    
    
def test_variable_names_READ_ME_FIRST():
    names_in_hw = [name for name in dir(hw)
                   if not name.startswith('__') and not name in ['get_ipython', 'pandas']]
    
    msg = f'''Here are the variables you created using assignment statements:

{', '.join(names_in_hw)}
    
We expected to find all four of bluejay_df, cardinal_df, bluejay_avg, and cardinals_avg, but at least one
of them is missing or has a typo.

Please double-check the announcement we sent about Homework 1 where we discuss this, then ask
for help if you need it!

You'll be able to resubmit this homework.
'''

    assert 'bluejay_df' in dir(hw), msg
    assert 'cardinal_df' in dir(hw), msg
    assert 'bluejay_avg' in dir(hw), msg
    assert 'cardinals_avg' in dir(hw), msg
    

def test_read_data_bluejay():
    msg = f'''We called pd.read_csv("bluejay.csv") and compared it to the
value of your bluejay_df DataFrame variable, and and they were not the same.'''
    assert hw.bluejay_df.equals(pd.read_csv("bluejay.csv")), msg


def test_read_data_cardinal():
    msg = f'''We called pd.read_csv("cardinal.csv") and compared it to the
value of your cardinal_df DataFrame variable, and and they were not the same.'''
    assert hw.cardinal_df.equals(pd.read_csv("cardinal.csv")), msg


def test_compute_average_bluejay():
    # Average algorithm as mentioned in Development chat.
    # replace variable with the column name
    numbers_bluejay = hw.bluejay_df["Density per 100 ha"]
    total_bluejay = sum(numbers_bluejay)
    count_bluejay = len(numbers_bluejay)
    avg_bluejay = total_bluejay / count_bluejay
    
    msg = f'''We extracted the 'Density per 100 ha' column from the blue jay data and ran the
calculate-average algorithm on it. Our value was {avg_bluejay} but your bluejay_avg value was {hw.bluejay_avg}.

Please double-check your code, and ask for help if you need it!'''
    
    assert avg_bluejay == hw.bluejay_avg, msg


def test_compute_average_cardinal():
    # Average algorithm as mentioned in Development chat.
    # replace variable with the column name
    numbers_cardinal = hw.cardinal_df["Density per 100 ha"]
    total_cardinal = sum(numbers_cardinal)
    count_cardinal = len(numbers_cardinal)
    avg_cardinals = total_cardinal / count_cardinal
    
    msg = f'''We extracted the 'Density per 100 ha' column from the blue jay data and ran the
calculate-average algorithm on it. Our value was {avg_cardinals} but your cardinals_avg value was {hw.cardinals_avg}.

Please double-check your code, and ask for help if you need it!'''
    
    assert avg_cardinals == hw.cardinals_avg, msg
        
