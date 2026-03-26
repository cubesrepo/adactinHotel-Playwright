

base_url = 'https://adactinhotelapp.com/'
credentials = {
    "valid_username": "merofa4553",
    "valid_password": "merofa4553_pass",
    "invalid_username": "user_1_invalid",
    "invalid_password": "user_1_invalid_pass"
}

class menu:
    search_hotel = "a[href='SearchHotel.php']"
    booked_itinerary = "a[href='BookedItinerary.php']"
    change_pass = "a[href='ChangePassword.php']"

class login:
    username = "#username"
    password = "#password"
    login_btn = "#login"
    error_message = "div[class='auth_error'] b"

class search_hotel:
    location = "#location"
    hotels = "#hotels"
    room_type = "#room_type"
    number_of_rooms = "#room_nos"
    check_in_date = "#datepick_in"
    check_out_date = "#datepick_out"
    adults_room = "#adult_room"
    child_room = "#child_room"
    search = "#Submit"

    check_box_hotel = "#radiobutton_0"
    continue_btn = "#continue"
    cancel_btn = "#cancel"
    please_select_hotel = "#radiobutton_span"

    location_error = "#location_span"
    num_rooms_error = "#num_room_span"
    check_in_error = "#checkin_span"
    check_out_error = "#checkout_span"
    adults_room_error = "#adults_room_span"

    first_name = "#first_name"
    last_name = "#last_name"
    billing_address = "#address"
    cc = "#cc_num"
    cc_type = "#cc_type"
    cc_exp_month = "#cc_exp_month"
    cc_exp_year = "#cc_exp_year"
    cvv_number = "#cc_cvv"
    book_now_btn = "#book_now"
    book_cancel_btn = "#cancel"

    first_name_error = "//label[@id='first_name_span']"
    last_name_error = "//label[@id='last_name_span']"
    address_error = "//label[@id='address_span']"
    cc_num_error = "#cc_num_span"
    cc_type_error = "#cc_type_span"
    cc_exp_error = "#cc_expiry_span"
    cc_cvv_error = "#cc_cvv_span"
    "https://adactinhotelapp.com/BookingConfirm.php"
class iterinary:
    cancel_selected = "input[value='Cancel Selected']"
