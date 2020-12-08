"""
    1 - Giới thiệu về Ứng dụng
"""
import speech_recognition
from gtts import gTTS
from playsound import playsound
import os
import time
thu_trong_tuan = ["Chủ Nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"]
bot_ear = speech_recognition.Recognizer()  # Siri nghe


def ai_speak(bot_branin_mini):
    """
        Chương trình chuyển đổi chữ thành âm thanh giúp bot giao tiếp với người dùng
    :param bot_branin_mini: text cần phát âm
    :return:
    """
    tts = gTTS(text=bot_branin_mini, lang='vi')
    tts.save("Siri.mp3")
    playsound("Siri.mp3")
    os.remove("Siri.mp3")


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
        # audio = bot_ear.listen(mic)
        audio = bot_ear.record(mic, duration=5)  # Siri nghe trong vòng 3 giây sau đó tắt Mic,
    # tránh treo máy do bật Mic lien tục
        print("\nSiri: ....")
    try:
        you_mini = bot_ear.recognize_google(audio, language='vi-VN')  # nó sẽ lấy giọng của chị Google
        print("\nYou: " + you_mini)
        return you_mini
    except:
        you_mini = "Tôi không hiểu bạn nói gì."
        print("\nSiri: " + you_mini)
        return you_mini


def bot_learning():
    """
        Chương trình chạy khi bot nghe được lệnh nhắc lại theo tôi. Chương trình lập ra mục đích để dạy cho bot nói
        những câu cơ bản tùy theo đoạn hội thoại nhất định. Các câu bot học được sẽ lưu vào một file.txt. Các câu thoại
        sẽ được ghi dưới dạng dict.
    :return: không có giá trị trả về.
    """
    with open("learing.txt", "a", encoding='utf-8') as f:
        you_mini = bot_listen()
        if you_mini != "":
            f.write(you_mini + '\n')


def bot_repeat():
    """
        Chương trình bot đọc theo các câu thoại được dạy
    :return: ko có giá trị trả về
    """
    with open("learing.txt", "r", encoding='utf-8') as f:
        bot_mini = f.readline()
        if bot_mini != "" or bot_mini != " " or bot_mini != "\n":
            ai_speak(bot_mini)
        else:
            ai_speak("không có gì để nói")


you = bot_listen()
if "giới thiệu" in you:
    bot_brain = """
    Tôi là AI có chức năng cơ bản. Các chức năng hiện tại của tôi là:
    Tự giới thiệu về bản thân.
    Lấy được ngày giờ
    Hết rồi. Rất mong tôi sẽ sớm được nâng cấp nhiều chức năng hơn.
    """
elif "giờ" in you:
    bot_brain = ("Bây giờ là: " + time.strftime("%H:%M:%S"))
elif "ngày" in you:
    bot_brain = ("Hôm nay là ngày: " + time.strftime("%d/%m/%Y"))
elif "thứ" in you:
    bot_brain = "Hôm nay là " + thu_trong_tuan[int(time.strftime("%w"))]
elif "học" in you:
    bot_learning()
elif "nhắc lại" in you:
    bot_repeat()
else:
    bot_brain = "tôi không hiểu"
ai_speak(bot_brain)
