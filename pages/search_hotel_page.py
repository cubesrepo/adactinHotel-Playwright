
from utilities import test_data

class SearchHotelPage:
    def __init__(self, page):
        self.page = page

    def select_dropdown_field(self, location, hotels, room_type, no_of_rooms,
                              adults_per_room, children_per_room):
        locators = {
            test_data.search_hotel.location: location,
            test_data.search_hotel.hotels: hotels,
            test_data.search_hotel.room_type: room_type,
            test_data.search_hotel.number_of_rooms: no_of_rooms,
            test_data.search_hotel.adults_room: adults_per_room,
            test_data.search_hotel.child_room: children_per_room
        }

        for locator, value in locators.items():
            self.page.locator(locator).select_option(label=value)
    def click_search(self):
        self.page.click(test_data.search_hotel.search)

    def enter_check_in_out_date(self, check_in, check_out):
        check_in_locator = self.page.locator(test_data.search_hotel.check_in_date)
        check_out_locator = self.page.locator(test_data.search_hotel.check_out_date)
        check_in_locator.clear()
        check_out_locator.clear()

        check_in_locator.type(check_in)
        check_out_locator.type(check_out)

    def search(self, location, hotels, room_type, no_of_rooms,
                              adults_per_room, children_per_room, check_in, check_out):
        self.select_dropdown_field(location, hotels, room_type, no_of_rooms, adults_per_room, children_per_room)
        self.enter_check_in_out_date(check_in, check_out)
        self.click_search()

    def get_error_message(self):
        locators = [test_data.search_hotel.location_error, test_data.search_hotel.num_rooms_error,
                    test_data.search_hotel.check_in_error, test_data.search_hotel.check_out_error, test_data.search_hotel.adults_room_error]
        error_list = []

        for locator in locators:
            value = self.page.text_content(locator).strip()
            error_list.append(value)

        return error_list

    def select_hotel(self):
        self.page.click(test_data.search_hotel.check_box_hotel)

    def click_continue(self):
        self.page.click(test_data.search_hotel.continue_btn)


    def book_information(self, first_name, last_name, billing_address, cc_no, cvv_no):
        locators = {
            test_data.search_hotel.first_name: first_name,
            test_data.search_hotel.last_name: last_name,
            test_data.search_hotel.billing_address: billing_address,
            test_data.search_hotel.cc: cc_no,
            test_data.search_hotel.cvv_number: cvv_no,
        }

        for locator, value in locators.items():
            self.page.type(locator, value)

    def cc_dropdown_options(self, cc_type, cc_exp_month, cc_exp_year):
        locators = {
            test_data.search_hotel.cc_type: cc_type,
            test_data.search_hotel.cc_exp_month: cc_exp_month,
            test_data.search_hotel.cc_exp_year: cc_exp_year
        }

        for locator, value in locators.items():
            self.page.locator(locator).select_option(label=value)

    def book_now(self):
        self.page.click(test_data.search_hotel.book_now_btn)

    def book(self, first_name, last_name, billing_address, cc_no, cvv_no,
             cc_type, cc_exp_month, cc_exp_year):

        self.select_hotel()
        self.click_continue()
        self.book_information(first_name, last_name, billing_address, cc_no, cvv_no)
        self.cc_dropdown_options(cc_type, cc_exp_month, cc_exp_year)
        self.book_now()

    def get_booking_error(self):
        error_list = []
        locators = [test_data.search_hotel.first_name_error, test_data.search_hotel.last_name_error,
                    test_data.search_hotel.address_error, test_data.search_hotel.cc_num_error,
                    test_data.search_hotel.cc_type_error, test_data.search_hotel.cc_exp_error,
                    test_data.search_hotel.cc_cvv_error
                    ]

        for locator in locators:
            value = self.page.text_content(locator).strip()
            error_list.append(value)

        return error_list
