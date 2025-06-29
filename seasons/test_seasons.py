from seasons import date_check

def main():
    test_check_dob()

def test_check_dob():
    assert date_check('2003-09-18') == ('2003', '09', '18')
    assert date_check('2003-9-18') == None
    assert date_check('2003-9-09') == None
    assert date_check('September 18, 2003') == None

if __name__ == "__main__":
    main()