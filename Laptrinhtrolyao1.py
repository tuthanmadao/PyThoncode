"""
    1 - Giới thiệu về Ứng dụng.
    Đây là ứng dụng trợ lý ảo sơ khai với một vài ứng dụng cơ bản như:
        + Xem ngày, giờ
        + Tự giới thiệu về bản thân
        + Xem thời tiết
        + Học một hoặc nhiều câu đơn giản
        + Nhắc lại các câu đã được học
    2 - Các thư viện sử dụng
    Để chạy được ứng dụng ta cần cài các thư viện sau:
        + pip install  pypiwin32
        + pip install SpeechRecognition
        + pip install gTTS
        + pip install playsound
        + pip install pyowm
"""
import speech_recognition
from gtts import gTTS
from playsound import playsound
import os
import time
from pyowm.owm import OWM
thu_trong_tuan = ["Chủ Nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"]
bot_ear = speech_recognition.Recognizer()  # Siri nghe
thoi_tiet = {
    "clear sky": "Bầu Trời quang đãng",
    "few clouds": "Trời có mây",
    "scattered clouds": "mây rải rác",
    "broken clouds": "Mây tan",
    "shower rain": "Mưa rào",
    "rain": "trời có mưa",
    "thunderstorm": "trời mưa giông",
    "snow": "Trời có tuyết",
    "mist": "trời có sương mù"
}


def ai_speak(bot_branin_mini):
    """
        Chương trình chuyển đổi chữ thành âm thanh giúp bot giao tiếp với người dùng
    :param bot_branin_mini: text cần phát âm
    :return:
    """
    # Đoạn chương trình đôi từ chữ viết sang âm thanh chị google
    tts = gTTS(text=bot_branin_mini, lang='vi')
    tts.save("Siri.mp3")  # Save file chuyển đổi vào định dạng .mp3 để phục vụ cho việc phát qua loa
    playsound("Siri.mp3")  # Phát âm thanh câu thoại của trợ lý ảo
    os.remove("Siri.mp3")  # XÓa file âm thanh


bot_brain = "Xin chào"  # Ban đầu chưa học gì nên não chưa có thông tin
print("Bạn muốn tôi làm gì: ")
ai_speak("Bạn muốn tôi làm gì: ")


def bot_listen():
    """
        Chương trình chạy tính năng nghe của bot. Bot nghe lại từ mic sau đó chuyển đổi thành chữ.
    :return: trả lại các âm tiết nghe được từ mic
    """
    with speech_recognition.Microphone() as mic:
        print("\nSiri: I'm listening")
        audio = bot_ear.record(mic, duration=5)  # Siri nghe trong vòng 3 giây sau đó tắt Mic,
    # tránh treo máy do bật Mic lien tục
        print("\nSiri: ....")
    try:
        you_mini = bot_ear.recognize_google(audio, language='vi-VN')  # nó sẽ lấy giọng của chị Google
        print("\nYou: " + you_mini)
        return you_mini
    except Exception as e:
        # Đoạn bắt Exception. Dùng Exception để bắt mọi lỗi phát sinh trong quá trình thu tiếng và chuyển đổi.
        you_mini = "Tôi không hiểu bạn nói gì."
        print("\nSiri: " + you_mini + str(e))
        return you_mini


def bot_learning():
    """
        Chương trình chạy khi bot nghe được lệnh nhắc lại theo tôi. Chương trình lập ra mục đích để dạy cho bot nói
        những câu cơ bản. Chương trình mới chỉ dạy robot nói nhưng chưa đưa vào tình huống cụ thể nên đây vẫn là học máy
        móc. Dạy sao tí đọc lại y nguyên vậy.
        sẽ được ghi dưới dạng dict.
    :return: không có giá trị trả về.
    """
    ai_speak("Bạn muốn tôi học những gì?")
    # Phát ra tiếng để báo hiệu bot sẵn sàng để học câu thoại
    with open("learing.txt", "a", encoding='utf-8') as f:
        # Mở file mặc định ghi các câu thoại người dùng dạy cho bot.
        while True:  # Vòng lặp để có thể dạy cho bot 1 hoặc nhiều câu lệnh
            print("Đọc lệnh 'kết thúc' để kết thúc việc học")
            you_mini = bot_listen().lower()  # gọi Function để chuyển tiếng thành văn bản
            if "kết thúc" in you_mini:
                # Khi có lệnh kết thức bot sẽ thoát khỏi vòng lặp while kết thúc quá trình học
                break
            if you_mini != "tôi không hiểu bạn nói gì.":
                # Chuỗi trên được mặc định khi bot ko nghe hoặc không hiểu được lệnh truyền vào
                # Lệnh if để đảm bảo rằng bot sẽ ghi lại những câu thoại mà bot thu được từ người dùng
                f.write(you_mini + '\n')
                # Ghi đoạn đọc được vào trong file định sẵn
                print("\nSiri:" + you_mini)
    return "đã học xong"


def bot_repeat():
    """
        Chương trình bot đọc theo các câu thoại được dạy
    :return: ko có giá trị trả về
    """
    with open("learing.txt", "r", encoding='utf-8') as f:
        # Mở file mặc định ghi các câu thoại người dùng dạy cho bot.
        bot_mini = f.readlines()  # Đọc tất cả các câu trong file vào bot_mini để chuẩn bị cho quá trình hoạt động sau
        print(bot_mini)
        for pt in bot_mini:  # Đọc từng câu thoại mà chương trình ghi lại được
            if pt != "" and pt != " " and pt != '\n':
                # Đọc tất cả các dòng không phải là dòng trống
                ai_speak(pt)
            else:
                continue


