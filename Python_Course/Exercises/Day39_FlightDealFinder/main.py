import data_manager, flight_data, notification_manager, flight_search


flight_data = flight_data.FlightData()
sheet = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
notification = notification_manager.NotificationManager()

while True:
    for key, value in sheet.new_dic.items():
        lowest_price = value
        flight_search.search_for_travel(key)
        for item in flight_search.sfly_data['data']:
            price = item['price']
            if price < int(lowest_price):
                old_price = price
                lowest_price = price
                sheet.new_dic[key] = price
                flight_data.capturing_details_of_fly(item)
                notification.send_message(flight_data)
        sheet.update_sheet(key, lowest_price)
    sheet.sendUpdate_sheet()
