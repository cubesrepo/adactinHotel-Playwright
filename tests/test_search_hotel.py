import pytest

from pages.search_hotel_page import SearchHotelPage

@pytest.fixture
def search_setup(valid_login_setup):
    search_hotel_page = SearchHotelPage(valid_login_setup)
    yield search_hotel_page


def test_valid_search_hotel(search_setup):
    search_setup.search("Los Angeles",
                        "Hotel Creek",
                        "Deluxe",
                        "8 - Eight",
                        "3 - Three",
                        "4 - Four",
                        "27/05/2026",
                        "27/06/2026")


def test_invalid_search_hotel(search_setup):

    search_setup.search("- Select Location -",
                        "Hotel Creek",
                        "Deluxe",
                        "- Select Number of Rooms -",
                        "- Select Adults per Room -",
                        "4 - Four",
                        "",
                        "")

    actual_errors = search_setup.get_error_message()
    expected_errors =["Please Select a Location", "Please Select Total Number of Rooms", "Please Select Check-In Date",
                     "Please Select Check-Out Date", "Please Select Adults per Room"]

    for actual, expected in zip(actual_errors, expected_errors):
        assert actual == expected

def test_successful_booking(search_setup):
    search_setup.search("Los Angeles",
                        "Hotel Creek",
                        "Deluxe",
                        "8 - Eight",
                        "3 - Three",
                        "4 - Four",
                        "27/05/2026",
                        "27/06/2026")

    search_setup.book("First_name",
                      "Last Name",
                      "Address 1",
                      "1234567812345678",
                      "1234",
                      "VISA",
                      "February",
                      "2028")

def test_unsuccessful_booking(search_setup):
    search_setup.search("Los Angeles",
                        "Hotel Creek",
                        "Deluxe",
                        "8 - Eight",
                        "3 - Three",
                        "4 - Four",
                        "27/05/2026",
                        "27/06/2026")

    search_setup.select_hotel()
    search_setup.click_continue()
    search_setup.book_now()

    actual_error = search_setup.get_booking_error()
    expected_error = ["Please Enter your First Name", "Please Enter you Last Name",
                      "Please Enter your Address", "Please Enter your 16 Digit Credit Card Number",
                      "Please Select your Credit Card Type", "Please Select your Credit Card Expiry Month",
                      "Please Enter your Credit Card CVV Number"]

    for actual_error, expected_error in zip(actual_error, expected_error):
        assert actual_error == expected_error







