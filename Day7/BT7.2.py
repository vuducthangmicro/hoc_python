album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
#Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
album_name_value = album_info["album_name"]
print(album_name_value)
album_name_value = album_info.get("album_name")
print(album_name_value)

release_year_value = album_info["release_year"]
print(release_year_value)
release_year_value = album_info.get("release_year")
print(release_year_value)


#Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info["release_year"] = 1971
print(album_info)

#Xóa phần tử với key là track_list
del album_info["track_list"]
print(album_info)

# Thêm một key mới là amount = 2000 bằng hai cách
album_info.update(amount=2000)
print(album_info)

info = {'amount': 2000}
album_info.update(info)
print(album_info)

# Làm trống dict: album_info
album_info.clear()
print(album_info)