def bot_weather():
    """
        Bot đọc tin thời tiết. ĐỌc được ra giá trị nhiệt độ, sức gió và trạng thái thời tiết.
        Tuy nhiên vẫn hạn chế là không thay đổi được vùng cần check nhiệt độ, ko có thông số về độ ẩm..., chưa có thông
        tin về các dự báo thời tiết trong ngày. Qua đó ảnh hưởng đến việc đưa ra các thông tin hạn chế cho người dùng.
    :return: trả về giá trị nhiệt độ, sức gió và trạng thái thời tiết
    """
    owm = OWM('a4d8a1f64517055225e7a8f89fd8c9b5')
    # Khai báo với Key ID được đăng ký trên trang chủ
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place('Uong Bi, VN').weather
    # Đẩy địa điểm cần đọc nhiệt độ
    temp_dict_celsius = weather.temperature('celsius')  # đọc giá trị nhiệt độ theo độ C vào biến để xử lý
    observation = mgr.weather_at_place('Uong Bi, VN')  # Gán địa điểm cần đọc giá trị thời tiết.
    wind_dict_in_meters_per_sec = observation.weather.wind()  # Default unit: 'meters_sec'
    weather = observation.weather
    trangthaithoitiet = weather.detailed_status  # ĐỌc trạng thái thời tiết
    # Trả về các giá trị nhiệt độ, sức gió và trạng thái thời tiết.
    return temp_dict_celsius["temp"], wind_dict_in_meters_per_sec["speed"], trangthaithoitiet


def bot_weather_string(index_weather):
    """
        Chương trình phân tích các chỉ số thời tiết nhận được. Đưa ra các cảnh báo về thời tiết.
        Mặt hạn chế của bot. Hiện tại chưa lấy được các chỉ số dự báo thời tiết nên bot chỉ có thể đưa ra thông tin
        thời tiết và cảnh báo dựa trên các chỉ số hiện tại nhận được từ trang chủ.
    :param index_weather: Tuple chứa các thông số về nhiệt độ, tốc độ gió, trạng thái thời tiết.
    :return: Trả về đoạn hội thoại để bot thông báo với người dùng.
    """
    trang_thai_thoi_tiet = thoi_tiet[index_weather[2]]
    nhiet_do = index_weather[0]
    # Chia khoảng các thông tin thời tiết để đưa ra thông tin nhận định chính xác cho người dùng
    if 15 < nhiet_do < 20:
        str_nhiet_do = "Trời lạnh, chú ý mặc ấm"
    elif 20 < nhiet_do < 27:
        str_nhiet_do = "Thời tiết tương đối mát mẻ."
    elif 27 < nhiet_do:
        str_nhiet_do = "Thời tiết nắng nóng."
    else:
        str_nhiet_do = "Trời rất lạnh. Bạn nên mặc ấm"
    van_toc_gio = index_weather[1]
    if 0 <= van_toc_gio <= 5.4:
        str_van_toc_gio = "Có gió nhẹ"
    elif 5.5 <= van_toc_gio <= 10.7:
        str_van_toc_gio = "Có gió to"
    elif 10.8 <= van_toc_gio <= 17.1:
        str_van_toc_gio = "Gió lớn, Chú ý khi đi đường"
    elif 17.2 <= van_toc_gio <= 24.4:
        str_van_toc_gio = "Gió rất lớn, nguy hiểm khi ra đường"
    elif 24.5 <= van_toc_gio <= 32.6:
        str_van_toc_gio = "Gió bão, Không nên ra đường"
    else:
        str_van_toc_gio = "Gió bão, sức phá hoại lớn"
    print(f"Nhiệt độ: {nhiet_do} độ C, Vận tốc gió: {van_toc_gio} m/s, {trang_thai_thoi_tiet}")
    return "Nhiệt độ hiện tại là" + str(nhiet_do) + "độ C." + str_nhiet_do + "Vận tốc gió" + str(van_toc_gio) \
           + "mét trên giây." + str_van_toc_gio + "." + str(trang_thai_thoi_tiet)


while True:
    you = bot_listen().lower()
    if "giới thiệu" in you:
        bot_brain = """
        Tôi là AI có các chức năng cơ bản như là:
        Tự giới thiệu về bản thân.
        Lấy được ngày giờ
        lấy được thông tin thời tiết
        học một hoặc nhiều câu thoại đơn giản
        nhắc lại các câu thoại được dạy
        Hết rồi. Rất mong tôi sẽ sớm được nâng cấp nhiều chức năng hơn.
        """
    elif "giờ" in you:
        # bot sẽ lấy thông tin giờ phút giây khi nghe lệnh giờ trong câu lệnh của người dùng
        bot_brain = ("Bây giờ là: " + time.strftime("%H:%M:%S"))
    elif "ngày" in you:
        # bot sẽ lấy thông tin ngày/tháng/năm khi nghe lệnh ngày trong câu lệnh của người dùng
        bot_brain = ("Hôm nay là ngày: " + time.strftime("%d/%m/%Y"))
    elif "thứ" in you:
        # Lấy thông tin về thứ trong tuần
        bot_brain = "Hôm nay là " + thu_trong_tuan[int(time.strftime("%w"))]
    elif "học" in you:
        # Lệnh bot học
        bot_learning()
        bot_brain = "Kết thúc việc học"
    elif "nhắc lại" in you:
        # lệnh bot nhắc lại những gì được dạy
        bot_repeat()
        bot_brain = "kết thúc việc nhắc lại"
    elif "thời tiết" in you:
        # Lệnh cho bot tìm thông tin thời tiết
        bot_brain = bot_weather_string(bot_weather())
    elif "kết thúc" in you:
        # Kết thúc tác vụ của bót.
        ai_speak("Tạm biệt")
        break
    else:
        bot_brain = "tôi không hiểu"
    ai_speak(bot_brain)
