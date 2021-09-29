try: 
    from a02 import jobOffer
except: 
    pass 

def test_jobOffer():
    assert jobOffer(50000, "Peshawar")=="I’ll take it!"
def test_jobOffer2():
    assert jobOffer(40000, "Peshawar")=="No thanks, I can find something better."
def test_jobOffer3():
    assert jobOffer(50000, "Karachi")=="No way"
def test_jobOffer4():
    assert jobOffer(100000, "Karachi")=="I’ll take it!"
def test_jobOffer5():
    assert jobOffer(100000)=="I’ll take it!"
def test_jobOffer6():
    assert jobOffer(100000, 'Lahore')=="I’ll take it!"
def test_jobOffer7():
    assert jobOffer(4000,'Lahore')=="No thanks, I can find something better."

