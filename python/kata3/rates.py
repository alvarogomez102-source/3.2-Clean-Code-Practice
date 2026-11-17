class RoomRateTable:
    def rate_for(self, room_type):
        if room_type == "standard":
            return 75
        if room_type == "sea_view":
            return 110
        if room_type == "suite":
            return 180
        raise ValueError("Unknown room type")
